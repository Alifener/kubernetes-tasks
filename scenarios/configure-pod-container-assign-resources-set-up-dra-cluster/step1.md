### Step 1
`kubectl get deviceclasses`{{exec}}

### Step 2
`kubectl get resourceslices`{{exec}}

### Step 3
`kubectl get resourceslice <resourceslice-name> -o yaml`{{exec}}

### Step 4
`kubectl get resourceslice <resourceslice-name> -o yaml`{{exec}}

### Step 5
`kind: ResourceSlice`{{exec}}

### Step 6
`kubectl apply -f https://k8s.io/examples/dra/deviceclass.yaml`{{exec}}