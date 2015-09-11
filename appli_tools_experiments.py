from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.by import By

eyes = Eyes()
# This is your api key, make sure you use it in all your tests.
eyes.api_key = '3Z1sOfalzP1QClQrzmHJaU5BbKiR0AFZlDsBPoVB3Uk110'

# Get a selenium web driver object.
driver = webdriver.Firefox()

xpaths = {'first_available_region': '/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/ul/li[1]/div[1]',
          'first_available_sector': '/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div[2]/ul/a[5]'
          }

try:
    # Start visual testing with browser viewport set to 1024x768.
    # Make sure to use the returned driver from this point on.
    driver = eyes.open(driver=driver, app_name='Applitools', test_name='Test Web Page',
                       viewport_size={'width': 1024, 'height': 768})
    driver.get('http://climbing-guide.net')

    # Visual validation point #1
    eyes.check_window('Main Page')

    driver.find_element_by_xpath(xpaths['first_available_region']).click()
    driver.find_element_by_xpath(xpaths['first_available_sector']).click()

    # Visual validation point #2
    eyes.check_window('Booki Central sector details page')

    # End visual testing. Validate visual correctness.
    eyes.close()
finally:
    driver.quit()
    eyes.abort_if_not_closed()
