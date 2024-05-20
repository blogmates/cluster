import subprocess

# Deploy authentication pod
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/auth-pod.yaml", "-n", "auth"], check=True)

# Deploy authentication service
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/auth-service.yaml", "-n", "auth"], check=True)

# Deploy authorisation pod
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/authorisation-pod.yaml", "-n", "auth"], check=True)

# Deploy authorisation service
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/authorisation-service.yaml", "-n", "auth"], check=True)

# Deploy auth database pod
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/auth-db-pod.yaml", "-n", "auth"], check=True)

# Deploy auth database service
subprocess.run(["kubectl", "apply", "-f", "k8s/auth/auth-db-service.yaml", "-n", "auth"], check=True)

# Deploy backend pod
subprocess.run(["kubectl", "apply", "-f", "k8s/app/backend-pod.yaml", "-n", "app"], check=True)

# Deploy backend service
subprocess.run(["kubectl", "apply", "-f", "k8s/app/backend-service.yaml", "-n", "app"], check=True)

# Deploy io pod
subprocess.run(["kubectl", "apply", "-f", "k8s/app/io-pod.yaml", "-n", "app"], check=True)

# Deploy io service
subprocess.run(["kubectl", "apply", "-f", "k8s/app/io-service.yaml", "-n", "app"], check=True)

# Deploy test-generic pod
subprocess.run(["kubectl", "apply", "-f", "k8s/test/test-generic-pod.yaml"], check=True)

# Deploy test-auth pod
subprocess.run(["kubectl", "apply", "-f", "k8s/test/test-auth-pod.yaml", "-n", "auth"], check=True)

# Deploy test-app pod
subprocess.run(["kubectl", "apply", "-f", "k8s/test/test-app-pod.yaml", "-n", "app"], check=True)
