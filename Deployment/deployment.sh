#!/bin/bash

PROJECT_ID="msbancoalpes"
ZONE="us-central1-a"

gcloud deployment-manager deployments create form-deployment --config Deployment/deployment.yaml --project $PROJECT_ID
