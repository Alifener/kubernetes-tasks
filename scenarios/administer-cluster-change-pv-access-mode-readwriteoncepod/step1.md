### Step 1
`kubectl get pvc cat-pictures-pvc -o jsonpath='{.spec.volumeName}'`{{exec}}