# Flask REST API – Dockerized & Deployed on AWS ECS Fargate

## Overview
This project demonstrates how to build and deploy a lightweight Python **Flask REST API** inside a **Docker container**, store the image in **Amazon ECR**, and run it serverlessly using **AWS ECS Fargate**.  
The API serves a simple employee dataset through REST endpoints.

---

## Architecture
Flask API → Docker Image → Amazon ECR → Amazon ECS (Fargate) → Public Internet


**Components**
- **Flask** – REST API framework (Python 3.10+)
- **Docker** – containerization for portability
- **Amazon ECR** – private image registry
- **Amazon ECS Fargate** – fully managed container runtime (no servers to manage)
- **AWS CLI** – used for authentication and deployment automation

---

## Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/employees` | Returns all employees in JSON format |
| GET | `/employees/<id>` | Returns one employee by ID |

**Example Output**
```json
[
  {"id": 1, "name": "Mahsa", "role": "Data Scientist"},
  {"id": 2, "name": "Rusbeh", "role": "AI Engineer"},
  {"id": 3, "name": "Sara", "role": "Software Developer"}
]


##Local Setup

# Clone the repository
git clone https://github.com/<your-username>/Flask-Docker_API.git
cd Flask-Docker_API

# Build Docker image
sudo docker build -t flask-docker-api:1.0 .

# Run the container locally
sudo docker run -d -p 5000:5000 flask-docker-api:1.0

# Test the API locally
curl http://localhost:5000/employees

# AWS Deployment Steps
##1. Create and Log in to ECR
aws ecr create-repository --repository-name flask-docker-api --region eu-central-1
aws ecr get-login-password --region eu-central-1 | \
sudo docker login --username AWS --password-stdin <account_id>.dkr.ecr.eu-central-1.amazonaws.com

##2. Tag and Push Image
sudo docker tag flask-docker-api:1.0 <account_id>.dkr.ecr.eu-central-1.amazonaws.com/flask-docker-api:1.0
sudo docker push <account_id>.dkr.ecr.eu-central-1.amazonaws.com/flask-docker-api:1.0

##3. Deploy on ECS Fargate
Create ECS Cluster (Networking Only – Fargate)

Create Task Definition (use the ECR image, container port 5000)

Create Service (launch type Fargate, assign Public IP, allow inbound TCP 5000)

Run Task → copy Public IP from the task details

##4. Test Deployed API
http://<Public-IP>:5000/employees
Example Screenshot
(Optional – include your own)

/screenshots/ecs_running.png

##Cleanup
When finished, stop resources to avoid charges:

1.Set service desired count to 0

2.Delete the service

3.Delete the cluster

4.(Optional) Delete image from ECR

##Author
Developed by **Mahsa Ghaempanah**
Deployed and tested with **AWS Fargate (eu-central-1)**


