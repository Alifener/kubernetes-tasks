### Step 1
`kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml`{{exec}}

### Step 2
`kubectl get pods dnsutils`{{exec}}

### Step 3
`kubectl exec -i -t dnsutils -- nslookup kubernetes.default`{{exec}}

### Step 4
`kubectl exec -ti dnsutils -- cat /etc/resolv.conf`{{exec}}

### Step 5
`kubectl exec -i -t dnsutils -- nslookup kubernetes.default`{{exec}}

### Step 6
`kubectl exec -i -t dnsutils -- nslookup kubernetes.default`{{exec}}

### Step 7
`kubectl get pods --namespace=kube-system -l k8s-app=kube-dns`{{exec}}

### Step 8
`kubectl logs --namespace=kube-system -l k8s-app=kube-dns`{{exec}}

### Step 9
`kubectl get svc --namespace=kube-system`{{exec}}

### Step 10
`kubectl get endpointslice -l k8s.io/service-name=kube-dns --namespace=kube-system`{{exec}}

### Step 11
`kubectl -n kube-system edit configmap coredns`{{exec}}