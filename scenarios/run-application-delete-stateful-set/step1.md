### Step 1
`kubectl delete -f <file.yaml>`{{exec}}

### Step 2
`kubectl delete statefulsets <statefulset-name>`{{exec}}

### Step 3
`kubectl delete service <service-name>`{{exec}}

### Step 4
`kubectl delete -f <file.yaml> --cascade=orphan`{{exec}}

### Step 5
`kubectl delete pods -l app.kubernetes.io/name=MyApp`{{exec}}

### Step 6
`kubectl delete statefulset -l app.kubernetes.io/name=MyApp`{{exec}}

### Step 7
`kubectl delete pvc -l app.kubernetes.io/name=MyApp`{{exec}}