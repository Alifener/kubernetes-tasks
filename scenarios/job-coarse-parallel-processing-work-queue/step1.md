### Step 1
`kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-service.yaml`{{exec}}

### Step 2
`kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-statefulset.yaml`{{exec}}

### Step 3
`kubectl run -i --tty temp --image ubuntu:22.04`{{exec}}

### Step 4
`docker build -t job-wq-1 .`{{exec}}

### Step 5
`docker tag job-wq-1 <username>/job-wq-1`{{exec}}

### Step 6
`docker push <username>/job-wq-1`{{exec}}

### Step 7
`kubectl apply -f ./job.yaml`{{exec}}

### Step 8
`kubectl wait --for=condition=complete --timeout=300s job/job-wq-1`{{exec}}

### Step 9
`kubectl describe jobs/job-wq-1`{{exec}}