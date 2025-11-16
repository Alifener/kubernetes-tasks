### Step 1
`kubectl apply -f https://k8s.io/examples/debug/node-problem-detector.yaml`{{exec}}

### Step 2
`kubectl create configmap node-problem-detector-config --from-file=config/`{{exec}}

### Step 3
`kubectl delete -f https://k8s.io/examples/debug/node-problem-detector.yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/debug/node-problem-detector-configmap.yaml`{{exec}}