### Step 1
`kubectl get nodes`{{exec}}

### Step 2
`kubectl drain --ignore-daemonsets <node name>`{{exec}}

### Step 3
`kubectl uncordon <node name>`{{exec}}