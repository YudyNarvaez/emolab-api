#!/bin/bash
set -e

aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 852736037849.dkr.ecr.us-west-1.amazonaws.com/sentimiento-api:latest
docker build -t sentimiento-api .
docker tag sentimiento-api:latest 852736037849.dkr.ecr.us-west-1.amazonaws.com/sentimiento-api
docker push 852736037849.dkr.ecr.us-west-1.amazonaws.com/sentimiento-api:latest
sls deploy