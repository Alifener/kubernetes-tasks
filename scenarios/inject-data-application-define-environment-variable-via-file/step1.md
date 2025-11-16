### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/envars-file-container.yaml`{{exec}}

### Step 2
`kubectl get pods`{{exec}}

### Step 3
`kubectl logs dapi-test-pod -c use-envfile | grep DB_ADDRESS`{{exec}}