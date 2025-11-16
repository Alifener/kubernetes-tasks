### Step 1
`kubectl get nodes --show-labels`{{exec}}

### Step 2
`kubectl label nodes <your-node-name> disktype=ssd`{{exec}}

### Step 3
`kubectl get nodes --show-labels`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx.yaml`{{exec}}

### Step 5
`kubectl get pods --output=wide`{{exec}}

### Step 6
`kubectl get nodes --show-labels`{{exec}}

### Step 7
`kubectl label nodes <your-node-name> disktype=ssd`{{exec}}

### Step 8
`kubectl get nodes --show-labels`{{exec}}

### Step 9
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx.yaml`{{exec}}

### Step 10
`kubectl get pods --output=wide`{{exec}}