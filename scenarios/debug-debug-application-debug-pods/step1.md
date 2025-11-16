### Step 1
`kubectl describe pods ${POD_NAME}`{{exec}}

### Step 2
`kubectl get endpointslices -l kubernetes.io/service-name=${SERVICE_NAME}`{{exec}}