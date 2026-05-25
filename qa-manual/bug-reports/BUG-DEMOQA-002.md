# Bug Report – DemoQA File Upload Button Has Poor Visibility

## Bug ID
BUG-DEMOQA-002

## Title
File upload button is too small and difficult to notice

**Detected during:** Exploratory Testing

## Application
DemoQA – Automation Practice Form

## Environment
- Platform: Web
- Browser: Chromium-based (Desktop)
- OS: Desktop (Linux)

## Severity
Low

## Priority
Low

## Description
The file upload button is displayed with very small dimensions, making it difficult for users to notice and identify it as an interactive element. This negatively impacts usability and discoverability of the file upload feature.

## Preconditions
- User is on the Automation Practice Form page

## Steps to Reproduce
1. Access https://demoqa.com/automation-practice-form
2. Scroll to the file upload section
3. Observe the file upload button

## Expected Result
The file upload button should be clearly visible, with sufficient size and contrast to indicate that it is a clickable element.

## Actual Result
The file upload button is very small and barely noticeable, making it hard to identify without prior knowledge.

## Evidence

**1. File upload button in page context**

![File upload button visibility](evidence/upload_button_context.png)

---

**2. Close-up of the file upload button**

![File upload button close-up](evidence/upload_button_closeup.png)

## Notes
Poor visibility of interactive elements may cause user confusion and reduce form completion rates, especially for less experienced users.