#!/bin/bash

# Kubernetes Cluster Setup Script
# This script sets up a complete Kubernetes development environment using kind

set -e

echo "🚀 Starting Kubernetes Cluster Setup..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "📦 Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo usermod -aG docker $USER
    sudo systemctl enable docker
    echo "✅ Docker installed successfully"
else
    echo "✅ Docker is already installed"
fi

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo "📦 Installing kubectl..."
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/
    echo "✅ kubectl installed successfully"
else
    echo "✅ kubectl is already installed"
fi

# Check if kind is installed
if ! command -v kind &> /dev/null; then
    echo "📦 Installing kind..."
    curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-linux-amd64
    chmod +x ./kind
    sudo mv ./kind /usr/local/bin/kind
    echo "✅ kind installed successfully"
else
    echo "✅ kind is already installed"
fi

# Create kind cluster
echo "🏗️ Creating Kubernetes cluster..."
if sudo kind get clusters | grep -q "dev-cluster"; then
    echo "⚠️ Cluster 'dev-cluster' already exists"
else
    sudo kind create cluster --name dev-cluster
    echo "✅ Cluster created successfully"
fi

# Configure kubectl
echo "⚙️ Configuring kubectl..."
sudo kind get kubeconfig --name dev-cluster > /tmp/kind-config
KUBECONFIG=~/.kube/config:/tmp/kind-config kubectl config view --merge --flatten > /tmp/merged-config
cp /tmp/merged-config ~/.kube/config
kubectl config use-context kind-dev-cluster

# Verify cluster
echo "🔍 Verifying cluster..."
kubectl cluster-info
kubectl get nodes

echo "🎉 Kubernetes cluster setup completed successfully!"
echo "📝 You can now deploy applications using the deployment scripts."
