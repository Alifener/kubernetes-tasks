### Step 1
`kubectl create namespace constraints-mem-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints.yaml --namespace=constraints-mem-example`{{exec}}

### Step 3
`kubectl get limitrange mem-min-max-demo-lr --namespace=constraints-mem-example --output=yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod.yaml --namespace=constraints-mem-example`{{exec}}

### Step 5
`kubectl get pod constraints-mem-demo --namespace=constraints-mem-example`{{exec}}

### Step 6
`kubectl get pod constraints-mem-demo --output=yaml --namespace=constraints-mem-example`{{exec}}