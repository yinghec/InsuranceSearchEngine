from os import getcwd
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def read_input():
# 	# customer
# 	zipcode = str(raw_input("\nEnter zipcode:  "))
# 	firstName = str(raw_input("\nEnter first name: "))
# 	lastName = str(raw_input("\nEnter last name: "))
# 	street = str(raw_input("\nEnter street address: "))
# 	apt = str(raw_input("\nEnter apartment number: "))
# 	birthday = str(raw_input("\nEnter birthday (yyyy-mm-dd): "))
# 	month_dob = birthday.split("-")[1]
# 	day_dob = birthday.split("-")[2]
# 	year_dob = birthday.split("-")[0]
# 	ssn = str(raw_input("\nEnter social security number (XXX-XX-XXXX): "))
# 	# ssn1 = ssn.split("-")[0]
# 	# ssn2 = ssn.split("-")[1]
# 	# ssn3 = ssn.split("-")[2]
	
# 	car_year = str(raw_input("\nEnter year of vehicle:  "))
# 	car_make = str(raw_input("\nEnter make of vehicle:  "))
# 	car_model = str(raw_input("\nEnter vehicle model:  "))
# 	car_odo = str(raw_input("\nEnter vehicle odometer reading:  "))
# 	car_own = str(raw_input("\nEnter vehicle ownership:  "))
# 	car_business = str(raw_input("\nEnter the primary use of the vehicle:  "))
# 	car_mileage = str(raw_input("\nEnter vehicle mileage:  "))

# 	# driver form
# 	driver_marital = str(raw_input("\nEnter driver marital status:  "))
# 	driver_current_insurance = str(raw_input("\nEnter driver current insurance status:  "))
# 	driver_age = str(raw_input("\nEnter driver age of getting driver license:  "))
# 	driver_study = str(raw_input("\nEnter driver current study status:  "))

# 	# contact
# 	email = str(raw_input("\nEnter email address: "))

	# customer form
	firstName = "Yin"
	lastName = "Chen"
	
	street = "4340 8th Ave NE"
	apt = "700"
	zipcode = "98105"
	month_dob = "10"
	day_dob = "10"
	year_dob = "1990"
	city = "seattle"
	# vehicle form
	car_year = "2015"
	car_make = "ACURA"
	car_model = "RDX"
	car_odo = "100-999 miles"
	car_own = "Own and do not make payments"
	car_business = "Pleasure (recreational driving only)"
	car_mileage = "12,000 - 12,999"

	# driver form
	driver_marital = "Single"
	driver_current_insurance = "No, I haven't needed insurance"
	driver_age = "16"
	driver_study = 'Graduate Student'

	# contact
	email = "chen@gmail.com"
	car_bodyType = "AWD 4D GAS"

	return zipcode,	firstName, lastName, street, apt, month_dob, day_dob, year_dob,car_year, \
	car_make, car_model, car_odo, car_own, car_business, car_mileage, driver_marital , \
	driver_current_insurance, driver_age ,driver_study , email, car_bodyType, city

