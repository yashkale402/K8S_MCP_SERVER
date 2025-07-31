# 🚀 Quick Start Guide

This guide will get you up and running with the Kubernetes development environment in just a few minutes.

## ⚡ One-Command Setup

```bash
# Setup entire cluster and deploy both applications
./scripts/setup-cluster.sh && ./scripts/deploy-nginx.sh && ./scripts/deploy-online-shop.sh
```

## 📋 Step-by-Step Setup

### 1. Setup Kubernetes Cluster
```bash
./scripts/setup-cluster.sh
```

### 2. Deploy nginx Application
```bash
./scripts/deploy-nginx.sh
```

### 3. Deploy Online Shop Application
```bash
./scripts/deploy-online-shop.sh
```

## 🌐 Access Your Applications

After deployment, your applications will be available at:

- **nginx**: http://localhost:8080
- **Online Shop**: http://localhost:8090

## 📊 Check Status

```bash
# Check all pods
kubectl get pods --all-namespaces

# Check services
kubectl get services --all-namespaces

# Check deployments
kubectl get deployments --all-namespaces
```

## 🧹 Cleanup

```bash
# Remove everything
./scripts/cleanup.sh
```

## 🔧 Manual Commands

If you prefer manual deployment:

```bash
# Apply all nginx manifests
kubectl apply -f manifests/nginx/

# Apply all online-shop manifests
kubectl apply -f manifests/online-shop/

# Port forwarding
kubectl port-forward -n nginx service/nginx-nodeport 8080:80 --address=0.0.0.0 &
kubectl port-forward -n online-shop service/online-shop-service 8090:80 --address=0.0.0.0 &
```

## 🆘 Troubleshooting

### Check Pod Logs
```bash
kubectl logs -n nginx nginx-pod
kubectl logs -n online-shop -l app=online-shop-app
```

### Check Pod Status
```bash
kubectl describe pod -n nginx nginx-pod
kubectl describe pod -n online-shop -l app=online-shop-app
```

### Restart Port Forwarding
```bash
pkill -f "kubectl port-forward"
./scripts/deploy-nginx.sh
./scripts/deploy-online-shop.sh
```

---

**🎉 That's it! Your Kubernetes development environment is ready!**
