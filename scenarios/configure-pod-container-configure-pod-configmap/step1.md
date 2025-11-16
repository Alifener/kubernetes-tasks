### Step 1
`kubectl create configmap <map-name> <data-source>`{{exec}}

### Step 2
`kubectl create configmap game-config --from-file=configure-pod-container/configmap/`{{exec}}

### Step 3
`kubectl describe configmaps game-config`{{exec}}

### Step 4
`kubectl get configmaps game-config -o yaml`{{exec}}