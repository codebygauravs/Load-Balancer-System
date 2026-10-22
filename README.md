# DevOps Load Balancer System (Mini Production Setup)

## Overview

This project demonstrates a containerized application deployed with multiple instances and load balanced using Nginx. It simulates a real-world DevOps environment where traffic is distributed across multiple containers for scalability and reliability.

---

## Key Features

* Dockerized Python Flask application
* Load balancing using Nginx
* Multiple container instances (horizontal scaling)
* Internal container networking using Docker network
* Health endpoint for monitoring
* Container-aware responses (hostname display)

---

## Architecture

```
User → Nginx (Load Balancer)
           ↓
    ┌───────────────┐
    │   app1        │
    │   app2        │
    └───────────────┘
```

---

## Project Structure

```
Load_Balancer_Setup/
│── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│── nginx/
│   ├── nginx.conf
│
│── README.md
```

---

## Tech Stack

* Python (Flask)
* Docker
* Nginx
* Linux

---

## How to Run

### 1. Build Docker Image

```bash
docker build -t devops-app ./app
```

### 2. Create Network

```bash
docker network create mynet
```

### 3. Run Application Containers

```bash
docker run -d --network mynet --name app1 devops-app
docker run -d --network mynet --name app2 devops-app
```

### 4. Run Nginx Load Balancer

```bash
docker run -d -p 8080:80 \
--network mynet \
-v $(pwd)/nginx/nginx.conf:/etc/nginx/nginx.conf \
nginx
```

---

## Access Application

```
http://localhost:8080
```

Refresh multiple times to see different container responses (load balancing in action).

---

## Sample Output

```
DevOps Load Balanced App

Container: 3fhs8d9
Status: Healthy
Uptime: 120 seconds

Refresh to see load balancing in action
```

---

## Learning Outcomes

* Containerization using Docker
* Service discovery using Docker networks
* Reverse proxy & load balancing with Nginx
* Multi-container architecture design
* Basic system observability (health endpoints)

---

## Future Improvements

* Add Docker Compose for orchestration
* Integrate CI/CD pipeline (GitHub Actions)
* Add monitoring with Prometheus & Grafana
* Implement auto-healing mechanism

---

## Author

**Gaurav Saini**
