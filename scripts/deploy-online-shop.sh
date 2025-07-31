#!/bin/bash

# Online Shop Deployment Script
# This script deploys the online shop application to the Kubernetes cluster

set -e

echo "🚀 Deploying online shop application..."

# Apply online-shop manifests
echo "📦 Creating online-shop namespace..."
kubectl apply -f manifests/online-shop/namespace.yaml

echo "🏗️ Deploying online-shop application..."
kubectl apply -f manifests/online-shop/deployment.yaml

echo "🌐 Creating online-shop services..."
kubectl apply -f manifests/online-shop/service-clusterip.yaml
kubectl apply -f manifests/online-shop/service-nodeport.yaml

# Wait for deployment to be ready
echo "⏳ Waiting for online-shop deployment to be ready..."
kubectl wait --for=condition=Available deployment/online-shop-app -n online-shop --timeout=120s

# Get deployment status
echo "📊 Online shop deployment status:"
kubectl get pods -n online-shop
kubectl get services -n online-shop
kubectl get deployment -n online-shop

# Get cluster node IP
NODE_IP=$(sudo docker inspect dev-cluster-control-plane | grep '"IPAddress"' | tail -1 | cut -d'"' -f4)

echo "✅ Online shop deployed successfully!"
echo "🌐 Access URLs:"
echo "   - NodePort: http://$NODE_IP:30090"
echo "   - Port Forward: kubectl port-forward -n online-shop service/online-shop-service 8090:80 --address=0.0.0.0"

# Start port forwarding in background
echo "🔗 Starting port forwarding on port 8090..."
nohup kubectl port-forward -n online-shop service/online-shop-service 8090:80 --address=0.0.0.0 > /tmp/online-shop-port-forward.log 2>&1 &

echo "🎉 Online shop is now accessible at http://localhost:8090"
