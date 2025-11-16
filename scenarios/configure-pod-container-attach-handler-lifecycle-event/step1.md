### Step 1
`kubectl apply -f https://k8s.io/examples/pods/lifecycle-events.yaml`{{exec}}

### Step 2
`kubectl get pod lifecycle-demo`{{exec}}

### Step 3
`kubectl exec -it lifecycle-demo -- /bin/bash`{{exec}}