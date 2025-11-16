### Step 1
`kubectl apply -f https://k8s.io/examples/application/basic-daemonset.yaml`{{exec}}

### Step 2
`kubectl get pods -o wide`{{exec}}

### Step 3
`kubectl exec <pod-name> -- cat /var/log/machine-id.log`{{exec}}

### Step 4
`kubectl delete --cascade=foreground --ignore-not-found --now daemonsets/example-daemonset`{{exec}}