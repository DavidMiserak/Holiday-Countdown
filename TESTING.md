# Behavior-Driven Development (BDD) Testing Guide

## Overview

This project uses Behave for Behavior-Driven Development (BDD) testing. BDD allows us to describe application behavior in a human-readable format using Gherkin syntax.

## Test Features

Our BDD tests cover the following scenarios:

### 1. Add Birthday
- Verify successful addition of a new birthday
- Validate input fields and success message
- Confirm birthday appears in the list

### 2. Edit Birthday
- Edit existing birthday details
- Update name and date
- Verify changes are reflected in the list

### 3. Delete Birthday
- Remove a birthday from the list
- Confirm deletion through user confirmation
- Validate birthday is no longer displayed

### 4. View Birthdays
- Display list of birthdays
- Verify countdown timers are present
- Check empty list handling

## Prerequisites

- Python 3.9+
- Firefox ESR
- GeckoDriver
- All dependencies in `requirements.txt`

## Setup for Testing

1. Install Firefox ESR
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get update
     sudo apt-get install firefox-esr
     ```
   - On macOS (with Homebrew):
     ```bash
     brew install firefox-esr
     ```
   - On Windows: Download from Mozilla Firefox website

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### WebDriver Configuration

The tests use Firefox in headless mode with GeckoDriver. WebDriver is automatically managed via `webdriver-manager`.

## Running Tests

### Manual Test Execution

1. Start the application:
   ```bash
   python run.py
   ```

2. Run Behave tests:
   ```bash
   behave tests/
   ```

### Pre-Commit Hook Tests

Tests will automatically run during pre-commit:
- Triggered before each commit
- Prevents committing if tests fail

## Test Configuration

- **Features**: Located in `tests/features/`
- **Step Definitions**: `tests/steps/birthday_steps.py`
- **Environment Setup**: `tests/environment.py`

## Troubleshooting

- Ensure Chrome is installed
- Check WebDriver compatibility
- Verify application is running on `localhost:5000`

## Writing New Tests

1. Create a new `.feature` file in `tests/features/`
2. Write scenarios using Gherkin syntax
3. Implement corresponding step definitions in `tests/steps/`

## Best Practices

- Keep scenarios concise and focused
- Use descriptive scenario names
- Cover both positive and negative test cases
