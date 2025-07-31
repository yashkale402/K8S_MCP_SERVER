#!/bin/bash

# nginx Deployment Script
# This script deploys nginx web server to the Kubernetes cluster

set -e

echo "🚀 Deploying nginx application..."

# Apply nginx manifests
echo "📦 Creating nginx namespace..."
kubectl apply -f manifests/nginx/namespace.yaml

echo "🏗️ Deploying nginx pod..."
kubectl apply -f manifests/nginx/pod.yaml

echo "🌐 Creating nginx services..."
kubectl apply -f manifests/nginx/service-clusterip.yaml
kubectl apply -f manifests/nginx/service-nodeport.yaml

# Wait for pod to be ready
echo "⏳ Waiting for nginx pod to be ready..."
kubectl wait --for=condition=Ready pod/nginx-pod -n nginx --timeout=60s

# Get pod status
echo "📊 nginx deployment status:"
kubectl get pods -n nginx
kubectl get services -n nginx

# Get cluster node IP
NODE_IP=$(sudo docker inspect dev-cluster-control-plane | grep '"IPAddress"' | tail -1 | cut -d'"' -f4)

echo "✅ nginx deployed successfully!"
echo "🌐 Access URLs:"
echo "   - NodePort: http://$NODE_IP:30080"
echo "   - Port Forward: kubectl port-forward -n nginx service/nginx-nodeport 8080:80 --address=0.0.0.0"

# Start port forwarding in background
echo "🔗 Starting port forwarding on port 8080..."
nohup kubectl port-forward -n nginx service/nginx-nodeport 8080:80 --address=0.0.0.0 > /tmp/nginx-port-forward.log 2>&1 &

echo "🎉 nginx is now accessible at http://localhost:8080"
