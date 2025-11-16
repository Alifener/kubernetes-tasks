### Step 1
`kubectl create namespace quota-object-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects.yaml --namespace=quota-object-example`{{exec}}

### Step 3
`kubectl get resourcequota object-quota-demo --namespace=quota-object-example --output=yaml`{{exec}}