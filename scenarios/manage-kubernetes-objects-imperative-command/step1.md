### Step 1
`kubectl create service nodeport <myservicename>`{{exec}}

### Step 2
`kubectl create service nodeport -h`{{exec}}

### Step 3
`kubectl delete deployment/nginx`{{exec}}

### Step 4
`kubectl create service clusterip my-svc --clusterip="None" -o yaml --dry-run=client | kubectl set selector --local -f - 'environment=qa' -o yaml | kubectl create -f -`{{exec}}

### Step 5
`kubectl create service clusterip my-svc --clusterip="None" -o yaml --dry-run=client > /tmp/srv.yaml`{{exec}}

### Step 6
`kubectl create --edit -f /tmp/srv.yaml`{{exec}}