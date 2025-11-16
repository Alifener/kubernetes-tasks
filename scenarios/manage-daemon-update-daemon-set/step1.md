### Step 1
`kubectl create -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml`{{exec}}

### Step 3
`kubectl get ds/fluentd-elasticsearch -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system`{{exec}}

### Step 4
`kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml --dry-run=client -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'`{{exec}}

### Step 5
`kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset-update.yaml`{{exec}}

### Step 6
`kubectl edit ds/fluentd-elasticsearch -n kube-system`{{exec}}

### Step 7
`kubectl set image ds/fluentd-elasticsearch fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.6.0 -n kube-system`{{exec}}

### Step 8
`kubectl rollout status ds/fluentd-elasticsearch -n kube-system`{{exec}}

### Step 9
`kubectl get pods -l name=fluentd-elasticsearch -o wide -n kube-system`{{exec}}

### Step 10
`kubectl delete ds fluentd-elasticsearch -n kube-system`{{exec}}