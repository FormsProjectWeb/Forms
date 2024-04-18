#!/bin/bash

PROJECT_ID="master-vehicle-420613"
ZONE="us-central1-a"

gcloud deployment-manager deployments create form-deployment --config Deploy/deployment.yaml --project $PROJECT_ID
