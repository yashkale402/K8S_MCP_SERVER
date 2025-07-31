#!/bin/bash

# Architecture Diagram Generator Script
# Regenerates the PNG and SVG architecture diagrams

set -e

echo "🎨 Regenerating Kubernetes Architecture Diagram..."

# Check if Python3 and matplotlib are installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Installing..."
    sudo apt-get update && sudo apt-get install -y python3-pip python3-matplotlib
fi

# Generate the diagram
cd "$(dirname "$0")/.."
python3 generate_diagram.py

echo "✅ Architecture diagrams regenerated successfully!"
echo "📁 Files created:"
echo "   - kubernetes-architecture-diagram.png (High-resolution PNG)"
echo "   - kubernetes-architecture-diagram.svg (Vector SVG)"

# Optional: Add to git if in a git repository
if [ -d ".git" ]; then
    read -p "Add diagrams to git? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add kubernetes-architecture-diagram.png kubernetes-architecture-diagram.svg
        echo "✅ Diagrams added to git staging area"
    fi
fi
