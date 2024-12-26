#!/bin/bash

API_VERSION="2024-02-01"

export OPENAI_API_VERSION=$API_VERSION

# =====================================================
# Using forked tera-sample-files with RESTful API build
# =====================================================
# Clone the repositories

# Extract the tar file
cd tera-sample-files/data/ || { echo "Failed to change directory to tera-sample-files/data"; exit 1; }
tar zxvf neo4j.tgz
cd ../
# Start Docker Compose services
pip install docker
docker compose up -d

# Copy .env.sample to .env
cp .env.sample .env
pip install -r requirements.txt
cd ../

# Update models.json with API_ENDPOINT and API_ENV_KEY
cd tera-backend/tera_backend/conf/
jq --arg api_endpoint "$AZURE_OPENAI_URI" --arg api_env_key "$AZURE_OPENAI_TOKEN" \
   'map(if .type == "azure-gpt-4o" or .type == "azure-text-embedding-ada" 
        then .api_endpoint = $api_endpoint | .api_env_key = $api_env_key 
        else . end)' models.json > temp.json && mv temp.json models.json
cd ../../

cd ../tera-sample-files/
python setup_fastapi_service.py

# # =====================================================
# # Using tera-sample-files
# # =====================================================
# # Clone the repositories
# git clone git@gitlab.com:imda_dsl/t2po/tech-analysis-tool/tera-backend.git
# git clone git@gitlab.com:imda_dsl/t2po/tech-analysis-tool/sample-files.git

# # Install python multi part
# pip install python-multipart

# # Extract the tar file
# cd tera-sample-files/data/ || { echo "Failed to change directory to tera-sample-files/data"; exit 1; }
# tar zxvf neo4j.tgz
# cd ../
# # Start Docker Compose services
# docker compose up -d

# # Copy .env.sample to .env
# cp .env.sample .env
# pip install -r requirements.txt
# cd ../

# # Update models.json with API_ENDPOINT and API_ENV_KEY
# cd tera-backend/tera_backend/conf/
# jq --arg api_endpoint "$AZURE_OPENAI_ENDPOINT" --arg api_env_key "$AZURE_OPENAI_API_KEY" \
#    'map(if .type == "azure-gpt-4o" or .type == "azure-text-embedding-ada" 
#         then .api_endpoint = $api_endpoint | .api_env_key = $api_env_key 
#         else . end)' models.json > temp.json && mv temp.json models.json
# cd ../../../

# # Set up apigw
# cd tera-backend/tera_backend/apigw

# # Generate password
# python -m apikey_manager create --name newkey
# python -m apikey_manager list

# # Update NEO4J_PASSWORD in .env file
# cp .env.dev .env
# sed -i '' 's/^NEO4J_PASSWORD=.*/NEO4J_PASSWORD=password/' .env
# cd ../../

# # Run apigw
# python -m tera_backend.apigw
