### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-pod.yaml`{{exec}}

### Step 2
`kubectl get pods`{{exec}}

### Step 3
`kubectl logs dapi-envars-fieldref`{{exec}}

### Step 4
`minikube`{{exec}}

### Step 5
`kubectl exec -it dapi-envars-fieldref -- sh`{{exec}}

### Step 6
`kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-container.yaml`{{exec}}

### Step 7
`kubectl get pods`{{exec}}

### Step 8
`kubectl logs dapi-envars-resourcefieldref`{{exec}}