### Step 1
`kubectl apply -f https://k8s.io/examples/debug/termination.yaml`{{exec}}

### Step 2
`kubectl get pod termination-demo`{{exec}}

### Step 3
`kubectl get pod termination-demo --output=yaml`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/debug/termination.yaml`{{exec}}

### Step 5
`kubectl get pod termination-demo`{{exec}}

### Step 6
`kubectl get pod termination-demo --output=yaml`{{exec}}

### Step 7
`kind: Pod`{{exec}}

### Step 8
`kubectl get pod termination-demo -o go-template="{{range .status.containerStatuses}}{{.lastState.terminated.message}}{{end}}"`{{exec}}