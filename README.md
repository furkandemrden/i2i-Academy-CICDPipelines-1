# Telecom Tax Calculator — CI/CD Pipeline Demo

A small Python project demonstrating a CI/CD pipeline with GitHub Actions.

## What it does

- `app.py` — calculates the final payable amount for a telecom service after VAT + telecom tax.
- `test_app.py` — a pytest unit test for `app.py`.
- `test_ui.py` — a headless Selenium UI test that verifies `https://example.com` loads correctly.
- `.github/workflows/ci-cd.yml` — GitHub Actions workflow triggered on every push:
  1. Sets up Python and installs dependencies
  2. Runs the unit test
  3. Runs the headless Selenium UI test
  4. If both pass, prints a deployment confirmation message

## Run locally

```bash
pip install -r requirements.txt
pytest test_app.py -v
pytest test_ui.py -v
```
