### Step 1
`kubectl apply -f https://k8s.io/examples/windows/run-as-username-pod.yaml`{{exec}}

### Step 2
`kubectl get pod run-as-username-pod-demo`{{exec}}

### Step 3
`kubectl exec -it run-as-username-pod-demo -- powershell`{{exec}}