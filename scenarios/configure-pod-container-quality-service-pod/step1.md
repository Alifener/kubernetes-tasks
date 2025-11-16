### Step 1
`kubectl create namespace qos-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod.yaml --namespace=qos-example`{{exec}}

### Step 3
`kubectl get pod qos-demo --namespace=qos-example --output=yaml`{{exec}}