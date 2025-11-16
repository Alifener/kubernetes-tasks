### Step 1
`kubectl get servicecidr`{{exec}}

### Step 2
`kubectl get service kubernetes`{{exec}}

### Step 3
`kubectl get ipaddress 10.96.0.1`{{exec}}

### Step 4
`kind: ServiceCIDR`{{exec}}

### Step 5
`kubectl delete servicecidr newcidr1`{{exec}}

### Step 6
`kubectl get servicecidr newcidr1 -o yaml`{{exec}}