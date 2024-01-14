#!/bin/bash
docker stop API-TRANSCRIPTOR-GRPC
docker rm API-TRANSCRIPTOR-GRPC
docker image rm api-transcriptor-grpc:1.0.0

app="api-transcriptor-grpc:1.0.0"
docker build -t ${app} -f Dockerfile ..
docker-compose -f api-transcriptor-grpc.yml -p API-TRANSCRIPTOR-GRPC up -d