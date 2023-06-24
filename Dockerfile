FROM python:3.11.4-slim-bookworm

ENV PYTHONUNBUFFERED 1

WORKDIR /celery_azure_blob

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p vol/db && \
    useradd -M celery_azure_blob && \
    chown -hR celery_azure_blob:celery_azure_blob vol && \
    chmod a+x startup.sh

USER celery_azure_blob

CMD [ "./startup.sh" ]