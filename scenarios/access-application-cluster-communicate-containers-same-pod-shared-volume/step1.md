### Step 1
`kubectl apply -f https://k8s.io/examples/pods/two-container-pod.yaml`{{exec}}

### Step 2
`kubectl get pod two-containers --output=yaml`{{exec}}

### Step 3
`kind: Pod`{{exec}}

### Step 4
`kubectl exec -it two-containers -c nginx-container -- /bin/bash`{{exec}}