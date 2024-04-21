# Cluster

Kubernetes cluster using minikube.

Deploy your docker images to docker hub: https://hub.docker.com/repositories/blogmates and update the version of the services in the pod files.

Arhitectural proposal: https://www.overleaf.com/1699178441myjbvskkwcbm#84d1c4

## Start the cluster

Make sure you have minikube, docker and python3 installed.

```
python3 scripts/init.py
```

## Create the pods and services

```
python3 scripts/vaporasul.py
```

## Test the conectivity beetwen clusters

We use kubernetes dns and cluster ip for service discovery

Each service gets a DNS record in the format:
```
<service-name>.<namespace>.svc.cluster.local
```

For services in the same namespace the service name of the pod is enough.

Check the service files for more details.

We also deploy three aditional pods for testing the connectivity: test-generic in the default namespace, test-app in the app namespace and test-auth in the auth namespace. We use this to test the conectivity using curl.

Examples:

Check that the pods are running:

```
kubectl get pods --all-namespaces
```
```
kubectl exec -it test-pod -- curl -s http://backend-service.app.svc.cluster.local/sanity

kubectl exec -it test-pod-auth -n auth -- curl -s http://backend-service.app.svc.cluster.local/sanity

kubectl exec -it test-pod-app -n app -- curl -s http:/io-service/sanity
```

All should Should return:
```
Server is up and running
```

## Usefull commands

```
kubectl get pods
kubectl get namespaces
kubectl get pods -n <namespace>
kubectl exec -it <podname> <command>
kubectl apply -f <file>
kubectl port-forward <nume-pod> 8888:5000
kubectl logs <nume-pod>
kubectl exec <nume-pod> -- ls
kubectl cp file.txt <nume-pod>:/file.txt
kubectl delete pods/<nume-pod>
minikube delete
```
