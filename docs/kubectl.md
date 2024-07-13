- Verbs: get, set, describe
- Output: yaml, json, wide, jsonpath$
- Shortcuts: kubectl api-resources
    - po -> pod
    - svc -> service
    - deploy -> deployment
    - cm -> configmap
    - no -> node
    - ns -> namespace
    - ing -> ingress
    - sa -> serviceaccount
    - pv -> persistentvolume
    - pvc -> persistentvolumeclaim
# Install 

# Alias
```
alias k=kubectl
echo 'alias k=kubectl' >>~/.bashrc
```
# Clusters
```
kubectl cluster-info
kubectl config view
kubectl config current-context
kubectl get componentstatus
```
# Namespaces
```
kubectl create namespace <namespace_name>
kubectl get namespace <namespace_name> 
kubectl describe namespace <namespace_name>
```
# Nodes
```
kubectl get node
kubectl delete node <node_name>
kubectl taint node <node_name>
kubectl drain node <node_name>
kubectl port-forward <pod name> <port number to listen on>:<port number to forward to>
kubectl cordon [node_name] # node maintenance
kubectl uncordon [node_name] # node is schedulable
```
# Pods
```
kubectl get pods
kubectl get pods -n=<namespace_name>
kubectl label pods <pod-name> new-label=awesome # Add a Label
kubectl annotate pods <pod-name> icon=xxx #Add an annotation
kubectl logs <pod-name>
```
# Deployments
```
kubectl get deployment
kubectl describe deployment <deployment_name>
kubectl create deployment <deployment_name>
kubectl scale --replicas=3 deployment nginx
```
# Resources
```
kubectl create -f ./file.yml
kubectl create -f ./dir
kubectl create -f http://www.fpaste.org/279276/48569091/raw/
```
# Services
```
kubectl get svc
kubectl describe svc
```
# Persistent Volumes
```
kubectl get pv
kubectl describe pv
kubectl get pvc
kubectl describe pvc
```
# Configmaps