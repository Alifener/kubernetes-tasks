### Step 1
`kind: CertificateSigningRequest`{{exec}}

### Step 2
`kubectl get csr`{{exec}}

### Step 3
`kubectl certificate approve myuser`{{exec}}

### Step 4
`kubectl get csr/myuser -o yaml`{{exec}}

### Step 5
`kubectl get csr myuser -o jsonpath='{.status.certificate}'| base64 -d > myuser.crt`{{exec}}

### Step 6
`kubectl config set-credentials myuser --client-key=myuser.key --client-certificate=myuser.crt --embed-certs=true`{{exec}}

### Step 7
`kubectl config set-context myuser --cluster=kubernetes --user=myuser`{{exec}}

### Step 8
`kubectl --context myuser auth whoami`{{exec}}

### Step 9
`kubectl create role developer --verb=create --verb=get --verb=list --verb=update --verb=delete --resource=pods`{{exec}}

### Step 10
`kubectl create rolebinding developer-binding-myuser --role=developer --user=myuser`{{exec}}