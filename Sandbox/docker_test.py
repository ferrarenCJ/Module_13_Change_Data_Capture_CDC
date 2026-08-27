# Sandbox/docker_test.py

import docker

client = docker.from_env()

print("Connected to Docker")

containers = client.containers.list(all=True)

print(f"\nContainers Found: {len(containers)}")

for container in containers:

    ports = container.attrs["NetworkSettings"]["Ports"]

    print(
        f"Name: {container.name}"
        f" | Status: {container.status}"
        f" | Image: {container.image.tags}"
        f" | Ports: {ports}"
    )