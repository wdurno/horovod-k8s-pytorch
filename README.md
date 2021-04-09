# horovod-k8s-pytorch

Demonstrates application of `horovod[pytorch]` in a Kubernetes environment.

Usage:
```
## build
python3 cli.py 
## distributed model fitting example 
kubectl exec -it horovod-0 -- horovodrun -np 3 -H horovod-0:1,horovod-1:1,horovod-2:1 python3 /app/src/python/ai/tensorflow_mnist.py 
```
