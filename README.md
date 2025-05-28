# Odoo Intern Technical Challenge

## Part 1: Python

**Instructions:**

Implement two classes:

1. `Product`:
    - Constructor takes `name` (string) and `price` (float).
    - Method `get_discounted_price(discount_rate)` returns the price after applying the given discount rate (e.g., 0.2 for 20% off), rounded to 2 decimals.

2. `DigitalProduct` (inherits from `Product`):
    - Overrides `get_discounted_price()` (no arguments) to always return the price with a fixed 20% discount, rounded to 2 decimals.

Write your solution in `exercises/python_exercise.py`.

## Part 2: XML / XPath Script

**Instructions:**

Implement a function named `modify_xml` that:

1. Parses the XML file `input_form.xml` (provided in this directory).
2. Locates the `<field name="author"/>` element and moves it to be the first child of the root `<form>` element.
3. Adds a new `<section>` element with the text "Details" after the fields.
4. Adds a `<button>` element with the attribute `name="toggle_availability"` after the section.
5. Outputs the modified XML as `output_form.xml`.

Write your solution in `exercises/xpath_exercise.py`.
The input XML is provided as `exercises/input_form.xml`.

## Testing Your Solution

You are encouraged to test your code locally before submitting. To do so, you can run the test scripts provided in the `tests/` directory:

```bash
python3 -m pytest tests
```

This will execute all available tests to help you verify your implementation.

## Evaluation Criteria
Your submission will be evaluated based on the following:
- **Correctness:** Does your code meet all requirements and pass all provided tests?
- **Code Quality:** Is your code clean, readable, and well-structured? Are best practices followed?
- **Completeness:** Have you implemented all requested features and handled edge cases?
- **Documentation:** Are your code and logic clear, with comments where appropriate?
- **Efficiency:** Is your solution efficient and free of unnecessary complexity?

## Submission Process
1. Push your changes to your repository.
2. Automated tests will run via GitHub Actions. You can check the status in the Actions tab of your repository.
3. Only submissions that pass all tests will be considered for review.
4. Ensure your commit history is clear and descriptive (use atomic and descriptive commits).

Good luck!