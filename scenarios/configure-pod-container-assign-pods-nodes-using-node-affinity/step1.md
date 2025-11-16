### Step 1
`kubectl get nodes --show-labels`{{exec}}

### Step 2
`kubectl label nodes <your-node-name> disktype=ssd`{{exec}}

### Step 3
`kubectl get nodes --show-labels`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml`{{exec}}

### Step 5
`kubectl get pods --output=wide`{{exec}}

### Step 6
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx-preferred-affinity.yaml`{{exec}}

### Step 7
`kubectl get pods --output=wide`{{exec}}

### Step 8
`kubectl get nodes --show-labels`{{exec}}

### Step 9
`kubectl label nodes <your-node-name> disktype=ssd`{{exec}}

### Step 10
`kubectl get nodes --show-labels`{{exec}}

### Step 11
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml`{{exec}}

### Step 12
`kubectl get pods --output=wide`{{exec}}

### Step 13
`kubectl apply -f https://k8s.io/examples/pods/pod-nginx-preferred-affinity.yaml`{{exec}}

### Step 14
`kubectl get pods --output=wide`{{exec}}