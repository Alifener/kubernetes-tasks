### Step 1
`kubectl create namespace quota-mem-cpu-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu.yaml --namespace=quota-mem-cpu-example`{{exec}}

### Step 3
`kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod.yaml --namespace=quota-mem-cpu-example`{{exec}}

### Step 5
`kubectl get pod quota-mem-cpu-demo --namespace=quota-mem-cpu-example`{{exec}}

### Step 6
`kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml`{{exec}}

### Step 7
`kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example -o jsonpath='{ .status.used }' | jq .`{{exec}}

### Step 8
`kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod-2.yaml --namespace=quota-mem-cpu-example`{{exec}}

### Step 9
`kubectl delete namespace quota-mem-cpu-example`{{exec}}