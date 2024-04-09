import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath","(//a[@class='dropdown-toggle'])[1]").click()
driver.find_element("xpath","//a[normalize-space()='Login']").click()
driver.find_element("xpath","//input[@id='input-email']").send_keys("jayjagannath@gmail.com")
driver.find_element("xpath","//input[@id='input-password']").send_keys("jayjagannath")
driver.find_element("xpath","//input[@value='Login']").click()


search_input = driver.find_element(By.NAME, "search")
search_input.send_keys("imac")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()
driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(1) .image").click()

# Get the price of the iMac
imac_price_str = driver.find_element(By.XPATH, "//span[@class='price-new']").text
print(imac_price_str)

# Add iMac to cart
driver.find_element(By.ID, "button-cart").click()
time.sleep(2)  # Wait for cart update

# Add 4 more items (assuming you navigate back to search page)
for _ in ["iphone","samsung","MacBook Air","MacBook Pro"]:
    driver.back()
    driver.find_element(By.NAME, "search").clear()
    driver.find_element(By.NAME, "search").send_keys(_)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()
    driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(1) .image").click()
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)  # Wait for cart update

# Go to shopping cart
driver.find_element(By.ID, "cart-total").click()
driver.find_element(By.XPATH, "//a[text()='View Cart']").click()
time.sleep(20)

# Remove all items except iMac
cart_items = driver.find_elements(By.CSS_SELECTOR, ".text-left .text-left a")
for item in cart_items:
    if "iMac" not in item.text:
        item.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
#
# # Checkout iMac
# driver.find_element(By.CSS_SELECTOR, ".fa.fa-shopping-cart").click()
# driver.find_element(By.XPATH, "//a[text()='View Cart']").click()
# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
#
# # Verify iMac price in checkout
# checkout_price_str = driver.find_element(By.CSS_SELECTOR,
#                                          ".table-bordered tbody tr:nth-child(2) td:nth-child(2)").text
# checkout_price = float(checkout_price_str.split("$")[-1])
# assert imac_price == checkout_price, f"iMac price mismatch: Expected {imac_price}, Actual {checkout_price}"
#
# # Confirm checkout
# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
# success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
# assert "Your order has been placed!" in success_message, "Checkout unsuccessful"
#
