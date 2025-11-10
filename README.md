# E-commerce Product Service

A containerized Flask microservice for product recommendations with CI/CD pipeline, image building and Kubernetes deployment.

## Features
- Flask API with `/` and `/products` endpoints
- Docker containerization with Alpine Linux
- Automated CI/CD pipeline with GitHub Actions
- Kubernetes deployment with high availability

## Tech Stack
- **Application**: Python Flask
- **Containerization**: Docker
- **Image Registry**: Docker Hub
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions

## Deployment

### Docker
```bash
docker build -t product-service .
docker run -p 8080:5000 product-service
```

### Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### CI/CD Pipeline
- Automated testing with pytest
- Docker image build and push to Docker Hub
- Kubernetes deployment configuration

## Access
- Local: http://localhost:8080/products
- Kubernetes: http://localhost/products
