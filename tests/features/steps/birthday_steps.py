#!/usr/bin/env python

import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("step_debug.log"), logging.StreamHandler()],
)
logger = logging.getLogger("birthday_steps")


def safe_wait_and_find(driver, locator, timeout=10):
    """Safely wait for and find an element"""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except Exception as e:
        logger.error(f"Element not found: {locator}")
        raise


# Add Birthday Feature Steps
@given("the user is on the add birthday page")
def step_goto_add_birthday_page(context):
    context.driver.get(f"{context.base_url}/add")
    logger.info("Navigated to add birthday page")


@when('the user enters name "{name}"')
def step_enter_name(context, name):
    name_input = safe_wait_and_find(context.driver, (By.ID, "name"))
    name_input.clear()
    name_input.send_keys(name)
    logger.info(f"Entered name: {name}")


@when('the user enters birthday "{birthday}"')
def step_enter_birthday(context, birthday):
    date_input = safe_wait_and_find(context.driver, (By.ID, "date"))
    date_input.clear()
    date_input.send_keys(birthday)
    logger.info(f"Entered birthday: {birthday}")


@when('the user clicks the "{button_text}" button')
def step_click_button(context, button_text):
    button = safe_wait_and_find(
        context.driver, (By.XPATH, f"//button[contains(text(), '{button_text}')]")
    )
    button.click()
    logger.info(f"Clicked button: {button_text}")


@then("the user should see a success message")
def step_verify_success_message(context):
    success_message = safe_wait_and_find(
        context.driver, (By.CLASS_NAME, "alert-success")
    )
    assert success_message.is_displayed(), "Success message not found"
    logger.info("Success message verified")


@then('the birthday for "{name}" should be in the birthday list')
def step_verify_birthday_in_list(context, name):
    birthday_list = safe_wait_and_find(
        context.driver, (By.CLASS_NAME, "list-group-item")
    )
    birthdays = context.driver.find_elements(By.CLASS_NAME, "list-group-item")

    birthday_found = any(name in birthday.text for birthday in birthdays)
    assert birthday_found, f"Birthday for {name} not found in the list"
    logger.info(f"Birthday for {name} found in list")


# Delete Birthday Feature Steps
@given('a birthday for "{name}" exists')
def step_create_birthday(context, name):
    context.driver.get(f"{context.base_url}/add")

    # Enter name
    name_input = safe_wait_and_find(context.driver, (By.ID, "name"))
    name_input.send_keys(name)

    # Enter a default birthday
    date_input = safe_wait_and_find(context.driver, (By.ID, "date"))
    date_input.send_keys("1990-01-01")

    # Submit the birthday
    submit_button = safe_wait_and_find(
        context.driver, (By.XPATH, "//button[contains(text(), 'Add Birthday')]")
    )
    submit_button.click()
    logger.info(f"Created birthday for {name}")


@when('the user clicks the delete button for "{name}"')
def step_click_delete_button(context, name):
    birthdays = context.driver.find_elements(By.CLASS_NAME, "list-group-item")
    for item in birthdays:
        if name in item.text:
            delete_button = item.find_element(
                By.XPATH, ".//button[contains(@class, 'btn-outline-danger')]"
            )
            delete_button.click()
            logger.info(f"Clicked delete for {name}")
            return

    raise AssertionError(f"Could not find birthday for {name}")


@when("confirms the deletion")
def step_confirm_deletion(context):
    # Handle browser confirmation dialog
    context.driver.switch_to.alert.accept()
    logger.info("Confirmed deletion")


@then('the birthday for "{name}" should be removed from the list')
def step_verify_birthday_removed(context, name):
    birthdays = context.driver.find_elements(By.CLASS_NAME, "list-group-item")
    birthday_found = any(name in birthday.text for birthday in birthdays)
    assert not birthday_found, f"Birthday for {name} was not removed from the list"
    logger.info(f"Birthday for {name} successfully removed")


# Edit Birthday Feature Steps
@when('the user clicks the edit button for "{name}"')
def step_click_edit_button(context, name):
    birthdays = context.driver.find_elements(By.CLASS_NAME, "list-group-item")
    for item in birthdays:
        if name in item.text:
            edit_button = item.find_element(
                By.XPATH, ".//a[contains(@class, 'btn-outline-primary')]"
            )
            edit_button.click()
            logger.info(f"Clicked edit for {name}")
            return

    raise AssertionError(f"Could not find birthday for {name}")


@when('changes the name to "{new_name}"')
def step_change_name(context, new_name):
    name_input = safe_wait_and_find(context.driver, (By.ID, "name"))
    name_input.clear()
    name_input.send_keys(new_name)
    logger.info(f"Changed name to {new_name}")


@when('changes the birthday to "{new_birthday}"')
def step_change_birthday(context, new_birthday):
    date_input = safe_wait_and_find(context.driver, (By.ID, "date"))
    date_input.clear()
    date_input.send_keys(new_birthday)
    logger.info(f"Changed birthday to {new_birthday}")


# View Birthday Feature Steps
@given("some birthdays have been added")
def step_add_some_birthdays(context):
    birthdays = [
        {"name": "John Doe", "date": "1990-05-15"},
        {"name": "Jane Smith", "date": "1985-12-25"},
    ]

    for birthday in birthdays:
        context.driver.get(f"{context.base_url}/add")

        name_input = safe_wait_and_find(context.driver, (By.ID, "name"))
        name_input.send_keys(birthday["name"])

        date_input = safe_wait_and_find(context.driver, (By.ID, "date"))
        date_input.send_keys(birthday["date"])

        submit_button = safe_wait_and_find(
            context.driver, (By.XPATH, "//button[contains(text(), 'Add Birthday')]")
        )
        submit_button.click()

    logger.info("Added multiple birthdays")


@when("the user navigates to the home page")
def step_navigate_home(context):
    context.driver.get(context.base_url)
    logger.info("Navigated to home page")


@then("the user should see a list of birthdays")
def step_verify_birthday_list(context):
    birthdays = context.driver.find_elements(By.CLASS_NAME, "list-group-item")
    assert len(birthdays) > 0, "No birthdays found in the list"
    logger.info("Birthday list verified")


@then("each birthday should display a countdown timer")
def step_verify_countdown_timers(context):
    countdown_timers = context.driver.find_elements(By.CLASS_NAME, "countdown-timer")
    assert len(countdown_timers) > 0, "No countdown timers found"

    for timer in countdown_timers:
        assert "Next birthday in:" in timer.text, "Invalid countdown timer text"

    logger.info("Countdown timers verified")


@given("no birthdays have been added")
def step_clear_birthdays(context):
    # For a real application, this would typically require a backend method
    # Here we just ensure we're on the home page
    context.driver.get(context.base_url)
    logger.info("Ensured no birthdays on home page")


@then("the user should see a message suggesting to add a birthday")
def step_verify_empty_list_message(context):
    empty_messages = context.driver.find_elements(By.CLASS_NAME, "alert-info")
    assert len(empty_messages) > 0, "No 'add birthday' message found"
    assert "No birthdays added yet" in empty_messages[0].text
    logger.info("Empty list message verified")
