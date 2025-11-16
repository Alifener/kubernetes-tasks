### Step 1
`kubectl rollout history daemonset <daemonset-name>`{{exec}}

### Step 2
`kubectl rollout history daemonset <daemonset-name> --revision=1`{{exec}}

### Step 3
`kubectl rollout undo daemonset <daemonset-name> --to-revision=<revision>`{{exec}}

### Step 4
`kubectl rollout status ds/<daemonset-name>`{{exec}}

### Step 5
`kubectl get controllerrevision -l <daemonset-selector-key>=<daemonset-selector-value>`{{exec}}