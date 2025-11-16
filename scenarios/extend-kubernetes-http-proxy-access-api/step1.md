### Step 1
`kubectl create deployment hello-app --image=gcr.io/google-samples/hello-app:2.0 --port=8080`{{exec}}

### Step 2
`kubectl proxy --port=8080`{{exec}}