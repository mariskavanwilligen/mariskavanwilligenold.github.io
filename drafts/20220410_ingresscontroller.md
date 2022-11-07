Title: Scaling Options Azure Kubernetes Service (AKS)
Date: 2022-04-05 10:43
Tags: Azure, Kubernetes, Scaling, Pods, AKS, Instances
Slug: 
Authors: Mariska van Willigen
Summary: Overview of the different scaling options in Azure Kubernetes Service

``` sh
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: pdf-ingress
  namespace: pdf
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/use-regex: "true"
    nginx.ingress.kubernetes.io/rewrite-target: /$1
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  tls:
    - hosts:
        - {{ environ('INGRESS_IP') }}
      secretName: aks-ingress-tls
  rules:
    - http:
        paths:
          - path: /(.*)
            pathType: Prefix
            backend:
              service:
                name: model-api
                port:
                  number: 80
``` 