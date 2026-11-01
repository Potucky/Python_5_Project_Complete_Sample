# eBay Header Navigation Tests (Behave + Selenium)

A BDD practice project that uses Python, Selenium WebDriver, and Behave to check navigation links in the eBay homepage header.

## What it tests

`features/scenario.feature` contains six scenarios, each opening the eBay homepage, clicking a header link, and verifying the page title:

- Daily Deals
- Brand Outlet
- Gift Cards
- Sell
- Sign in / Register
- Help & Contact

## Project Structure

```text
├── requirements.txt
├── README.md
└── features/
    ├── environment.py      # Browser setup and teardown (Chrome)
    ├── scenario.feature    # Gherkin scenarios
    └── steps/
        └── eBay.py         # Step definitions
```

## Getting Started

1. Install Python 3.10 or higher and Google Chrome.
2. Clone or download the project.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the scenarios from the project root with the standard Behave command:

```bash
behave
```

## Notes

- The tests run against the live eBay website, so results depend on the current page layout and link text.
- `requirements.txt` pins behave, selenium, webdriver-manager, colorama, loguru, pytest, pytest-html, and requests.
- This is a learning project, not a complete test suite.
