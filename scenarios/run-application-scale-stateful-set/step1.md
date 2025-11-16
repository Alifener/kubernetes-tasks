### Step 1
`kubectl get statefulsets <stateful-set-name>`{{exec}}

### Step 2
`kubectl scale statefulsets <stateful-set-name> --replicas=<new-replicas>`{{exec}}

### Step 3
`kubectl apply -f <stateful-set-file-updated>`{{exec}}

### Step 4
`kubectl edit statefulsets <stateful-set-name>`{{exec}}

### Step 5
`kubectl patch statefulsets <stateful-set-name> -p '{"spec":{"replicas":<new-replicas>}}'`{{exec}}