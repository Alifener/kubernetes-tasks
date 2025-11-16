### Step 1
`helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/`{{exec}}

### Step 2
`helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard`{{exec}}

### Step 3
`kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443`{{exec}}