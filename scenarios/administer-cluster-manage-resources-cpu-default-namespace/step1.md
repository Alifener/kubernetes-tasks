### Step 1
`kubectl create namespace default-cpu-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults.yaml --namespace=default-cpu-example`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod.yaml --namespace=default-cpu-example`{{exec}}

### Step 4
`kubectl get pod default-cpu-demo --output=yaml --namespace=default-cpu-example`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-2.yaml --namespace=default-cpu-example`{{exec}}

### Step 6
`kubectl get pod default-cpu-demo-2 --output=yaml --namespace=default-cpu-example`{{exec}}

### Step 7
`kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-3.yaml --namespace=default-cpu-example`{{exec}}

### Step 8
`kubectl get pod default-cpu-demo-3 --output=yaml --namespace=default-cpu-example`{{exec}}

### Step 9
`kubectl delete namespace default-cpu-example`{{exec}}