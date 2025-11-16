### Step 1
`kubectl drain <node-to-drain> --ignore-daemonsets`{{exec}}

### Step 2
`kubectl uncordon <node-to-uncordon>`{{exec}}