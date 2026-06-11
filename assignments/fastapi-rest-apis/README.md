# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that serves JSON data, handles path and query parameters, and supports create, read, update, and delete operations. You will practice structuring endpoints, validating request data, and returning clear HTTP responses.

## 📝 Tasks

### 🛠️ FastAPI App Setup

#### Description
Create the FastAPI application and set up the basic data model used by the API.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a root or health endpoint that returns a simple JSON response.
- Define Pydantic models for the resource data.
- Store a small sample dataset in memory.

### 🛠️ Read and Create Endpoints

#### Description
Build endpoints that let a client list existing resources, view one resource by ID, and create a new resource.

#### Requirements
Completed program should:

- Return all resources from a `GET` request.
- Return a single resource by ID from a path parameter.
- Return a `404` response when the requested resource does not exist.
- Accept JSON data in a `POST` request to create a new resource.
- Return a `201` response when a resource is created successfully.

### 🛠️ Update, Delete, and Validation

#### Description
Add the remaining REST operations and make sure the API validates data before it is stored or returned.

#### Requirements
Completed program should:

- Update an existing resource with a `PUT` or `PATCH` endpoint.
- Delete a resource with a `DELETE` endpoint.
- Use query parameters to filter or search the resource list.
- Return appropriate HTTP status codes for success and failure cases.
- Validate incoming data using FastAPI and Pydantic.