FROM python:3.8.3-alpine

RUN apk add --no-cache --upgrade bash

ENTRYPOINT ["/bin/bash"]

RUN apk --no-cache add curl

RUN adduser codeship --disabled-password

USER codeship:codeship

WORKDIR /home/codeship/odyssey

COPY . /home/codeship/odyssey
