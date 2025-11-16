### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume.yaml`{{exec}}

### Step 2
`kubectl get pods`{{exec}}

### Step 3
`kubectl logs kubernetes-downwardapi-volume-example`{{exec}}

### Step 4
`kubectl exec -it kubernetes-downwardapi-volume-example -- sh`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume-resources.yaml`{{exec}}

### Step 6
`kubectl exec -it kubernetes-downwardapi-volume-example-2 -- sh`{{exec}}