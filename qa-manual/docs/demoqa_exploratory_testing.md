# Exploratory Testing – DemoQA Practice Form

## Session Objective
Explore form behavior by interacting with different input combinations, edge cases, and validation rules.

## Approach
The form was tested without predefined scripts, focusing on field validations, user input handling, and submission behavior.

## Areas Explored
- Required fields validation
- Invalid email formats
- Mobile number input validation
- Boundary values and empty submissions
- Form submission behavior

## Observations
- Required fields are enforced
- Invalid email formats are rejected
- Form submission succeeds only when mandatory fields are correctly filled
- The file upload button is very small and poorly visible, which may impact usability and accessibility.

## Risks & Limitations
- Limited validation feedback for some fields
- Some invalid inputs are accepted due to demo application constraints

## Conclusion
Exploratory testing confirmed that core validation rules work as expected, while also revealing limitations in feedback clarity for certain inputs.