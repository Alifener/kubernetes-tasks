### Step 1
`minikube addons enable metrics-server`{{exec}}

### Step 2
`kubectl get apiservices`{{exec}}

### Step 3
`kubectl create namespace mem-example`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit.yaml --namespace=mem-example`{{exec}}

### Step 5
`kubectl get pod memory-demo --namespace=mem-example`{{exec}}

### Step 6
`kubectl get pod memory-demo --output=yaml --namespace=mem-example`{{exec}}