#!/bin/bash

# Execuatr antes
# docker buildx create --name mybuilder --use --bootstrap

cd ../hom/tests
docker buildx build --platform linux/amd64,linux/arm64 --tag larc-et/tests:local .

cd ../../../logs-transparentes/backend/bu_service
docker buildx build --platform linux/amd64,linux/arm64 -t larc-et/bu-service:local .

cd ../public
docker buildx build --platform linux/amd64,linux/arm64 --tag larc-et/back-pub:local .

cd ../../frontend_new
docker buildx build --platform linux/amd64,linux/arm64 --tag larc-et/frontend:local .

cd ../tlmanager
docker buildx build --platform linux/amd64,linux/arm64 --tag larc-et/tlmanager:local .
