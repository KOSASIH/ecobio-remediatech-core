#!/bin/bash

# run_experiments.sh

# Enable strict error handling
set -euo pipefail

# Logging function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log "Starting experiments..."

# Activate the virtual environment
source venv/bin/activate

# Run the experiment script
log "Running the experiment..."
python examples/example_experiment.py

log "Experiments completed successfully."
