### Step 1
`kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes/minikube" | jq '.'`{{exec}}