### Step 1
`kubectl get deviceclasses`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml`{{exec}}

### Step 3
`kubectl apply -f https://k8s.io/examples/dra/resourceclaim.yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/dra/dra-example-job.yaml`{{exec}}

### Step 5
`kubectl delete -f https://k8s.io/examples/dra/dra-example-job.yaml`{{exec}}

### Step 6
`kubectl delete -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml`{{exec}}

### Step 7
`kubectl delete -f https://k8s.io/examples/dra/resourceclaim.yaml`{{exec}}

### Step 8
`kubectl delete -f https://k8s.io/examples/dra/dra-example-job.yaml`{{exec}}

### Step 9
`kubectl delete -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml`{{exec}}

### Step 10
`kubectl delete -f https://k8s.io/examples/dra/resourceclaim.yaml`{{exec}}