### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/envars.yaml`{{exec}}

### Step 2
`kubectl get pods -l purpose=demonstrate-envars`{{exec}}

### Step 3
`kubectl exec envar-demo -- printenv`{{exec}}