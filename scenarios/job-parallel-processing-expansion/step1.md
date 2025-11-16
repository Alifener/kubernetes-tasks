### Step 1
`kubectl create -f ./jobs`{{exec}}

### Step 2
`kubectl get jobs -l jobgroup=jobexample`{{exec}}

### Step 3
`kubectl get pods -l jobgroup=jobexample`{{exec}}

### Step 4
`kubectl logs -f -l jobgroup=jobexample`{{exec}}

### Step 5
`kubectl delete job -l jobgroup=jobexample`{{exec}}