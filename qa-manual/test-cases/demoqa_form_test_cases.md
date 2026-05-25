# DEMOQA FORM VALIDATION – TEST CASES

**Application:** DemoQA – Practice Form
**Test Type:** Manual / Functional

---

### TC-FORM-01 — Required fields left empty

**Objective:**
Verify system behavior when mandatory fields are not filled.

**Steps:**

1. Access the DemoQA Automation Practice Form
2. Leave all required fields empty (First Name, Last Name, Gender, Mobile Number)
3. Click **Submit**

**Expected Result:**
The form highlights required fields and prevents submission.

**Status:** Passed

---

### TC-FORM-02 — Invalid email format

**Objective:**
Verify email field validation with an invalid format.

**Test Data:**

* Email: `testemail`

**Steps:**

1. Enter an invalid email address
2. Fill all other required fields with valid data
3. Click **Submit**

**Expected Result:**
The system displays an error or does not accept the invalid email format.

**Status:** Passed

---

### TC-FORM-03 — Mobile number length validation

**Objective:**
Verify validation for mobile number length.

**Test Data:**

* Mobile Number: `12345`

**Steps:**

1. Enter a mobile number with fewer than 10 digits
2. Fill all other required fields
3. Click **Submit**

**Expected Result:**
The form prevents submission or highlights the mobile number field as invalid.

**Status:** Passed

---

### TC-FORM-04 — Mobile number with non-numeric characters

**Objective:**
Ensure that the mobile number field accepts only numeric values.

**Test Data:**

* Mobile Number: `abc1234567`

**Steps:**

1. Enter alphanumeric characters in the mobile number field
2. Attempt to submit the form

**Expected Result:**
The system prevents submission or rejects non-numeric input.

**Status:** Passed

---

### TC-FORM-05 — Gender selection required

**Objective:**
Verify that gender selection is mandatory.

**Steps:**

1. Fill all required fields except Gender
2. Click **Submit**

**Expected Result:**
The form does not submit and indicates that gender selection is required.

**Status:** Passed

---

### TC-FORM-06 — Submission with valid data

**Objective:**
Verify successful form submission with valid input data.

**Test Data:**

* First Name: John
* Last Name: Doe
* Email: [user@example.com](mailto:user@example.com)
* Gender: Male
* Mobile Number: 1234567890

**Steps:**

1. Fill all required fields with valid data
2. Click **Submit**

**Expected Result:**
The form is successfully submitted and a confirmation modal is displayed.

**Status:** Passed

---

### TC-FORM-07 — Hobbies selection

**Objective:**
Verify that one or more hobbies can be selected.

**Steps:**

1. Select one or more hobbies
2. Complete the required fields
3. Submit the form

**Expected Result:**
Selected hobbies are displayed correctly in the submission confirmation.

**Status:** Passed

---

### TC-FORM-08 — File upload (valid file)

**Objective:**
Verify file upload functionality with a valid file.

**Test Data:**

* File type: `.jpg` or `.png`

**Steps:**

1. Click on the upload button
2. Select a valid file
3. Submit the form

**Expected Result:**
The file is uploaded and shown in the confirmation modal.

**Status:** Passed

---

### TC-FORM-09 — File upload (unsupported file type)

**Objective:**
Verify system behavior when uploading an unsupported file type.

**Test Data:**

* File type: `.exe`

**Steps:**

1. Select an unsupported file type
2. Submit the form

**Expected Result:**
The system accepts the file or does not validate file type.

**Status:** Failed

**Related Bug:**  
BUG-DEMOQA-001 – File upload accepts .exe

---

### TC-FORM-10 — State and City dependency

**Objective:**
Verify that City options depend on the selected State.

**Steps:**

1. Select a State
2. Open the City dropdown

**Expected Result:**
Only cities related to the selected state are available.

**Status:** Passed

---

**Notes:**
Some validations in DemoQA are limited. Missing or weak validations should be documented as QA observations or defects.