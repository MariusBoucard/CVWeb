#!/bin/bash

# Stop and delete the Minikube cluster
echo "Stopping and deleting Minikube..."
minikube stop
minikube delete

# Start Minikube
echo "Starting Minikube..."
minikube start

# Build Docker images for cv-front and cv-backend
echo "Building Docker images..."
docker build --build-arg VITE_APP_BACKEND_URL=http://cv-backend.default.svc.cluster.local -t cv-front:latest ./cv-frontend/
docker build -t cv-backend:latest ./cv-backend/

# Load the images into Minikube
echo "Loading images into Minikube..."
minikube image load cv-front:latest
minikube image load cv-backend:latest
kubectl create namespace web
# Apply Kubernetes configuration
echo "Applying Kubernetes configuration..."
kubectl apply -f k8sConfig.yaml
kubectl apply -f nginx.yaml

# Wait for pods to be ready
echo "Waiting for pods to be ready..."
kubectl get pods --watch & sleep 10
kill $! # Stop watching after 10 seconds

# Get Minikube IP and service details
echo "Fetching Minikube IP and service details..."
minikube ip
kubectl get service cv-front

# WE SHOULD RESTART THE NGINX AS WELL AND THEN REDIRECT WITH OUR LOCAL NGINX TO IT !

echo "Reload complete!"