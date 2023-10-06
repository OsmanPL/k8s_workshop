# k8s_workshop

## Comandos de Kubernetes

### Obtener namespace
- `kubectl get ns`

### Crear namespace
- `kubectl create ns <nombre_namespace>`

### Crear cualquier objeto de k8s
- `kubectl apply -f <ruta_archivo> -n <nombre_namespace>`

### Eliminar cualquier objeto de k8s
- `kubectl delete -f <ruta_archivo> -n <nombre_namespace>`

### Editar cualquier objeto de k8s
- `kubectl edit <tipo_objeto> <nombre_objeto> -n <nombre_namespace>`

### Obtener cualquier objeto de k8s
- `kubectl get <tipo_objeto> -n <nombre_namespace>`

### Obtener todos los objeto de k8s (Exceptuando Ingress)
- `kubectl get all -n <nombre_namespace>`

### Nodeport
- `kubectl port-forward service/<service-name> <local-port>:<service-port> -n <nombre_namespace>`

## Configurar Ingress Controller NGINX

- `kubectl create ns nginx-ingress`
- `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
- `helm repo update`
- `helm install nginx-ingress ingress-nginx/ingress-nginx -n nginx-ingress`
- `kubectl get services -n nginx-ingress`

## Presentación
<a href="https://docs.google.com/presentation/d/1GYPgXNPyRHMKvfbtk1m8o_nLeAChx2gLPd0B5ddcNoE/edit?usp=sharing" title="Presentación K8S Workshop">Presentación K8S Workshop</a>