### Step 1
`kubectl apply -f https://k8s.io/examples/application/job/redis/redis-pod.yaml`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/application/job/redis/redis-service.yaml`{{exec}}

### Step 3
`kubectl run -i --tty temp --image redis --command "/bin/sh"`{{exec}}