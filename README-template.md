# Información de la Materia: ST0263 Tópicos Especiales en Telemática

**Estudiante(s):** Santiago Ospina Idrobo, sospinai@eafit.edu.co

**Profesor:** Edwin Nelson Montoya

# Sistema de Compartición de Archivos P2P

## 1. Breve Descripción de la Actividad

Este proyecto implementa un sistema básico de compartición de archivos Peer-to-Peer (P2P) utilizando Django para el servidor central y gRPC para la comunicación entre los peers. El sistema permite a los usuarios simular la subida y descarga de archivos mediante el intercambio de nombres de archivos como strings.

### 1.1. Aspectos Cumplidos

- Implementación de un servidor central en Django para gestionar los peers y la indexación de archivos.
- Uso de gRPC para la comunicación entre peers, permitiendo operaciones de `upload` y `download`.
- Dockerización del servidor central y del peer para facilitar la implementación y ejecución.
- Manejo de la lista de archivos disponibles en cada peer y actualización dinámica de esta lista.

### 1.2. Aspectos No Cumplidos

- La transferencia real de archivos no se implementó; solo se simula con nombres de archivos.
- No se implementaron medidas de seguridad avanzadas para la comunicación entre peers.

## 2. Información General de Diseño

Se utilizó una arquitectura P2P donde cada peer puede funcionar tanto como cliente como servidor. Django REST Framework facilita la gestión de peers y archivos, mientras que gRPC se usa para la comunicación directa entre peers.

## 3. Ambiente de Desarrollo

- **Lenguaje de Programación**: Python 3.9
- **Framework**: Django 5.0.2, djangorestframework 3.14.0
- **gRPC**: grpcio 1.62.0, grpcio-tools 1.62.0
- **Docker**: Para contenerización de la aplicación.

### Como se Compila y Ejecuta

- **Servidor Central**: `docker build -t servidor-central .` seguido por `docker run -p 8000:8000 servidor-central`.
- **Peer**: `docker build -t peer-app .` seguido por `docker run -p 50051:50051 peer-app`.

### Como se Compila y Ejecuta - Local

- **Servidor Central**: `python manage.py runserver`
- **Peer**: `python grpc_server.py` seguido por `python grpc_client.py`.

### Configuración

Los parámetros del proyecto, como IP y puertos, se configuran mediante archivos `config.json` en cada peer, y variables de entorno o archivos de configuración para el servidor central de Django.

## 4. Ambiente de Ejecución

Similar al ambiente de desarrollo con las imágenes Docker construidas a partir de los `Dockerfile` proporcionados.

### Como se Lanza el Servidor

Utilizar los comandos Docker mencionados anteriormente para iniciar tanto el servidor central como los peers.

### Mini Guía de Uso

- **Para los Peers**: Ejecute el script `interact_with_server.py` para interactuar con el sistema a través de un menú CLI que permite realizar operaciones de `login`, `logout`, `send_index`, `query`, `upload`, y `download`.

## 5. Otra Información

Este proyecto es un ejemplo básico y conceptual de un sistema P2P y está diseñado principalmente con fines educativos.

## Referencias

- Documentación oficial de Django: https://docs.djangoproject.com/en/4.0/
- Documentación oficial de gRPC: https://grpc.io/docs/languages/python/basics/
- Docker Docs: https://docs.docker.com/