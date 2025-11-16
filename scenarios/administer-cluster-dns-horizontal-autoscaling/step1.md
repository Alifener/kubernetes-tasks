### Step 1
`kubectl get deployment --namespace=kube-system`{{exec}}

### Step 2
`kubectl get deployment -l k8s-app=kube-dns --namespace=kube-system`{{exec}}

### Step 3
`kubectl get deployment --namespace=kube-system`{{exec}}

### Step 4
`kubectl apply -f dns-horizontal-autoscaler.yaml`{{exec}}

### Step 5
`kubectl get configmap --namespace=kube-system`{{exec}}

### Step 6
`kubectl edit configmap kube-dns-autoscaler --namespace=kube-system`{{exec}}