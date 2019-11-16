FROM python:3.7-alpine

WORKDIR /opt/vault
COPY . .

RUN pip install bottle

CMD python -m vaultserver
