# ecommerce-cart-service

A FastAPI microservice for managing customer shopping carts, cart item creation, retrieval, and checkout.

## Overview

This service stores cart items in a MySQL database and provides endpoints for cart operations.

## Endpoints

* `POST /api/v1/cart`
* `GET /api/v1/cart/{customer_id}`
* `POST /api/v1/checkout/{customer_id}`

## Database

* MySQL 8.4
* Database: `cart_db`
* Container: `cart-mysql`
* Host port: `3308`
* Container port: `3306`

## Environment Variables

This service loads variables from `.env`.

* `APP_NAME` - application name
* `APP_VERSION` - application version
* `MYSQL_HOST` - MySQL host (default: `localhost`)
* `MYSQL_PORT` - MySQL port (default: `3308`)
* `MYSQL_DATABASE` - database name (default: `cart_db`)
* `MYSQL_USER` - database user (default: `cart_user`)
* `MYSQL_PASSWORD` - database password (default: `cart_password`)
* `PRODUCT_SERVICE_URL` - product service URL
* `ORDER_SERVICE_URL` - order service URL

## Run with Docker Compose

1. Ensure Docker Desktop is running.
2. Create the shared network if needed:

   ```powershell
   docker network create ecommerce-network
   ```

3. Start the service:

   ```powershell
   docker compose up --build -d
   ```

4. Verify the health endpoint:

   ```text
   http://localhost:8001/health
   ```

## Run All Services

1. Ensure Docker Desktop is running.
2. Create the shared network if it does not already exist:

   ```powershell
   docker network create ecommerce-network
   ```

3. Start all services in order:

   ```powershell
   cd repo\ecommerce-product-service
   docker compose up --build -d

   cd ..\ecommerce-cart-service
   docker compose up --build -d

   cd ..\ecommerce-order-service
   docker compose up --build -d

   cd ..\ecommerce-api-gateway
   docker compose up --build -d
   ```

4. Verify:

   * Product Service: `http://localhost:8000/api/v1/products/health`
   * Cart Service: `http://localhost:8001/health`
   * Order Service: `http://localhost:8002/health`
   * API Gateway: `http://localhost:8080/health`

## Cleanup

To stop and remove all containers for the full stack:

```powershell
cd repo\ecommerce-product-service
docker compose down

cd ..\ecommerce-cart-service
docker compose down

cd ..\ecommerce-order-service
docker compose down

cd ..\ecommerce-api-gateway
docker compose down
```

If the shared network is no longer needed:

```powershell
docker network rm ecommerce-network
```

## Project Structure

* `app/main.py`
* `app/api/cart.py`
* `app/config.py`
* `app/db/database.py`
* `app/models/`
* `app/schemas/`
* `app/services/`

