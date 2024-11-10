#!/bin/bash

# deploy_model.sh

# Enable strict error handling
set -euo pipefail

# Logging function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log "Deploying model..."

# Activate the virtual environment
source venv/bin/activate

# Check if the model file exists
MODEL_FILE="model.pkl"
if [[ ! -f "$MODEL_FILE" ]]; then
    log "Error: Model file $MODEL_FILE not found!"
    exit 1
fi

# Deploy the model (this is a placeholder for actual deployment logic)
log "Deploying model from $MODEL_FILE..."
# Here you would add the actual deployment commands, e.g., copying files, starting services, etc.

log "Model deployed successfully."
