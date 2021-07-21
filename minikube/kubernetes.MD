# Getting Started with Kubernetes


```sh
minikube start
```

```sh
kubectl get pods
```

```sh
kubectl get deployments
```

```sh
minikube dashboard
```

```sh
kubectl create -f deployment.yml
```

```sh
kubectl scale --replicas=3 deployment nginx-deployment
```

```sh
minikube addons enable dashboard
```

```sh
kubectl apply -f /opt/kubernetes-dashboard.yaml
```

```sh
kubectl get pods -n kubernetes-dashboard -w
```

```sh
kubectl convert -f deployment.yml
```

```sh
kubectl convert -f . | kubectl create -f -
```

```sh
kubectl get pods
```

```sh
kubectl get deployments
```

```sh
minikube ip
```

```sh
minikube stop
```


