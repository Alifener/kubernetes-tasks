### Step 1
`kubectl debug node/mynode -it --image=ubuntu`{{exec}}

### Step 2
`kubectl delete pod node-debugger-mynode-pdx84 --now`{{exec}}