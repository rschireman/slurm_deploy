# Deploy Code on a Slurm Cluster using GitHub Actions

This repository provides a framework for deploying code to a Slurm cluster using GitHub Actions. By leveraging GitHub Actions, you can automate the deployment process, ensuring your code is consistently and efficiently deployed to your Slurm-managed compute resources.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Repository Secrets](#repository-secrets)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Slurm is a highly scalable cluster management and job scheduling system for large and small Linux clusters. GitHub Actions is a CI/CD platform that allows you to automate your build, test, and deployment pipeline. This repository demonstrates how to combine these tools to deploy your code onto a Slurm cluster seamlessly. This example utilizes code from my Ph.D. that generates reference datasets for ML potential training.

## Prerequisites

- A Slurm cluster set up and running.
- GitHub repository with access to GitHub Actions.
- SSH access to the Slurm cluster.
- Basic knowledge of YAML and GitHub Actions.

## Setup

### Repository Secrets

To securely connect to your Slurm cluster, you need to add the following secrets to your GitHub repository:

1. **SLURM_USER**: The username for SSH access to the Slurm cluster.
2. **SLURM_HOST**: The hostname or IP address of the Slurm cluster.
3. **SSH_PRIVATE_KEY**: The private SSH key used for authentication.

To add these secrets:
1. Go to your GitHub repository.
2. Click on `Settings`.
3. Navigate to `Secrets and variables` > `Actions`.
4. Click on `New repository secret` and add the required secrets.

## Usage
1. Push code to the main branch of your repository.
2. GitHub Actions will trigger the workflow defined in .github/workflows/deploy.yml.
3. The workflow will:
     - Checkout the latest code.
     - Set up SSH keys (see above).
     - Copy your code to the Slurm cluster.
     - Submit a job to the Slurm scheduler.

You can monitor the progress and logs of the workflow in the Actions tab of your GitHub repository.