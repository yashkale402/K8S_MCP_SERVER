#!/bin/bash

# Cleanup Script
# This script removes all deployed applications and optionally the cluster

set -e

echo "🧹 Starting cleanup process..."

# Kill port forwarding processes
echo "🔌 Stopping port forwarding..."
pkill -f "kubectl port-forward" || true

# Delete applications
echo "🗑️ Removing nginx application..."
kubectl delete namespace nginx --ignore-not-found=true

echo "🗑️ Removing online-shop application..."
kubectl delete namespace online-shop --ignore-not-found=true

# Ask if user wants to delete the cluster
read -p "Do you want to delete the entire cluster? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🗑️ Deleting kind cluster..."
    sudo kind delete cluster --name dev-cluster
    echo "✅ Cluster deleted successfully"
else
    echo "⚠️ Cluster preserved. Applications removed."
fi

# Ask if user wants to remove tools
read -p "Do you want to remove kubectl and kind? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🗑️ Removing tools..."
    sudo rm -f /usr/local/bin/kubectl
    sudo rm -f /usr/local/bin/kind
    echo "✅ Tools removed successfully"
fi

echo "🎉 Cleanup completed!"
