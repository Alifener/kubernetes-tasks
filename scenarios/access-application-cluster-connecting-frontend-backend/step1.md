### Step 1
`kubectl apply -f https://k8s.io/examples/service/access/backend-deployment.yaml`{{exec}}

### Step 2
`kubectl describe deployment backend`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/service/access/backend-service.yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/service/access/frontend-deployment.yaml`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/service/access/frontend-service.yaml`{{exec}}

### Step 6
`kubectl get service frontend --watch`{{exec}}