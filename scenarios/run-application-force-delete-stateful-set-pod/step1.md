### Step 1
`kubectl delete pods <pod>`{{exec}}

### Step 2
`kubectl delete pods <pod> --grace-period=0 --force`{{exec}}

### Step 3
`kubectl delete pods <pod> --grace-period=0`{{exec}}

### Step 4
`kubectl patch pod <pod> -p '{"metadata":{"finalizers":null}}'`{{exec}}