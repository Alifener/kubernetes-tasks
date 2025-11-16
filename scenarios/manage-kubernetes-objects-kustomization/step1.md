### Step 1
`kubectl kustomize <kustomization_directory>`{{exec}}

### Step 2
`kubectl apply -k <kustomization_directory>`{{exec}}

### Step 3
`kubectl kustomize ./`{{exec}}

### Step 4
`kind: Deployment`{{exec}}

### Step 5
`kind: Service`{{exec}}

### Step 6
`kind: Deployment`{{exec}}