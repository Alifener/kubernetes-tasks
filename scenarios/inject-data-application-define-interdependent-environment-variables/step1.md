### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/dependent-envars.yaml`{{exec}}

### Step 2
`kubectl get pods dependent-envars-demo`{{exec}}

### Step 3
`kubectl logs pod/dependent-envars-demo`{{exec}}