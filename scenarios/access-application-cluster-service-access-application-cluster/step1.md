### Step 1
`kubectl apply -f https://k8s.io/examples/service/access/hello-application.yaml`{{exec}}

### Step 2
`kubectl get deployments hello-world`{{exec}}

### Step 3
`kubectl describe deployments hello-world`{{exec}}

### Step 4
`kubectl get replicasets`{{exec}}

### Step 5
`kubectl describe replicasets`{{exec}}

### Step 6
`kubectl expose deployment hello-world --type=NodePort --name=example-service`{{exec}}

### Step 7
`kubectl describe services example-service`{{exec}}

### Step 8
`kubectl delete services example-service`{{exec}}

### Step 9
`kubectl delete deployment hello-world`{{exec}}