### Step 1
`minikube addons enable metrics-server`{{exec}}

### Step 2
`kubectl apply -f https://k8s.io/examples/application/php-apache.yaml`{{exec}}

### Step 3
`kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10`{{exec}}

### Step 4
`kubectl get hpa`{{exec}}

### Step 5
`kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"`{{exec}}

### Step 6
`kubectl get hpa php-apache --watch`{{exec}}

### Step 7
`kubectl get deployment php-apache`{{exec}}

### Step 8
`kubectl get hpa php-apache --watch`{{exec}}

### Step 9
`kubectl get deployment php-apache`{{exec}}

### Step 10
`kubectl get hpa php-apache -o yaml > /tmp/hpa-v2.yaml`{{exec}}

### Step 11
`kind: Deployment`{{exec}}

### Step 12
`kind: Ingress`{{exec}}

### Step 13
`kind: Deployment`{{exec}}

### Step 14
`kind: Ingress`{{exec}}

### Step 15
`kind: Ingress`{{exec}}