from behave import step, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ======= HOOKS ==
def before_all(context):
    print("🚀 Launching browser")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    print("🛑 Closing browser")
    context.driver.quit()

# ======= STEP: Open eBay homepage =======
@step('I Navigate to eBay')
def navigate_ebay(context):
    context.driver.get("https://www.ebay.com")
    print("🌐 Navigated to https://www.ebay.com")

# ======= Daily Deals =======
@step('I click on Daily Deals')
def click_daily(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daily Deals"))
        ).click()
        print("🛍 Clicked on Daily Deals")
        time.sleep(2)
    except TimeoutException:
        print("❌ Daily Deals button not found")
        raise

@step('verify Daily Deals page loaded')
def verify_daily(context):
    WebDriverWait(context.driver, 15).until(EC.title_contains("Daily Deals"))
    print(f"✅ Daily Deals page loaded: {context.driver.title}")

# ======= Brand Outlet =======
@step('I click on Brand Outlet')
def click_brand(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Brand Outlet"))
        ).click()
        print("👕 Clicked on Brand Outlet")
        time.sleep(2)
    except TimeoutException:
        print("❌ Brand Outlet button not found")
        raise

@step('verify Brand Outlet page loaded')
def verify_brand(context):
    WebDriverWait(context.driver, 15).until(EC.title_contains("Brand Outlet"))
    print(f"✅ Brand Outlet page loaded: {context.driver.title}")

# ======= Gift Cards =======
@step('I click on Gift Cards')
def click_gift(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Gift Cards"))
        ).click()
        print("🎁 Clicked on Gift Cards")
        time.sleep(2)
    except TimeoutException:
        print("❌ Gift Cards button not found")
        raise

@step('verify Gift Cards page loaded')
def verify_gift(context):
    WebDriverWait(context.driver, 15).until(EC.title_contains("Gift Cards"))
    print(f"✅ Gift Cards page loaded: {context.driver.title}")

# ======= Sell =======
@step('I click on Sell')
def click_sell(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sell"))
        ).click()
        print("💼 Clicked on Sell")
        time.sleep(2)
    except TimeoutException:
        print("❌ Sell button not found")
        raise

@step('verify Sell page loaded')
def verify_sell(context):
    WebDriverWait(context.driver, 15).until(EC.title_contains("Sell"))
    print(f"✅ Sell page loaded: {context.driver.title}")

# ======= Sign in =======
@step('I click on Sign in or Register')
def click_signin(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        ).click()
        print("🔐 Clicked on Sign in")
        time.sleep(2)
    except TimeoutException:
        print("❌ Sign in button not found")
        raise

@step('verify Sign in page loaded')
def verify_signin(context):
    WebDriverWait(context.driver, 15).until(EC.title_contains("Sign in"))
    print(f"✅ Sign in page loaded: {context.driver.title}")

# ======= Help & Contact =======
@step('I click on Help & Contact')
def click_help(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Help & Contact"))
        ).click()
        print("❓ Clicked on Help & Contact")
        time.sleep(2)
    except TimeoutException:
        print("❌ Help & Contact button not found")
        raise

@step('verify Help & Contact page loaded')
def verify_help(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.title_contains("Customer Service")
        )
        print(f"✅ Help & Contact page loaded: {context.driver.title}")
    except TimeoutException:
        print(f"❌ Help & Contact page not loaded. Current title: {context.driver.title}")
        raise
