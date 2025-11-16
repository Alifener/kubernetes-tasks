### Step 1
`kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-deployment.yaml`{{exec}}

### Step 2
`kubectl get pods`{{exec}}

### Step 3
`kubectl get deployment`{{exec}}

### Step 4
`kubectl get replicaset`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-service.yaml`{{exec}}

### Step 6
`kubectl get service mongo`{{exec}}

### Step 7
`kubectl get pod mongo-75f59d57f4-4nd6q --template='{{(index (index .spec.containers 0).ports 0).containerPort}}{{"\n"}}'`{{exec}}

### Step 8
`kubectl port-forward mongo-75f59d57f4-4nd6q 28015:27017`{{exec}}

### Step 9
`kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017`{{exec}}

### Step 10
`kubectl port-forward deployment/mongo 28015:27017`{{exec}}

### Step 11
`kubectl port-forward replicaset/mongo-75f59d57f4 28015:27017`{{exec}}

### Step 12
`kubectl port-forward service/mongo 28015:27017`{{exec}}

### Step 13
`kubectl port-forward deployment/mongo :27017`{{exec}}