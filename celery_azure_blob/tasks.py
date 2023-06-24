from celery import shared_task
from celery.utils.log import get_task_logger

from django.conf import settings

import os
import uuid
from .models import File
from azure.storage.blob import BlobServiceClient


logger = get_task_logger(__name__)


CONNECTION_STRING = os.getenv('CONNECTION_STRING')
STORAGE_ACCOUNT_NAME = os.getenv('STORAGE_ACCOUNT_NAME')
STORAGE_ACCOUNT_KEY = os.getenv('STORAGE_ACCOUNT_KEY')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')


TMP_DIR = settings.BASE_DIR / 'vol' / 'tmp'

# one and only task in this module
@shared_task
def upload_file_to_azure(file_name):
    blob_service_client = BlobServiceClient.from_connection_string(
        CONNECTION_STRING
    )
    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=file_name
    )
    with open(TMP_DIR / file_name, "rb") as f:
        _ = blob_client.upload_blob(f.read())
    os.remove(TMP_DIR / file_name)
    logger.info(f"{file_name} uploaded successfully")


def get_uploaded_files():
    blob_service_client = BlobServiceClient.from_connection_string(
        CONNECTION_STRING
    )
    container_client = blob_service_client.get_container_client(
        CONTAINER_NAME
    )
    return list(container_client.list_blob_names())


def save_file_in_server(file, filename):
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)
    with open(TMP_DIR / filename, "wb+") as d:
        for chunk in file.chunks():
            d.write(chunk)


def handle_files_upload(files):
    for file in files:
        name, ext = os.path.splitext(file.name)
        blobname = str(uuid.uuid4())
        f_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{blobname}"
        save_file_in_server(file, blobname)
        db = File(
            file_name = name,
            blob_name = blobname,
            file_ext = ext,
            file_url = f_url
        )
        db.save()
        upload_file_to_azure.delay(blobname)

