### Step 1
`kubectl get pod <pod-name>`{{exec}}

### Step 2
`kubectl describe pod <pod-name>`{{exec}}

### Step 3
`kubectl get pod <pod-name> --template '{{.status.initContainerStatuses}}'`{{exec}}

### Step 4
`kubectl logs <pod-name> -c <init-container-2>`{{exec}}