def auto_search(browser):
	wait = WebDriverWait(browser, 10)

	zipcode, firstName, lastName, street, apt, month_dob, day_dob, year_dob,car_year, car_make, car_model, car_odo, \
	car_own, car_business, car_mileage, driver_marital , driver_current_insurance, driver_age ,driver_study , email, \
	car_bodyType, city = read_input()

	browser.get("https://www.statefarm.com/")
	#browser.maximize_window()

	# customer
	wait.until(EC.element_to_be_clickable((By.ID,"sZip")))
	browser.find_element_by_id("sZip").send_keys(zipcode)
	browser.find_element_by_id("getAQuoteGo").click()
	wait.until(EC.element_to_be_clickable((By.ID, "driver1FirstName-sfxid_4")))
	browser.find_element_by_id("driver1FirstName-sfxid_4").send_keys(firstName)
	browser.find_element_by_id("driver1LastName-sfxid_6").send_keys(lastName)
	browser.find_element_by_id("street1-sfxid_8").send_keys(street)
	browser.find_element_by_id("street2-sfxid_9").send_keys(apt)
	browser.find_element_by_name("driver1DateOfBirth__1").send_keys(month_dob)
	browser.find_element_by_name("driver1DateOfBirth__2").send_keys(day_dob)
	browser.find_element_by_name("driver1DateOfBirth__3").send_keys(year_dob)
	#browser.find_element_by_name("NameAndAddressFormModel.City.Value").send_keys(city)
	browser.find_element_by_id("continueButtonBtnWrpr").click()
	wait.until(EC.element_to_be_clickable((By.ID, "showYmmbBtnId")))
	browser.find_element_by_id("showYmmbBtnId").click()
	wait.until(EC.element_to_be_clickable((By.ID, "ymmbYearId-sfxid_22")))
	Select(browser.find_element_by_id("ymmbYearId-sfxid_22")).select_by_visible_text(car_year)
	sleep(2)
	Select(browser.find_element_by_id("ymmbMakeId-sfxid_23")).select_by_visible_text(car_make)
	sleep(2)
	Select(browser.find_element_by_id("ymmbModelId-sfxid_24")).select_by_visible_text(car_model)
	sleep(2)
	Select(browser.find_element_by_id("ymmbBodyStyleId-sfxid_25")).select_by_visible_text(car_bodyType)
	browser.find_element_by_id("ymmbModuleFooterBtn").click()
	browser.find_element_by_class_name("sfx_text sfx_label sfx_radio sfx_radio_checked").click()
	#wait.until()
	# recall previous quote
	#wait.until(EC.element_to_be_clickable((By.ID,"ProactiveCustomerIdentityForm:forgotPassword")))
	#browser.find_element_by_id("ProactiveCustomerIdentityForm:forgotPassword").click()

	# vehicle
	sleep(4)
	#wait.until(EC.element_to_be_selected((By.ID,"UnlistedVehicleFormModel_Year_Value")))
	#sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_Year_Value")).select_by_visible_text(car_year)
	#wait.until(EC.element_to_be_clickable((By.ID, "UnlistedVehicleFormModel_Make_Value")))
	sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_Make_Value")).select_by_visible_text(car_make)
	#wait.until(EC.element_to_be_clickable((By.ID, "UnlistedVehicleFormModel_Model_Value")))
	sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_Model_Value")).select_by_visible_text(car_model)
	#wait.until(EC.element_to_be_clickable((By.ID, "UnlistedVehicleFormModel_BodyStyle_Value")))
	sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_BodyStyle_Value")).select_by_visible_text(car_bodyType)
	#wait.until(EC.element_to_be_clickable((By.ID, "UnlistedVehicleFormModel_VehicleUse_Value")))
	sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_VehicleUse_Value")).select_by_visible_text(car_business)
	#wait.until(EC.element_to_be_clickable((By.ID, "UnlistedVehicleFormModel_OwnOrLease_Value")))
	sleep(2)
	Select(browser.find_element_by_id("UnlistedVehicleFormModel_OwnOrLease_Value")).select_by_visible_text(car_own)
	#browser.execute_script("window.scrollTo(0, 500);")
	wait.until(EC.element_to_be_clickable((By.ID, "next")))
	#wait.until(EC.visibility_of(By.ID, "next"))
	target = browser.find_element_by_id("next")
	#hover = WebDriverWait(browser,5,poll_frequency=.2).until(EC.visibility_of(target))
	#target.click()
	#ActionChains(browser).move_to_element(target).click().perform()
	#action(webdriver).move_to_element_with_offset(link,0,20).click().perform();
	browser.find_element(By.ID, "next").click()
	#sleep(100)
	# quote price

	#price=browser.find_element(By.CLASS_NAME, "price")
	#qt = str(price.text)
	#quote = qt.strip("$")
	browser.close()
	#return quote


def run(browser_name):
	browser_path = getcwd()

	# browser
	if browser_name == 'FIREFOX':
		browser = webdriver.Firefox('')
	elif browser_name == 'CHROME':	
		co = webdriver.ChromeOptions()
		co.add_argument("disable-extensions")
		browser = webdriver.Chrome('/Users/YC/Desktop/chromedriver', chrome_options=co)
	elif browser_name == 'IE':
		capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
		capabilities['acceptSslCerts'] = True
		capabilities['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS']=True
		capabilities['ignoreProtectedModeSettings'] = True
		browser = webdriver.Ie(capabilities=capabilities)
	elif browser_name == 'PHANTOMJS':
		browser = webdriver.PhantomJS('/Users/YC/Desktop/phantomjs')

	# print results
	quote = auto_search(browser)
	print "\nLowest Quote is: "+ "$"+str(quote)

if __name__ == "__main__":	
	t0 = time()
	run('CHROME')
	#run('PHANTOMJS')
	print "\nRunning Time: "+ str(time() - t0) + "s"
