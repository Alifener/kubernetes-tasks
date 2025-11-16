### Step 1
`kubectl create namespace constraints-cpu-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints.yaml --namespace=constraints-cpu-example`{{exec}}

### Step 3
`kubectl get limitrange cpu-min-max-demo-lr --output=yaml --namespace=constraints-cpu-example`{{exec}}