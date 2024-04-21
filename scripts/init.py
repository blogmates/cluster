import subprocess
import time

# Start Minikube cluster
subprocess.run(["minikube", "start"], check=True)

# Wait for Minikube to be ready
while True:
    try:
        subprocess.run(["minikube", "status"], check=True)
        break
    except subprocess.CalledProcessError:
        print("Waiting for Minikube to be ready...")
        time.sleep(10)

# Create namespaces
subprocess.run(["kubectl", "create", "namespace", "auth"], check=True)
subprocess.run(["kubectl", "create", "namespace", "app"], check=True)