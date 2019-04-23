import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

app_labels = { "app": "nginx" }

deployment = Deployment(
    "nginx",
    spec={
        "selector": { "match_labels": app_labels },
        "replicas": 1,
        "template": {
            "metadata": { "labels": app_labels },
            "spec": { "containers": [{ "name": "nginx", "image": "nginx" }] }
        }
    })

service = Service(
    "nginx",
    spec={
        "ports": [
            {
                "port": 80,
                "targetPort": 80,
                "protocol": "TCP"
            }
        ]
    }
)

pulumi.export("name", deployment.metadata["name"])
