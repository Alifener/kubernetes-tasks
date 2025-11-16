### Single line code blocks can be copied by default
`copy me`

### It can also be disabled
`copying disabled`{{}}

### Create a Pod with Busybox  
`kubectl run busybox-pod --image=busybox -- sleep 3600`{{exec}}  

### Verify the Pod is running  
`kubectl get pods`{{exec}}  

### Describe the Pod  
`kubectl describe pod busybox-pod`{{exec}}  

### Open a shell inside the Pod  
`kubectl exec -it busybox-pod -- sh`{{exec}}  

### Exit the shell (if inside)  
`exit`{{exec}}  

### Delete the Pod  
`kubectl delete pod busybox-pod`{{exec}}  
