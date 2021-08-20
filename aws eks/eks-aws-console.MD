# Create a EKS Cluster using AWS Console

### 1. Create an IAM Role
 Create an IAM Role for EKS Cluster using cloud formation template - eksClusterRole 
 
### 2. Create your Amazon EKS cluster VPC
 Create VPC using cloud formation template - amazon-eks-vpc-sample.yaml
	
 Go to Outputs once VPC is created and notedown VPC, Security group etc.
		

### 3. Create your Amazon EKS cluster

 Create an EKS Cluster from AWS Console, select appropriate VPC, Security group etc. 
 
 When your cluster provisioning is complete (usually between 10 and 15 minutes), note the API server endpoint and Certificate authority values. These are used in your kubectl configuration.

### 4. Make sure aws cli is installed and setup in your local computer

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

### 5. Make sure kubectl is installed in your local computer

https://kubernetes.io/docs/tasks/tools/

### 6. Create a kubeconfig file

```sh
aws eks --region <us-west-2> update-kubeconfig --name <cluster_name>
kubectl get svc
```


### 7. Create your Amazon EKS node role for Compute nodes
In Order to create compute, we will first create a role for the compute nodes using cloud formation and then we will use that role for compute nodes.
amazon-eks-nodegroup-role.yaml

### 8. Create compute
 Create Node group and provide appropriate parameters

 
### 9. Deploy a sample Linux workload

```sh
kubectl create namespace <my-namespace>
```
Then create a sample deployment file - sample-service.yaml and apply the deployment - 
```
	kubectl apply -f sample-service.yaml
```

### 10. View all resources that exist in the my-namespace namespace.

```sh
kubectl get all -n my-namespace
```

### 11. View the details of the deployed service
```sh
kubectl -n <my-namespace> describe service <my-service>
```

### 12. View the details of one of the pods that was deployed

```sh
kubectl -n <my-namespace> describe pod <my-deployment-776d8f8fd8-78w66>
```

### 13. Execute a shell on one of the pods by replacing the <value> below with a value returned for one of your pods
```sh
kubectl exec -it <my-deployment-776d8f8fd8-78w66> -n <my-namespace> -- /bin/bash
```

### 14. Remove the sample service, deployment, pods, and namespace
```sh
kubectl delete namespace <my-namespace>	
```
