#!/bin/bash

cd ../hom/tests
docker build -t larc-et/tests:local .

cd ../../../logs-transparentes/backend/bu_service
docker build -t larc-et/bu-service:local .

cd ../public
docker build -t larc-et/back-pub:local .

cd ../../frontend_new
docker build -t larc-et/frontend:local .

cd ../tlmanager
docker build -t larc-et/tlmanager:local .