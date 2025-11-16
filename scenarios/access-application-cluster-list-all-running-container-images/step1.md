### Step 1
`kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec['initContainers', 'containers'][*].image}" |\`{{exec}}

### Step 2
`kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\`{{exec}}

### Step 3
`kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" -l app=nginx`{{exec}}

### Step 4
`kubectl get pods --namespace kube-system -o jsonpath="{.items[*].spec.containers[*].image}"`{{exec}}

### Step 5
`kubectl get pods --all-namespaces -o go-template --template="{{range .items}}{{range .spec.containers}}{{.image}} {{end}}{{end}}"`{{exec}}