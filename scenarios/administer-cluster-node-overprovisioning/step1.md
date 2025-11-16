### Step 1
`kubectl apply -f https://k8s.io/examples/priorityclass/low-priority-class.yaml`{{exec}}

### Step 2
`kubectl --namespace example apply -f https://k8s.io/examples/deployments/deployment-with-capacity-reservation.yaml`{{exec}}

### Step 3
`kubectl edit deployment capacity-reservation`{{exec}}