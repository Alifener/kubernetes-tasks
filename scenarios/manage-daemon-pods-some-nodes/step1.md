### Step 1
`kubectl label nodes example-node-1 example-node-2 ssd=true`{{exec}}

### Step 2
`kubectl label nodes example-node-3 ssd=true`{{exec}}

### Step 3
`kubectl get pods -o wide`{{exec}}