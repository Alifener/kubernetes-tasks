### Step 1
`kubectl apply -f https://k8s.io/examples/application/deployment.yaml`{{exec}}

### Step 2
`kubectl describe deployment nginx-deployment`{{exec}}

### Step 3
`kubectl get pods -l app=nginx`{{exec}}

### Step 4
`kubectl describe pod <pod-name>`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/application/deployment-update.yaml`{{exec}}

### Step 6
`kubectl get pods -l app=nginx`{{exec}}

### Step 7
`kubectl apply -f https://k8s.io/examples/application/deployment-scale.yaml`{{exec}}

### Step 8
`kubectl get pods -l app=nginx`{{exec}}

### Step 9
`kubectl delete deployment nginx-deployment`{{exec}}