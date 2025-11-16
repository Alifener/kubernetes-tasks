### Step 1
`kubectl get storageclass`{{exec}}

### Step 2
`kubectl patch storageclass standard -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'`{{exec}}

### Step 3
`kubectl patch storageclass gold -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'`{{exec}}

### Step 4
`kubectl get storageclass`{{exec}}