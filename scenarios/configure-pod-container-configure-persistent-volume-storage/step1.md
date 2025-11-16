### Step 1
`kubectl apply -f https://k8s.io/examples/pods/storage/pv-volume.yaml`{{exec}}

### Step 2
`kubectl get pv task-pv-volume`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/pods/storage/pv-claim.yaml`{{exec}}

### Step 4
`kubectl get pv task-pv-volume`{{exec}}

### Step 5
`kubectl get pvc task-pv-claim`{{exec}}

### Step 6
`kubectl apply -f https://k8s.io/examples/pods/storage/pv-pod.yaml`{{exec}}

### Step 7
`kubectl get pod task-pv-pod`{{exec}}

### Step 8
`kubectl exec -it task-pv-pod -- /bin/bash`{{exec}}

### Step 9
`kubectl delete pod task-pv-pod`{{exec}}

### Step 10
`kubectl apply -f https://k8s.io/examples/pods/storage/pv-duplicate.yaml`{{exec}}

### Step 11
`kubectl get pod test`{{exec}}

### Step 12
`kubectl exec -it test -- /bin/bash`{{exec}}

### Step 13
`kubectl delete pod test`{{exec}}

### Step 14
`kubectl delete pvc task-pv-claim`{{exec}}

### Step 15
`kubectl delete pv task-pv-volume`{{exec}}