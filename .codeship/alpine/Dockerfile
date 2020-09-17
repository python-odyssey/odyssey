FROM python:3.8.3-alpine

ENV TOXENV=py38

RUN apk add --no-cache --upgrade bash

ENTRYPOINT ["/bin/bash"]

RUN apk --no-cache add curl build-base libffi-dev openssl-dev python3-dev git libxml2 libxslt 

RUN adduser codeship --disabled-password

WORKDIR /home/codeship/odyssey

COPY --chown=codeship:codeship . /home/codeship/odyssey

RUN chown -R codeship:codeship /home/codeship

USER codeship:codeship
