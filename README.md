# Wisecow Application - DevOps Trainee Assignment
## Project Overview
This repository contains the Wisecow application, containerized, pushed to DockerHub, and deployed on an Amazon EKS cluster as part of the AccuKnox DevOps Trainee practical assessment.

The application is exposed via the domain **https://culmarket.store** with TLS for secure HTTPS communication.
## Problem Statements Completed

### PS1: Containerisation and Deployment
- Dockerfile created for the Wisecow app.
- Docker image built and pushed to DockerHub.
- Application deployed on Amazon EKS cluster.
- Kubernetes manifests include Deployment, Service, and Ingress with TLS.
- TLS certificate configured for the domain `culmarket.store`.

### PS2: Scripts bash and python
- **System Health Monitoring Script**: Monitors CPU, memory, disk, and running processes. Alerts if thresholds exceeded.
- **Application Health Checker**: Checks uptime and HTTP status codes of the application.

### PS3: KubeArmor Policy
- Zero-trust KubeArmor policy created and applied to the Kubernetes workload.
- Screenshot of policy violations included in `screenshots/` folder.

## CI/CD
- GitHub Actions workflow automates:
  - Docker image build and push to DockerHub on commit.
  - Automatic deployment to EKS cluster after successful image build.
