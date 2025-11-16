### Step 1
`kubectl edit cm -n kube-system kubeadm-config`{{exec}}

### Step 2
`kubectl edit cm -n kube-system kubelet-config`{{exec}}

### Step 3
`kubectl edit cm -n kube-system kube-proxy`{{exec}}

### Step 4
`kubectl delete po -n kube-system -l k8s-app=kube-proxy`{{exec}}

### Step 5
`kubectl edit deployment -n kube-system coredns`{{exec}}

### Step 6
`kubectl edit service -n kube-system kube-dns`{{exec}}

### Step 7
`kubectl rollout restart deployment -n kube-system coredns`{{exec}}

### Step 8
`kubectl edit no <node-name>`{{exec}}

### Step 9
`kubectl patch no <node-name> --patch-file <patch-file>`{{exec}}