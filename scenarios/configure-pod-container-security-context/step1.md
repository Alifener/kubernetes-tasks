### Step 1
`kubectl apply -f https://k8s.io/examples/pods/security/security-context.yaml`{{exec}}

### Step 2
`kubectl get pod security-context-demo`{{exec}}

### Step 3
`kubectl exec -it security-context-demo -- sh`{{exec}}