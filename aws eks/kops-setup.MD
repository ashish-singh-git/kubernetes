# Installing Kubernetes on AWS using Kops

### 1. Launch Linux EC2 instance in AWS, we will use this EC2 instance to launch
 our Kubernetes cluster by installing Kops on it. I will launch this instance in 
  Ohio region but you can pick any region of your choice
 
### 2. Create and attach IAM role to EC2 Instance.
	Kops would need permissions following permissions in order to operate:
		S3
		EC2
		VPC
		Route53
		Autoscaling
		etc..
		
	Create a Role for the above specified permissions and then attach it to the running EC2 instance

### 3. Install Kops
```sh
curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x kops-linux-amd64
sudo mv kops-linux-amd64 /usr/local/bin/kops
```

### 4. Install kubectl
```sh
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
### 5. Create S3 bucket in AWS
S3 bucket is used by kubernetes to persist cluster state and so, create any S3 bucket of your choice

bucket_name

### 6. Create private hosted zone in AWS Route53
 1. Head over to aws Route53 and create a private hosted zone
 2. Choose a name of your choice - kubernetes.kops.com
 3. Choose type as private hosted zone for VPC
 4. Select default vpc in the region you are setting up your cluster

 
### 7 Configure environment variables.
Open .bashrc file 
```
	vi ~/.bashrc
```
Add following content into .bashrc, you can choose any arbitary name for cluster and make sure buck name matches the one you created in previous step.

```sh
export KOPS_CLUSTER_NAME=kubernetes.kops.com
export KOPS_STATE_STORE=s3://bucket_name
```
Then running command to reflect variables added to .bashrc
```
	source ~/.bashrc
```
### 8. Create ssh key pair
This keypair is used for ssh into kubernetes cluster

```sh
ssh-keygen
```

### 9. Create a Kubernetes cluster definition.
```sh
kops create cluster \
--state=${KOPS_STATE_STORE} \
--node-count=2 \
--master-size=t2.micro \
--node-size=t2.micro \
--zones=us-west-2a,us-west-2b \
--name=${KOPS_CLUSTER_NAME} \
--dns private \
--master-count 1
```

### 10. Create kubernetes cluster

```sh
kops update cluster --yes
```
Above command may take some time to create the required infrastructure resources on AWS. Execute the validate command to check its status and wait until the cluster becomes ready

```sh
kops validate cluster
```
For the above above command, you might see validation failed error initially when you create cluster and it is expected behaviour, you have to wait for some more time and check again.

### 11. To connect to the master
```sh
ssh admin@api.kubernetes.kops.com
kubectl get nodes
```

### 12. Running a container (simple version)
From this point onwards, it is assumed that kubectl is on your path from one of the getting started guides.

The kubectl create line below will create a deployment named my-nginx to ensure that there are always a nginx pod running.

```sh
kubectl create deployment --image nginx my-nginx	
```

You can list the pods to see what is up and running:

```sh
kubectl get pods
```

You can also see the deployment that was created:
```sh
kubectl get deployment
```

You can also scale the deployment to ensure there is two nginx pods running:
```sh
kubectl scale deployment --replicas 2 my-nginx
```

You can now list the pods to see there is two up and running:

```sh
kubectl get pods
```

Exposing your pods to the internet

On some platforms (for example Google Compute Engine) the kubectl command can integrate with your cloud provider to add a public IP address for the pods, to do this run:

```sh
kubectl expose deployment my-nginx --port=80 --type=LoadBalancer
```

sudo apt install xdg-utils
sudo apt install chromium-browser
xdg-settings set default-web-browser chromium-browser-chromium.desktop

This should print the service that has been created, and map an external IP address to the service. Where to find this external IP address will depend on the environment you run in. For instance, for Google Compute Engine the external IP address is listed as part of the newly created service and can be retrieved by running

```sh
kubectl get services
```

In order to access your nginx landing page, you also have to make sure that traffic from external IPs is allowed. Do this by opening a firewall to allow traffic on port 80.

Cleanup

To delete the two replicated containers, delete the deployment:

```sh
kubectl delete deployment my-nginx
```

# Destroy the kubernetes cluster
```sh
kops delete cluster  --yes
```
