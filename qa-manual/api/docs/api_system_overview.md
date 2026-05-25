# System Overview – JSONPlaceholder API

## System Description
JSONPlaceholder is a free fake REST API used for testing and prototyping.
It simulates CRUD operations without persisting data permanently.

## Base URL
https://jsonplaceholder.typicode.com

## API Type
RESTful API

## Supported Methods
- GET
- POST
- PUT
- PATCH
- DELETE

## Purpose of Testing
Validate API behavior, request/response structure, status codes, and data consistency from a QA API testing perspective.

## API Behavior Notes

- - Requests to non-existent resources (e.g. /posts/9999) return HTTP 404 with an empty response body.
- DELETE requests do not actually remove data due to mock API behavior.
