### Step 1
`kubectl run nginx --image nginx`{{exec}}

### Step 2
`kubectl get pods --output=wide`{{exec}}

### Step 3
`kubectl exec nginx -- cat /etc/hosts`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/service/networking/hostaliases-pod.yaml`{{exec}}

### Step 5
`kubectl get pod --output=wide`{{exec}}

### Step 6
`kubectl logs hostaliases-pod`{{exec}}