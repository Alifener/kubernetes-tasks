### Step 1
`kubectl patch deployment -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';`{{exec}}

### Step 2
`kubectl patch daemonset -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';`{{exec}}

### Step 3
`kubectl get cm/cluster-info --namespace kube-public -o yaml | \`{{exec}}

### Step 4
`kubectl apply -f -`{{exec}}

### Step 5
`kubectl patch deployment -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';`{{exec}}

### Step 6
`kubectl patch daemonset -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';`{{exec}}

### Step 7
`kubectl apply -f -`{{exec}}