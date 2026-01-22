```text
  _____                           _ _     
 |_   _| __ ___ _ __   ___ __ _ __| (_)___ 
   | || '__/ _ \ '_ \ / __/ _` / _` | / __|
   | || | |  __/ | | | (_| (_| | (_| | \__ \
   |_||_|  \___|_| |_|\___\__,_|\__,_|_|___/
   
   Distributed Microservices Home Suite
   [ Python | Go | Java | Angular | K8s ]
```

# Trencadís: A Clean Architecture Microservices Suite

**Trencadís** is a home management ecosystem built to demonstrate modern software engineering practices. Inspired by the mosaic technique of **Catalan Modernism**, this project assembles diverse technologies (Python, Go, Java, Angular) into a cohesive, scalable, and robust distributed system.

## 🏛 Architecture Overview
This project follows the **Clean Architecture** principles by Robert C. Martin. Each service is designed with a strict separation of concerns, ensuring the business logic remains independent of frameworks and external agencies.

- **Frontend:** Angular 17+ (Reactive State Management)
- **Recipe Service:** Python & FastAPI (High-performance API)
- **Shopping List Service:** Go (Concurrent & Lightweight)
- **Spending Service:** Java & Spring Boot (Enterprise-grade robustness)
- **Infrastructure:** Kubernetes (Orchestration) & GitHub Actions (CI/CD)

## 🛠 Project Roadmap
- [ ] **Phase 0: Create repository and project structure** - Current
- [ ] **Phase 1: Recipe Service (Python)** - Upcoming
- [ ] **Phase 2: Shopping List (Go)** - Upcoming
- [ ] **Phase 3: Financial Module (Java)** - Planned
- [ ] **Phase 4: Dashboard (Angular)** - Planned
- [ ] **Phase 5: Cloud Native Deployment (K8s)** - Planned

## 👨‍💻 Engineering Standards
- **Clean Code:** Self-documenting code, SRP, and meaningful naming.
- **SOLID Principles:** Strictly followed across all languages.
- **Testing:** Unit and Integration tests for every business use case.
- **Documentation:** Architecture decision records (ADR) and C4 Diagrams.

## 📐 Engineering Principles

This project serves as a practical implementation of high-level software engineering standards.

### Clean Architecture (by Robert C. Martin)
The architecture is structured in concentric layers, where dependencies only point inwards. This ensures that the **Business Logic (Domain)** is:
- **Independent of Frameworks:** The UI, Database, and external tools are treated as plugins.
- **Testable:** Logic can be tested without an external server or database.
- **Independent of UI:** The UI can change without changing the rest of the system.

### SOLID Principles
Every module in **Trencadís** is built with these principles in mind:
- **S**ingle Responsibility: Each class or function has one, and only one, reason to change.
- **O**pen/Closed: Software entities are open for extension but closed for modification.
- **L**iskov Substitution: Objects are replaceable with instances of their subtypes without altering correctness.
- **I**nterface Segregation: Clients should not be forced to depend on methods they do not use.
- **D**ependency Inversion: High-level modules do not depend on low-level modules; both depend on abstractions.

## Author
by AFelipeTrujillo