### Step 1
`kubectl apply -f https://k8s.io/examples/application/mysql/mysql-pv.yaml`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/application/mysql/mysql-deployment.yaml`{{exec}}

### Step 3
`kubectl describe deployment mysql`{{exec}}

### Step 4
`kubectl get pods -l app=mysql`{{exec}}

### Step 5
`kubectl describe pvc mysql-pv-claim`{{exec}}

### Step 6
`kubectl run -it --rm --image=mysql:9 --restart=Never mysql-client -- mysql -h mysql -ppassword`{{exec}}

### Step 7
`kubectl delete deployment,svc mysql`{{exec}}

### Step 8
`kubectl delete pvc mysql-pv-claim`{{exec}}

### Step 9
`kubectl delete pv mysql-pv-volume`{{exec}}