### Step 1
`kubectl create secret generic user --from-file=./username.txt`{{exec}}

### Step 2
`kubectl create secret generic pass --from-file=./password.txt`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/pods/storage/projected.yaml`{{exec}}

### Step 4
`kubectl get --watch pod test-projected-volume`{{exec}}

### Step 5
`kubectl exec -it test-projected-volume -- /bin/sh`{{exec}}

### Step 6
`kubectl delete pod test-projected-volume`{{exec}}

### Step 7
`kubectl delete secret user pass`{{exec}}

### Step 8
`kubectl create secret generic user --from-file=./username.txt`{{exec}}

### Step 9
`kubectl create secret generic pass --from-file=./password.txt`{{exec}}

### Step 10
`kubectl apply -f https://k8s.io/examples/pods/storage/projected.yaml`{{exec}}

### Step 11
`kubectl get --watch pod test-projected-volume`{{exec}}

### Step 12
`kubectl exec -it test-projected-volume -- /bin/sh`{{exec}}