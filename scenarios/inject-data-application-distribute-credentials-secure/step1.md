### Step 1
`kubectl apply -f https://k8s.io/examples/pods/inject/secret.yaml`{{exec}}

### Step 2
`kubectl get secret test-secret`{{exec}}

### Step 3
`kubectl describe secret test-secret`{{exec}}

### Step 4
`kubectl create secret generic test-secret --from-literal='username=my-app' --from-literal='password=39528$vdg7Jb'`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/pods/inject/secret-pod.yaml`{{exec}}

### Step 6
`kubectl get pod secret-test-pod`{{exec}}

### Step 7
`kubectl exec -i -t secret-test-pod -- /bin/bash`{{exec}}