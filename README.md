# Order Processing System

## **1. Project Overview**

### **Objective:**

The objective of this project is to design and implement an asynchronous, scalable order processing system that handles incoming webhooks from multiple store types (e.g., Salla and Zid) while ensuring:

1. **Concurrency Handling**
2. **Duplicate Prevention**
3. **Dynamic Schema Handling**
4. **Scalability** and **Performance Optimization**

### **Key Features:**

- **Dynamic Data Processing:** Supports multiple store types with different schemas.
- **Concurrency Management:** Ensures data consistency using database locks and transactions.
- **Duplicate Prevention:** Checks for duplicate orders before processing.
- **Async Task Handling:** Utilizes Celery and Redis for asynchronous processing.
- **Dockerized Environment:** Containers for PostgreSQL, Redis, Celery, and Django.
- **Testing Tools:** Provides scripts to simulate real-world webhook requests.

---

## **2. System Design and Architecture**

### **High-Level Design:**

1. **API Layer:** Receives webhook data from stores and forwards it for processing.
2. **Service Layer:** Contains the business logic for validating and processing orders.
3. **Mapper Layer:** Maps incoming data to standardized formats.
4. **Database Layer:** Stores processed data with constraints to ensure consistency.
5. **Task Queue Layer:** Handles async task execution using Celery and Redis.
6. **Scheduler:** Periodic tasks for system health checks and data cleanup.

### **Component Diagram:**

- API Gateway → Django Views → Service Layer → Database + Celery Task → Redis → Celery Worker

---

## **3. Implementation Details**

### **Models:**

#### **StoreTypes Model:** Defines store types with schema variations.

#### **Stores Model:** Stores information about each store.

#### **Orders Model:** Tracks orders and prevents duplicates.

#### **Customers Model:** Manages customer data.

### **Mappers:**

- **Dynamic Mapper:** Maps incoming webhook data to match our internal schema dynamically.
- **Factory Pattern:** Supports schema extensions for future store types.

### **Services:**

- **OrderProcessingService:** Validates, processes, and saves orders.
- **Transaction Handling:** Uses atomic transactions to maintain data integrity.

### **Tasks:**

- **Async Processing:** Celery tasks for webhook processing.
- **Retry Mechanism:** Handles transient failures with exponential backoff.

---

## **4. Dockerization**

### **Docker Compose Setup:**

- **Services:**
  1. `web`: Django application.
  2. `redis`: Redis message broker.
  3. `worker`: Celery worker.
  4. `beat`: Celery Beat scheduler.
  5. `db`: PostgreSQL database.

### **Dockerfile Configuration:**

- Multi-stage builds for production-ready deployment.
- Environment variables for sensitive configurations.


---

## **5. Recommendations for Improvement**

1. **Improved Schema Validation:** Use JSON schema for validating incoming data.
2. **Event-Driven Architecture:** Replace HTTP requests with message queues like RabbitMQ.
3. **Monitoring and Logging:** Add ELK for metrics and visualization.
4. **Load Balancing:** Deploy multiple Celery workers for better horizontal scaling.
5. **Database Sharding:** Optimize for high-traffic scenarios by splitting data across databases.
6. **Caching Layer:** Use Redis as a cache for frequently accessed data.
7. **Error Handling Enhancements:** More robust handling for network failures and retries.

---

## **6. Setup and Execution Guide**

### **1. Prerequisites:**

- **Docker and Docker Compose installed.**

### **2. Build and Start Services:**

```bash
# Build and start containers
docker-compose up --build
```

### **3. Run Tests:**

```bash
# Execute test script
docker-compose exec web python /app/test.py
```

### **4. Stop Services:**

```bash
docker-compose down
```

---

## **Conclusion:**

This project demonstrates a scalable and modular solution for processing dynamic webhook data. It handles concurrency, avoids duplication, and integrates async processing. The dockerized setup ensures portability and ease of deployment. Future enhancements can focus on event-driven systems, distributed caching, and performance optimization to handle enterprise-level workloads.

