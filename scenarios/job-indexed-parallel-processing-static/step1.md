### Step 1
`kubectl apply -f https://kubernetes.io/examples/application/job/indexed-job.yaml`{{exec}}

### Step 2
`kubectl wait --for=condition=complete --timeout=300s job/indexed-job`{{exec}}

### Step 3
`kubectl describe jobs/indexed-job`{{exec}}

### Step 4
`kubectl logs indexed-job-fdhq5 # Change this to match the name of a Pod from that Job`{{exec}}