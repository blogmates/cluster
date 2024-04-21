import subprocess

# Deploy authentication pod
subprocess.run(["kubectl", "apply", "-f", "auth-pod.yaml", "-n", "auth"], check=True)

# Deploy authentication service
subprocess.run(["kubectl", "apply", "-f", "auth-service.yaml", "-n", "auth"], check=True)

# Deploy authorisation pod
subprocess.run(["kubectl", "apply", "-f", "authorisation-pod.yaml", "-n", "auth"], check=True)

# Deploy authorisation service
subprocess.run(["kubectl", "apply", "-f", "authorisation-service.yaml", "-n", "auth"], check=True)

# Deploy backend pod
subprocess.run(["kubectl", "apply", "-f", "backend-pod.yaml", "-n", "app"], check=True)

# Deploy backend service
subprocess.run(["kubectl", "apply", "-f", "backend-service.yaml", "-n", "app"], check=True)

# Deploy io pod
subprocess.run(["kubectl", "apply", "-f", "io-pod.yaml", "-n", "app"], check=True)

# Deploy io service
subprocess.run(["kubectl", "apply", "-f", "io-service.yaml", "-n", "app"], check=True)

# Deploy test-generic pod
subprocess.run(["kubectl", "apply", "-f", "test-generic-pod.yaml"], check=True)
