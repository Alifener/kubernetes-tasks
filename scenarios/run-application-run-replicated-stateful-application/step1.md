### Step 1
`kubectl apply -f https://k8s.io/examples/application/mysql/mysql-configmap.yaml`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/application/mysql/mysql-services.yaml`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/application/mysql/mysql-statefulset.yaml`{{exec}}

### Step 4
`kubectl get pods -l app=mysql --watch`{{exec}}

### Step 5
`kubectl run mysql-client --image=mysql:5.7 -i --rm --restart=Never --\`{{exec}}

### Step 6
`kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\`{{exec}}

### Step 7
`kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\`{{exec}}

### Step 8
`kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql /usr/bin/mysql.off`{{exec}}

### Step 9
`kubectl get pod mysql-2`{{exec}}

### Step 10
`kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql.off /usr/bin/mysql`{{exec}}

### Step 11
`kubectl delete pod mysql-2`{{exec}}

### Step 12
`kubectl get pod mysql-2 -o wide`{{exec}}

### Step 13
`kubectl drain <node-name> --force --delete-emptydir-data --ignore-daemonsets`{{exec}}

### Step 14
`kubectl get pod mysql-2 -o wide --watch`{{exec}}

### Step 15
`kubectl uncordon <node-name>`{{exec}}

### Step 16
`kubectl scale statefulset mysql  --replicas=5`{{exec}}

### Step 17
`kubectl get pods -l app=mysql --watch`{{exec}}

### Step 18
`kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\`{{exec}}

### Step 19
`kubectl scale statefulset mysql --replicas=3`{{exec}}

### Step 20
`kubectl get pvc -l app=mysql`{{exec}}

### Step 21
`kubectl delete pvc data-mysql-3`{{exec}}

### Step 22
`kubectl delete pvc data-mysql-4`{{exec}}

### Step 23
`kubectl delete pod mysql-client-loop --now`{{exec}}

### Step 24
`kubectl delete statefulset mysql`{{exec}}

### Step 25
`kubectl get pods -l app=mysql`{{exec}}

### Step 26
`kubectl delete configmap,service,pvc -l app=mysql`{{exec}}