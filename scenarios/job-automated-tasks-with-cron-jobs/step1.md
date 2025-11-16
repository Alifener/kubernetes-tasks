### Step 1
`kubectl create -f https://k8s.io/examples/application/job/cronjob.yaml`{{exec}}

### Step 2
`kubectl get cronjob hello`{{exec}}

### Step 3
`kubectl get jobs --watch`{{exec}}

### Step 4
`kubectl get cronjob hello`{{exec}}

### Step 5
`kubectl logs $pods`{{exec}}

### Step 6
`kubectl delete cronjob hello`{{exec}}