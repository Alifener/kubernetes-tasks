### Step 1
`kubectl apply -f https://k8s.io/examples/pods/init-containers.yaml`{{exec}}

### Step 2
`kubectl get pod init-demo`{{exec}}

### Step 3
`kubectl exec -it init-demo -- /bin/bash`{{exec}}