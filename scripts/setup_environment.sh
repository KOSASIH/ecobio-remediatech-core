#!/bin/bash

# setup_environment.sh

# Enable strict error handling
set -euo pipefail

# Logging function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log "Setting up the development environment..."

# Update package list
log "Updating package list..."
sudo apt-get update

# Install Python and pip
log "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
log "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
log "Installing required Python packages..."
pip install -r requirements.txt

log "Development environment setup complete."
