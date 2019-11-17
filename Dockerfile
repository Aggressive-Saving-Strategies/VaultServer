FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=true
ENV PYTHONPATH=.

WORKDIR /opt/vault
COPY . .

RUN pip install bottle requests

CMD python -m vaultserver
