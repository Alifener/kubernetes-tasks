### Step 1
`kubectl apply -f https://k8s.io/examples/application/shell-demo.yaml`{{exec}}

### Step 2
`kubectl get pod shell-demo`{{exec}}

### Step 3
`kubectl exec --stdin --tty shell-demo -- /bin/bash`{{exec}}

### Step 4
`kubectl exec shell-demo -- env`{{exec}}

### Step 5
`kubectl exec shell-demo -- ps aux`{{exec}}

### Step 6
`kubectl exec shell-demo -- ls /`{{exec}}

### Step 7
`kubectl exec shell-demo -- cat /proc/1/mounts`{{exec}}

### Step 8
`kubectl exec -i -t my-pod --container main-app -- /bin/bash`{{exec}}