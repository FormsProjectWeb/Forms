#!/bin/bash

PROJECT_ID="singular-cache-415315"
ZONE="us-central1-a"

gcloud deployment-manager deployments create form-deployment --config Deploy/deployment.yaml --project $PROJECT_ID
