### Step 1
`kubectl apply -f https://k8s.io/examples/pods/share-process-namespace.yaml`{{exec}}

### Step 2
`kubectl exec -it nginx -c shell -- /bin/sh`{{exec}}