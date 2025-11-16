### Step 1
`minikube version`{{exec}}

### Step 2
`minikube version: v1.5.2`{{exec}}

### Step 3
`minikube start --network-plugin=cni`{{exec}}

### Step 4
`kubectl get pods --namespace=kube-system -l k8s-app=cilium`{{exec}}