### Step 1
`kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-failjob.yaml`{{exec}}

### Step 2
`kubectl get jobs -l job-name=job-pod-failure-policy-failjob -o yaml`{{exec}}

### Step 3
`kubectl delete jobs/job-pod-failure-policy-failjob`{{exec}}

### Step 4
`kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-ignore.yaml`{{exec}}

### Step 5
`kubectl drain nodes/$nodeName --ignore-daemonsets --grace-period=0`{{exec}}

### Step 6
`kubectl get jobs -l job-name=job-pod-failure-policy-ignore -o yaml`{{exec}}

### Step 7
`kubectl uncordon nodes/$nodeName`{{exec}}

### Step 8
`kubectl delete jobs/job-pod-failure-policy-ignore`{{exec}}

### Step 9
`kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-config-issue.yaml`{{exec}}

### Step 10
`kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o yaml`{{exec}}