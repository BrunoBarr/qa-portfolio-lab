# Test Cases – SauceDemo

---

## LOGIN

### TC-LOGIN-01 — Login with valid credentials

**Precondition:**  
Registered user

**Test data:**
- Username: standard_user
- Password: secret_sauce

**Steps:**
1. Access https://www.saucedemo.com
2. Enter a valid username
3. Enter a valid password
4. Click Login

**Expected result:**  
User is redirected to the products page.

**Status:** Passed

---

### TC-LOGIN-02 — Login with invalid password

**Test data:**
- Username: standard_user
- Password: wrong_password

**Steps:**
1. Access the website
2. Enter a valid username
3. Enter an invalid password
4. Click Login

**Expected result:**  
Error message indicating invalid credentials.

**Status:** Passed

---

### TC-LOGIN-03 — Login with empty fields

**Steps:**
1. Access the website
2. Click Login without filling in the fields

**Expected result:**  
Error message requesting the username to be filled in.

**Status:** Passed

---

### TC-LOGIN-04 — Login with locked-out user

**Test data:**
- Username: locked_out_user
- Password: secret_sauce

**Steps:**
1. Access the website
2. Enter username and password
3. Click Login

**Expected result:**  
Message informing that the user is locked out.

**Status:** Passed

---

## PRODUCTS

### TC-PROD-01 — View product list

**Precondition:**  
User logged in

**Steps:**
1. Perform a valid login
2. Check the products page

**Expected result:**  
Product list is displayed correctly with name, price, and “Add to cart” button.

**Status:** Passed

---

### TC-PROD-02 — Sort products by price (low to high)

**Steps:**
1. Be on the products page
2. Select sorting option “Price (low to high)”

**Expected result:**  
Products are correctly sorted by ascending price.

**Status:** Passed

---

## CART

### TC-CART-01 — Add product to cart

**Steps:**
1. Be logged in
2. Click “Add to cart” on a product
3. Access the cart

**Expected result:**  
Product appears in the cart.

**Status:** Passed

---

### TC-CART-02 — Remove product from cart

**Steps:**
1. Add a product to the cart
2. Access the cart
3. Click “Remove”

**Expected result:**  
Product is successfully removed.

**Status:** Passed

---

## CHECKOUT

### TC-CHK-01 — Complete checkout with valid data

**Test data:**
- First Name: John
- Last Name: Doe
- Zip Code: 12345

**Steps:**
1. Add a product to the cart
2. Click Checkout
3. Fill in valid data
4. Complete the purchase

**Expected result:**  
Purchase confirmation message.

**Status:** Passed

---

### TC-CHK-02 — Checkout with required fields empty

**Steps:**
1. Start checkout
2. Do not fill in the data
3. Click Continue

**Expected result:**  
Error message requesting completion of the required fields.

**Status:** Passed