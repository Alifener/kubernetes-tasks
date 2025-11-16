### Step 1
`./easyrsa init-pki`{{exec}}

### Step 2
`./easyrsa --batch "--req-cn=${MASTER_IP}@`date +%s`" build-ca nopass`{{exec}}

### Step 3
`./easyrsa --subject-alt-name="IP:${MASTER_IP},"\`{{exec}}