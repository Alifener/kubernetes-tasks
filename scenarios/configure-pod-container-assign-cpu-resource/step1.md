### Step 1
`minikube addons enable metrics-server`{{exec}}

### Step 2
`kubectl get apiservices`{{exec}}

### Step 3
`kubectl create namespace cpu-example`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/pods/resource/cpu-request-limit.yaml --namespace=cpu-example`{{exec}}

### Step 5
`kubectl get pod cpu-demo --namespace=cpu-example`{{exec}}

### Step 6
`kubectl get pod cpu-demo --output=yaml --namespace=cpu-example`{{exec}}