# Person API Documentation

## Introduction

This API provides CRUD (Create, Read, Update, Delete) operations for managing person resources.

## Base URL

The base URL for all API endpoints is: `/api/`

## Authentication

This API does not currently require authentication.

## Standard Request/Response Formats

### Create a new person (POST /api/)

Request:

```json
{
  "name": "John Doe"
}
```


Response:

```json
{
  "id": 1,
  "name": "John Doe"
}
```

Get details of a person (GET /api/{id}/)

Response:

```json
{
  "id": 1,
  "name": "John Doe"
}
```

Update a person (PUT /api/{id}/)

Request:

```json
{
  "name": "Jane Doe"
}
```

Response:

```json
{
  "id": 1,
  "name": "Jane Doe"
}
```


Sample Usage
cURL Examples
Create a new person:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8000/api/
```

