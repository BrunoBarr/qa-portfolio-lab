# API Test Cases – JSONPlaceholder

## TC-API-GET-01 — Get all posts

**Method:** GET  
**Endpoint:** /posts

**Steps:**
1. Send GET request to `/posts`

**Expected Result:**
- Status code 200
- Response body contains a list of posts

**Actual Result:**
- Status code 200
- Response returned 100 posts

**Status:** Pass  
**Execution date:** 2026-01-29  
**Tool:** Postman  

**Notes:**
API returns 100 posts as expected.

**Evidence:**  
See: `/manual/api/evidence/TC-API-GET-01.png`

---

## TC-API-GET-02 — Get post by valid ID

**Method:** GET  
**Endpoint:** /posts/1

**Expected Result:**
- Status code 200
- Response contains post with ID 1

**Actual Result:**
- Status code 200
- Response returned post with ID 1

**Status:** Pass  
**Execution date:** 2026-01-29  
**Tool:** Postman

**Evidence:**  
See: `/manual/api/evidence/TC-API-GET-02.png`

---

## TC-API-GET-03 — Get post by invalid ID

**Method:** GET  
**Endpoint:** /posts/9999

**Expected Result:**
- Status code 404
- Empty response body

**Actual Result:**
- Status code 404
- Empty object returned({})

**Status:** Pass  
**Execution date:** 2026-01-29  
**Tool:** Postman

**Evidence:**  
See: `/manual/api/evidence/TC-API-GET-03.png`

---

## TC-API-POST-01 — Create new post

**Method:** POST  
**Endpoint:** /posts

**Body (JSON):**
```json
{
  "title": "QA Test",
  "body": "Testing API with Postman",
  "userId": 1
}
```
**Expected Result:**
- Status code 201
- Response returns created object with ID

**Actual Result:**
- Status code 201
- Object returned with generated ID

**Status:** Pass  
**Execution date:** 2026-01-29  
**Tool:** Postman  

**Notes:**
JSONPlaceholder simulates creation but does not persist data.

See: `/manual/api/evidence/TC-API-POST-01.png`

---

## TC-API-DELETE-01 — Delete post

**Method:** DELETE
**Endpoint:** /posts/1

**Expected Result:** 
- Status code 200 or 204

**Actual Result:**
- Status code 200
- Empty response body

**Status:** Pass  
**Execution date:** 2026-01-29  
**Tool:** Postman  

See: `/manual/api/evidence/TC-API-DELETE-01.png`