\# 🚀# 🚀 Microservices Lab - E-Commerce Platform



!\[Python](https://img.shields.io/badge/python-3.11-blue)

!\[Docker](https://img.shields.io/badge/docker-ready-blue)

!\[License](https://img.shields.io/badge/license-MIT-green)



> A production-ready microservices architecture demonstrating cloud-native patterns, health monitoring, and scalable system design.



\## 📋 Overview



This project demonstrates a complete microservices ecosystem with automated health checks, API gateway routing, and containerized deployment. Built to showcase DevOps best practices and modern software architecture.



\## 🏗️ Architecture

```

&nbsp;                   Client/Browser

&nbsp;                         ↓

&nbsp;                  API Gateway (Nginx)

&nbsp;                      Port: 80

&nbsp;                         ↓

&nbsp;       ┌─────────────────┼─────────────────┐

&nbsp;       ↓                 ↓                 ↓

&nbsp;  User Service    Product Service    Order Service

&nbsp;   Port: 8001        Port: 8002        Port: 8003

&nbsp;                                           ↓

&nbsp;                                     PostgreSQL DB

&nbsp;                                       Port: 5432

```



\## ✨ Features



\- ✅ \*\*Microservices Architecture\*\* - Independent, scalable services

\- ✅ \*\*Health Monitoring\*\* - Automated health checks with auto-recovery

\- ✅ \*\*API Gateway\*\* - Centralized routing with Nginx

\- ✅ \*\*Containerization\*\* - Full Docker support with Docker Compose

\- ✅ \*\*Database Integration\*\* - PostgreSQL with SQLAlchemy ORM

\- ✅ \*\*RESTful APIs\*\* - Clean API design with proper HTTP methods

\- ✅ \*\*Service Independence\*\* - Each service can be deployed separately



\## 🛠️ Tech Stack



| Component | Technology |

|-----------|-----------|

| \*\*Backend Services\*\* | Python 3.11 (Flask, FastAPI) |

| \*\*Database\*\* | PostgreSQL 16 |

| \*\*API Gateway\*\* | Nginx |

| \*\*Containerization\*\* | Docker, Docker Compose |

| \*\*Health Monitoring\*\* | Docker Health Checks |



\## 🚀 Quick Start



\### Prerequisites



\- \[Docker Desktop](https://www.docker.com/products/docker-desktop/)

\- \[Git](https://git-scm.com/downloads)



\### Installation \& Setup



1\. \*\*Clone the repository\*\*

```bash

&nbsp;  git clone https://github.com/YOUR\_USERNAME/microservices-lab.git

&nbsp;  cd microservices-lab

```



2\. \*\*Start all services\*\*

```bash

&nbsp;  docker-compose up -d

```



3\. \*\*Verify services are healthy\*\* (wait 30 seconds for startup)

```bash

&nbsp;  docker-compose ps

```

&nbsp;  All services should show status: "Up (healthy)"



4\. \*\*Test the services\*\*

```bash

&nbsp;  # User Service

&nbsp;  curl http://localhost:8001/health

&nbsp;  

&nbsp;  # Product Service

&nbsp;  curl http://localhost:8002/health

&nbsp;  

&nbsp;  # Order Service

&nbsp;  curl http://localhost:8003/health

&nbsp;  

&nbsp;  # API Gateway

&nbsp;  curl http://localhost/health

```



\## 📚 API Documentation



\### User Service Endpoints

```http

GET /api/users          # Get all users

GET /api/users/{id}     # Get user by ID

GET /health             # Health check

```



\### Product Service Endpoints

```http

GET /api/products       # Get all products

GET /api/products/{id}  # Get product by ID

GET /health             # Health check

```



\### Order Service Endpoints

```http

GET /api/orders         # Get all orders

POST /api/orders        # Create new order

GET /health             # Health check

```



\### Example: Create an Order

```bash

curl -X POST http://localhost/api/orders \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{

&nbsp;   "user\_id": 1,

&nbsp;   "product\_id": 1,

&nbsp;   "quantity": 2,

&nbsp;   "total\_price": 1999.98

&nbsp; }'

```



\## 📁 Project Structure

```

microservices-lab/

├── user-service/           # User management service

│   ├── app.py             # Flask application

│   ├── Dockerfile         # Container definition

│   └── requirements.txt   # Python dependencies

├── product-service/        # Product catalog service

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt

├── order-service/          # Order processing service

│   ├── app.py             # FastAPI application

│   ├── Dockerfile

│   └── requirements.txt

├── api-gateway/            # Nginx API gateway

│   └── nginx.conf         # Routing configuration

├── docker-compose.yml      # Service orchestration

└── README.md

```



\## 🔧 Configuration



\### Environment Variables



The order service uses these environment variables:

```bash

DATABASE\_URL=postgresql://orderuser:orderpass@order-db:5432/orders

```



\### Health Check Configuration



All services include health endpoints that return:

```json

{

&nbsp; "status": "healthy",

&nbsp; "service": "service-name",

&nbsp; "timestamp": "2025-12-28T12:00:00"

}

```



\## 📊 Monitoring



\### View Service Logs

```bash

\# All services

docker-compose logs -f



\# Specific service

docker-compose logs -f user-service

```



\### Check Resource Usage

```bash

docker stats

```



\### Service Health Status

```bash

docker inspect microservices-lab-user-service --format='{{.State.Health.Status}}'

```



\## 🛑 Stopping Services

```bash

\# Stop all services

docker-compose down



\# Stop and remove volumes

docker-compose down -v

```



\## 🔄 Making Changes



After modifying code:

```bash

\# Rebuild specific service

docker-compose build user-service



\# Restart service

docker-compose up -d user-service

```



\## 🎯 Future Enhancements



\- \[ ] Add CI/CD pipeline with GitHub Actions

\- \[ ] Implement JWT authentication

\- \[ ] Add Prometheus \& Grafana monitoring

\- \[ ] Kubernetes deployment manifests

\- \[ ] Service-to-service communication

\- \[ ] API rate limiting

\- \[ ] Frontend application



\## 🤝 Contributing



Contributions are welcome! Feel free to open issues or submit pull requests.



\## 📝 License



This project is licensed under the MIT License.



\## 👤 Author



\*\*Your Name\*\*

\- GitHub: \[@YOUR\_USERNAME](https://github.com/YOUR\_USERNAME)

\- Email: your.email@example.com



---



⭐ If you find this project helpful, please give it a star! Microservices Lab - E-Commerce Platform



!\[Python](https://img.shields.io/badge/python-3.11-blue)

!\[Docker](https://img.shields.io/badge/docker-ready-blue)

!\[License](https://img.shields.io/badge/license-MIT-green)



> A production-ready microservices architecture demonstrating cloud-native patterns, health monitoring, and scalable system design.



\## 📋 Overview



This project demonstrates a complete microservices ecosystem with automated health checks, API gateway routing, and containerized deployment. Built to showcase DevOps best practices and modern software architecture.



\## 🏗️ Architecture

```

&nbsp;                   Client/Browser

&nbsp;                         ↓

&nbsp;                  API Gateway (Nginx)

&nbsp;                      Port: 80

&nbsp;                         ↓

&nbsp;       ┌─────────────────┼─────────────────┐

&nbsp;       ↓                 ↓                 ↓

&nbsp;  User Service    Product Service    Order Service

&nbsp;   Port: 8001        Port: 8002        Port: 8003

&nbsp;                                           ↓

&nbsp;                                     PostgreSQL DB

&nbsp;                                       Port: 5432

```



\## ✨ Features



\- ✅ \*\*Microservices Architecture\*\* - Independent, scalable services

\- ✅ \*\*Health Monitoring\*\* - Automated health checks with auto-recovery

\- ✅ \*\*API Gateway\*\* - Centralized routing with Nginx

\- ✅ \*\*Containerization\*\* - Full Docker support with Docker Compose

\- ✅ \*\*Database Integration\*\* - PostgreSQL with SQLAlchemy ORM

\- ✅ \*\*RESTful APIs\*\* - Clean API design with proper HTTP methods

\- ✅ \*\*Service Independence\*\* - Each service can be deployed separately



\## 🛠️ Tech Stack



| Component | Technology |

|-----------|-----------|

| \*\*Backend Services\*\* | Python 3.11 (Flask, FastAPI) |

| \*\*Database\*\* | PostgreSQL 16 |

| \*\*API Gateway\*\* | Nginx |

| \*\*Containerization\*\* | Docker, Docker Compose |

| \*\*Health Monitoring\*\* | Docker Health Checks |



\## 🚀 Quick Start



\### Prerequisites



\- \[Docker Desktop](https://www.docker.com/products/docker-desktop/)

\- \[Git](https://git-scm.com/downloads)



\### Installation \& Setup



1\. \*\*Clone the repository\*\*

```bash

&nbsp;  git clone https://github.com/YOUR\_USERNAME/microservices-lab.git

&nbsp;  cd microservices-lab

```



2\. \*\*Start all services\*\*

```bash

&nbsp;  docker-compose up -d

```



3\. \*\*Verify services are healthy\*\* (wait 30 seconds for startup)

```bash

&nbsp;  docker-compose ps

```

&nbsp;  All services should show status: "Up (healthy)"



4\. \*\*Test the services\*\*

```bash

&nbsp;  # User Service

&nbsp;  curl http://localhost:8001/health

&nbsp;  

&nbsp;  # Product Service

&nbsp;  curl http://localhost:8002/health

&nbsp;  

&nbsp;  # Order Service

&nbsp;  curl http://localhost:8003/health

&nbsp;  

&nbsp;  # API Gateway

&nbsp;  curl http://localhost/health

```



\## 📚 API Documentation



\### User Service Endpoints

```http

GET /api/users          # Get all users

GET /api/users/{id}     # Get user by ID

GET /health             # Health check

```



\### Product Service Endpoints

```http

GET /api/products       # Get all products

GET /api/products/{id}  # Get product by ID

GET /health             # Health check

```



\### Order Service Endpoints

```http

GET /api/orders         # Get all orders

POST /api/orders        # Create new order

GET /health             # Health check

```



\### Example: Create an Order

```bash

curl -X POST http://localhost/api/orders \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{

&nbsp;   "user\_id": 1,

&nbsp;   "product\_id": 1,

&nbsp;   "quantity": 2,

&nbsp;   "total\_price": 1999.98

&nbsp; }'

```



\## 📁 Project Structure

```

microservices-lab/

├── user-service/           # User management service

│   ├── app.py             # Flask application

│   ├── Dockerfile         # Container definition

│   └── requirements.txt   # Python dependencies

├── product-service/        # Product catalog service

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt

├── order-service/          # Order processing service

│   ├── app.py             # FastAPI application

│   ├── Dockerfile

│   └── requirements.txt

├── api-gateway/            # Nginx API gateway

│   └── nginx.conf         # Routing configuration

├── docker-compose.yml      # Service orchestration

└── README.md

```



\## 🔧 Configuration



\### Environment Variables



The order service uses these environment variables:

```bash

DATABASE\_URL=postgresql://orderuser:orderpass@order-db:5432/orders

```



\### Health Check Configuration



All services include health endpoints that return:

```json

{

&nbsp; "status": "healthy",

&nbsp; "service": "service-name",

&nbsp; "timestamp": "2025-12-28T12:00:00"

}

```



\## 📊 Monitoring



\### View Service Logs

```bash

\# All services

docker-compose logs -f



\# Specific service

docker-compose logs -f user-service

```



\### Check Resource Usage

```bash

docker stats

```



\### Service Health Status

```bash

docker inspect microservices-lab-user-service --format='{{.State.Health.Status}}'

```



\## 🛑 Stopping Services

```bash

\# Stop all services

docker-compose down



\# Stop and remove volumes

docker-compose down -v

```



\## 🔄 Making Changes



After modifying code:

```bash

\# Rebuild specific service

docker-compose build user-service



\# Restart service

docker-compose up -d user-service

```



\## 🎯 Future Enhancements



\- \[ ] Add CI/CD pipeline with GitHub Actions

\- \[ ] Implement JWT authentication

\- \[ ] Add Prometheus \& Grafana monitoring

\- \[ ] Kubernetes deployment manifests

\- \[ ] Service-to-service communication

\- \[ ] API rate limiting

\- \[ ] Frontend application



\## 🤝 Contributing



Contributions are welcome! Feel free to open issues or submit pull requests.



\## 📝 License



This project is licensed under the MIT License.



\## 👤 Author



\*\*Your Name\*\*

\- GitHub: \[@prathibha18042](https://github.com/prathibha18042)

\- Email: prathibha18042@gmail.com

---



⭐ If you find this project helpful, please give it a star!

