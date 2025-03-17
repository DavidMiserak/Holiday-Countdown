#!/usr/bin/env python

"""
Environment for Behave Testing
"""

import os
import sys
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Ensure proper logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("behave_debug.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("behave_tests")


def create_webdriver():
    """Create and configure WebDriver"""
    try:
        # Configure Firefox options
        firefox_options = Options()
        # Uncomment to run in headless mode if needed
        firefox_options.add_argument("-headless")

        # Use the known GeckoDriver path
        service_path = "/usr/bin/geckodriver"

        # Setup Firefox WebDriver
        service = Service(service_path)
        driver = webdriver.Firefox(service=service, options=firefox_options)

        # Set implicit wait
        driver.implicitly_wait(10)

        logger.info("WebDriver created successfully")
        return driver
    except Exception as e:
        logger.error(f"Failed to create WebDriver: {e}")
        raise


def before_all(context):
    """Setup before all scenarios"""
    logger.info("Configuring Behave context")
    context.base_url = "http://localhost:5000"


def before_scenario(context, scenario):
    """Setup before each scenario"""
    try:
        # Ensure any existing driver is closed
        if hasattr(context, "driver"):
            try:
                context.driver.quit()
            except:
                pass

        # Create new driver for the scenario
        context.driver = create_webdriver()

        # Navigate to base URL
        context.driver.get(context.base_url)
        logger.info(f"Navigated to {context.base_url}")
    except Exception as e:
        logger.error(f"Scenario setup failed: {e}")
        raise


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    try:
        # Take screenshot on failure
        if scenario.status == "failed":
            # Ensure screenshots directory exists
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{scenario.name}.png"

            try:
                context.driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot saved to {screenshot_path}")
            except Exception as screenshot_error:
                logger.error(f"Failed to save screenshot: {screenshot_error}")
    except Exception as e:
        logger.error(f"After scenario cleanup failed: {e}")

    # Always close the driver
    try:
        if hasattr(context, "driver"):
            context.driver.quit()
            del context.driver
    except Exception as e:
        logger.error(f"Driver cleanup failed: {e}")


def after_all(context):
    """Final cleanup"""
    logger.info("Behave test run completed")
