### Step 1
`kubectl create secret generic db-user-pass \`{{exec}}

### Step 2
`kubectl create secret generic db-user-pass \`{{exec}}

### Step 3
`kubectl create secret generic db-user-pass \`{{exec}}

### Step 4
`kubectl get secrets`{{exec}}

### Step 5
`kubectl describe secret db-user-pass`{{exec}}

### Step 6
`kubectl get secret db-user-pass -o jsonpath='{.data}'`{{exec}}