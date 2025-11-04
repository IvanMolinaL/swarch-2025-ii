# Laboratorio 1 - Sistema Monolítico

## Representación Arquitectónica

### Arquitectura C&C
![C&C Diagram swarch-L1](C&C_swarch-L1.png)

### Estructura de Proyecto
swarch-L1/
├── 🐳 Dockerfile
├── 🐳 docker-compose.yaml
└── 📁 app/
    ├── 🐍 app.py              (Flask Application)
    ├── 🐍 config.py           (Configuration)
    ├── 📄 requirements.txt    (Dependencies)
    ├── 📁 models/             (Data Layer)
    │   ├── __init__.py
    │   ├── book.py
    │   └── literary_genre.py
    ├── 📁 repositories/       (Data Access Layer)
    │   ├── __init__.py
    │   ├── book_repository.py
    │   └── genre_repository.py
    ├── 📁 services/           (Business Logic Layer)
    │   ├── __init__.py
    │   ├── book_service.py
    │   └── genre_service.py
    ├── 📁 controllers/        (Presentation Layer)
    │   ├── __init__.py
    │   ├── book_controller.py
    │   └── genre_controller.py
    └── 📁 templates/          (View Layer)
        ├── base.html
        ├── 📁 book/
        │   ├── list.html
        │   └── create.html
        └── 📁 genre/
            ├── list.html
            └── create.html

### Vista de Despliegue

## Propiedades del Sistema

### 1.
### 2.
### 3.
### 4.
### 5.

## Testing
