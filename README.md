# 🚀 Kubernetes With AI — E-Commerce Project Deployment

This project demonstrates a complete **Kubernetes-based AI-integrated deployment pipeline** for an e-commerce application. The deployment includes all essential Kubernetes objects and services, starting from cluster setup to full-scale project rollout.

## 🧭 Project Workflow Overview

```
Kubernetes Overview ➝ MCP Server ➝ Kubectl Setup ➝ Cluster Setup ➝ Kubernetes Objects ➝ E-Commerce Project Deployment
```

## 📦 Components Breakdown

### 📌 1. Kubernetes Overview
Initial understanding and basics of Kubernetes architecture.

### 📌 2. MCP Server
The **Master Control Plane (MCP) server** is the foundation that hosts the Kubernetes cluster.
* Hosts the control plane components.
* Manages all cluster-level operations.

### 📌 3. Kubectl Setup
CLI tool for communicating with the Kubernetes cluster.

```bash
# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/
kubectl version --client
```

### 📌 4. Cluster Setup
* Creates the Kubernetes cluster using `kind`, `minikube`, or a cloud provider like AWS EKS or Azure AKS.
* Prepares the environment for deployment of Kubernetes objects.

```bash
# Create kind cluster
kind create cluster --name ecommerce-cluster
```

## 📦 Kubernetes Objects Deployed

### 🗂️ Namespaces
Logical separation of environments and applications.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ecommerce
```

### 📦 Pods
Smallest deployable units in Kubernetes running your app containers.

### 🚀 Deployments
Declarative updates for your application pods.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: shop-deployment
  namespace: ecommerce
spec:
  replicas: 3
  selector:
    matchLabels:
      app: shop
  template:
    metadata:
      labels:
        app: shop
    spec:
      containers:
      - name: shop-container
        image: your-shop-image
        ports:
        - containerPort: 80
```

### 🔧 Services
Enable communication inside and outside the cluster.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: shop-service
  namespace: ecommerce
spec:
  selector:
    app: shop
  ports:
  - port: 80
    targetPort: 80
  type: NodePort
```

## 🛍️ E-Commerce Project Deployment
* App components are deployed using Kubernetes manifests.
* Includes web frontend, backend services, and optional AI microservices for personalization or recommendations.

## ✅ Key Features
* 🧠 **AI Integration Ready**
* 📂 Modular Namespace Architecture
* 🔁 Scalable Deployments
* 🌐 NodePort Services for external access
* 📦 Easy-to-maintain manifest structure

## 📁 Project Structure

```
kubernetes-ai-ecommerce/
├── README.md
├── manifests/
│   ├── namespaces/
│   ├── deployments/
│   ├── services/
│   └── ecommerce-app/
└── scripts/
    ├── setup.sh
    └── cleanup.sh
```

## 📌 Useful Commands

```bash
# View all pods in a namespace
kubectl get pods -n ecommerce

# View services
kubectl get svc -n ecommerce

# Describe a pod
kubectl describe pod <pod-name> -n ecommerce

# Access the application via port-forward
kubectl port-forward svc/shop-service 8080:80 -n ecommerce
```

## 🧼 Cleanup

```bash
kubectl delete namespace ecommerce
kind delete cluster --name ecommerce-cluster
```

## 📚 References
* [Kubernetes Docs](https://kubernetes.io/docs/)
* [kubectl Cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
* [kind (Kubernetes in Docker)](https://kind.sigs.k8s.io/)

---

**Created by**: DevOps & AI Integration Team  
**Version**: 1.0  
**Last Updated**: July 31, 2025
