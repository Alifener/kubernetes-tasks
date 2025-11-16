### Step 1
`kubectl create namespace pod-resources-example`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-memory-request-limit.yaml --namespace=pod-resources-example`{{exec}}

### Step 3
`kubectl get pod memory-demo --namespace=pod-resources-example`{{exec}}

### Step 4
`kubectl get pod memory-demo --output=yaml --namespace=pod-resources-example`{{exec}}