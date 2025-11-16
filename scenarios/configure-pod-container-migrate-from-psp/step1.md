### Step 1
`kubectl get pods --all-namespaces -o jsonpath="{range .items[?(@.metadata.annotations.kubernetes\.io\/psp=='$PSP_NAME')]}{.metadata.namespace} {.metadata.name}{'\n'}{end}"`{{exec}}

### Step 2
`kubectl get pods -n $NAMESPACE -o jsonpath="{.items[*].metadata.annotations.kubernetes\.io\/psp}" | tr " " "\n" | sort -u`{{exec}}

### Step 3
`kubectl label --dry-run=server --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL`{{exec}}

### Step 4
`kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/audit=$LEVEL`{{exec}}

### Step 5
`kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL`{{exec}}

### Step 6
`kubectl apply -f privileged-psp.yaml`{{exec}}

### Step 7
`kubectl create clusterrole privileged-psp --verb use --resource podsecuritypolicies.policy --resource-name privileged`{{exec}}

### Step 8
`kubectl create -n $NAMESPACE rolebinding disable-psp --clusterrole privileged-psp --group system:serviceaccounts:$NAMESPACE`{{exec}}

### Step 9
`kubectl delete -n $NAMESPACE rolebinding disable-psp`{{exec}}