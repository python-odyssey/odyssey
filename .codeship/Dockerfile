FROM python:3.8.3-alpine

WORKDIR /app

RUN apk add --no-cache --upgrade bash

ENTRYPOINT ["/bin/bash"]

RUN apk --no-cache add curl

COPY . /app
