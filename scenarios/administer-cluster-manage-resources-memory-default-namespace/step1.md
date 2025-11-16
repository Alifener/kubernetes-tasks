### Step 1
`kubectl create namespace default-mem-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults.yaml --namespace=default-mem-example`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod.yaml --namespace=default-mem-example`{{exec}}

### Step 4
`kubectl get pod default-mem-demo --output=yaml --namespace=default-mem-example`{{exec}}

### Step 5
`kubectl delete pod default-mem-demo --namespace=default-mem-example`{{exec}}

### Step 6
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-2.yaml --namespace=default-mem-example`{{exec}}

### Step 7
`kubectl get pod default-mem-demo-2 --output=yaml --namespace=default-mem-example`{{exec}}

### Step 8
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-3.yaml --namespace=default-mem-example`{{exec}}

### Step 9
`kubectl get pod default-mem-demo-3 --output=yaml --namespace=default-mem-example`{{exec}}

### Step 10
`kubectl delete namespace default-mem-example`{{exec}}