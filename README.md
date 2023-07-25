# simple_file_server
A django application that uploads file to azure blob storage asynchronously with celery using redis as a message broker.

A simplest file server for any web application.

![Screenshot from 2023-06-23 22-23-01](https://github.com/deshrit/celery_azure_blob/assets/59757711/288248f7-7edd-4be5-8170-9478ace208f9)


# To run locally
### 1. Create `./.env` file
```bash
# Use your configs

# Django
DEBUG=
SECRET_KEY='your_credential'
ALLOWED_HOSTS='0.0.0.0 127.0.0.1 localhost'

# Celery
CELERY_BROKER_URL='redis://redis:6379/'

# Azure Blob Storage
CONNECTION_STRING='your_credential'
STORAGE_ACCOUNT_NAME='your_credential'
STORAGE_ACCOUNT_KEY='your_credential'
CONTAINER_NAME='your_credential'

```
### 2. Must have docker and docker compose
```
docker compose up
```

### 3. Application access
```
http://0.0.0.0:8008
```
