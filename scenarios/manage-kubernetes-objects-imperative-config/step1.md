### Step 1
`kubectl delete <type> <name>`{{exec}}

### Step 2
`kubectl delete <type> -l <label>`{{exec}}

### Step 3
`kubectl create -f <url> --edit`{{exec}}

### Step 4
`kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml`{{exec}}

### Step 5
`kubectl replace -f <kind>_<name>.yaml`{{exec}}

### Step 6
`kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml`{{exec}}

### Step 7
`kubectl replace -f <kind>_<name>.yaml`{{exec}}