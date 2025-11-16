### Step 1
`kubectl create namespace quota-pod-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/quota-pod.yaml --namespace=quota-pod-example`{{exec}}

### Step 3
`kubectl get resourcequota pod-demo --namespace=quota-pod-example --output=yaml`{{exec}}