from os import getcwd
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

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
	
	# vehicle form
	car_year = "2015"
	car_make = "Acura"
	car_model = "RDX"
	car_odo = "100-999 miles"
	car_own = "Owned"
	car_business = "Pleasure"
	car_mileage = "12,000 - 12,999"

	# driver form
	driver_marital = "Single"
	driver_current_insurance = "No, I haven't needed insurance"
	driver_age = "16"
	driver_study = 'Graduate Student'

	# contact
	email = "chen@gmail.com"

	return zipcode,	firstName, lastName, street, apt, month_dob, day_dob, year_dob,car_year, \
	car_make, car_model, car_odo, car_own, car_business, car_mileage, driver_marital , \
	driver_current_insurance, driver_age ,driver_study , email

def auto_search(browser):
	wait = WebDriverWait(browser, 10)

	zipcode, firstName, lastName, street, apt, month_dob, day_dob, year_dob,car_year, car_make, car_model, car_odo, \
	car_own, car_business, car_mileage, driver_marital , driver_current_insurance, driver_age ,driver_study , email \
	= read_input()

	browser.get("https://sales2.geico.com/internetsales/iSnapPreQuote.xhtml?execution=e1s1&pg=iSnapCustomer")

	# customer
	wait.until(EC.element_to_be_clickable((By.ID,"CustomerForm:firstName")))
	browser.find_element_by_name("CustomerForm:firstName").send_keys(firstName)
	browser.find_element_by_name("CustomerForm:lastName").send_keys(lastName)
	browser.find_element_by_name("CustomerForm:customerMailingAddress").send_keys(street)
	browser.find_element_by_name("CustomerForm:unitNumber").send_keys(apt)
	browser.find_element_by_name("CustomerForm:mailingZip").send_keys(zipcode)
	browser.find_element_by_name("CustomerForm:birthMonth").send_keys(month_dob)
	browser.find_element_by_name("CustomerForm:birthDay").send_keys(day_dob)
	browser.find_element_by_name("CustomerForm:birthYear").send_keys(year_dob)
	browser.find_element_by_id("CustomerForm:continueBtn").click()

	# recall previous quote
	wait.until(EC.element_to_be_clickable((By.ID,"ProactiveCustomerIdentityForm:forgotPassword")))
	browser.find_element_by_id("ProactiveCustomerIdentityForm:forgotPassword").click()

	# vehicle
	sleep(3)
	Select(browser.find_element_by_id("VehicleForm:year")).select_by_visible_text(car_year)
	Select(browser.find_element_by_id("VehicleForm:year")).select_by_visible_text(car_year)
	wait.until(EC.element_to_be_clickable((By.ID,"VehicleForm:make")))
	Select(browser.find_element_by_id("VehicleForm:make")).select_by_visible_text(car_make)
	Select(browser.find_element_by_id("VehicleForm:make")).select_by_visible_text(car_make)
	wait.until(EC.element_to_be_clickable((By.ID,"VehicleForm:model")))
	Select(browser.find_element_by_id("VehicleForm:model")).select_by_visible_text(car_model)
	Select(browser.find_element_by_id("VehicleForm:model")).select_by_visible_text(car_model)
	Select(browser.find_element_by_id("VehicleForm:odometerReading")).select_by_visible_text(car_odo)
	Select(browser.find_element_by_id("VehicleForm:odometerReading")).select_by_visible_text(car_odo)
	Select(browser.find_element_by_id("VehicleForm:ownership")).select_by_visible_text(car_own)
	Select(browser.find_element_by_id("VehicleForm:ownership")).select_by_visible_text(car_own)
	Select(browser.find_element_by_id("VehicleForm:otherBusiness")).select_by_visible_text(car_business)
	Select(browser.find_element_by_id("VehicleForm:otherBusiness")).select_by_visible_text(car_business)
	wait.until(EC.element_to_be_clickable((By.ID,"VehicleForm:estimatedMileage")))
	Select(browser.find_element_by_id("VehicleForm:estimatedMileage")).select_by_visible_text(car_mileage)
	#Select(browser.find_element_by_id("VehicleForm:estimatedMileage")).select_by_visible_text(car_mileage)
	browser.find_element_by_id("VehicleForm:addNo").click()

	# driver
	wait.until(EC.element_to_be_clickable((By.ID,"DriverForm:maritalStatus")))
	Select(browser.find_element_by_id("DriverForm:maritalStatus")).select_by_visible_text(driver_marital)
	Select(browser.find_element_by_id("DriverForm:maritalStatus")).select_by_visible_text(driver_marital)
	browser.find_element_by_id("DriverForm:gender:1").click()
	browser.find_element_by_id("DriverForm:gender:1").click()
	wait.until(EC.element_to_be_clickable((By.ID,"DriverForm:curInsComp")))
	Select(browser.find_element_by_id("DriverForm:curInsComp")).select_by_visible_text(driver_current_insurance)
	Select(browser.find_element_by_id("DriverForm:curInsComp")).select_by_visible_text(driver_current_insurance)
	browser.find_element_by_id("DriverForm:firstUSLicenseAge").send_keys(driver_age)
	browser.find_element_by_id("DriverForm:fulltimeStudent:1").click()
	browser.find_element_by_id("DriverForm:fulltimeStudent:1").click()
	# sleep(1)
	browser.find_element_by_id("DriverForm:fulltimeStudent:0").click()
	#browser.find_element_by_id("DriverForm:fulltimeStudent:0").click()
	sleep(3)
	browser.find_element_by_id("DriverForm:fulltimeStudent:1").click()
	browser.find_element_by_id("DriverForm:fulltimeStudent:1").click()
	sleep(3)
	wait.until(EC.element_to_be_clickable((By.ID,"DriverForm:currentYearOfStudy")))
	Select(browser.find_element_by_id('DriverForm:currentYearOfStudy')).select_by_visible_text(driver_study)
	Select(browser.find_element_by_id('DriverForm:currentYearOfStudy')).select_by_visible_text(driver_study)
	browser.find_element_by_id("DriverForm:addNo").click()

	# driving history
	wait.until(EC.element_to_be_clickable((By.ID,"DriHisForm:select:1")))
	browser.find_element_by_id("DriHisForm:select:1").click()
	browser.find_element_by_id("DriHisForm:continueBtn").click()
	browser.find_element_by_id("DiscountsForm:emailAddress").send_keys(email)
	browser.find_element_by_id("DiscountsForm:continueBtn").click()
	# quote price
	price=browser.find_element(By.CLASS_NAME, "price")
	qt = str(price.text)
	quote = qt.strip("$")
	browser.close()
	return quote

def run(browser_name):
	browser_path = getcwd()

	# browser
	if browser_name == 'FIREFOX':
		browser = webdriver.Firefox()
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
