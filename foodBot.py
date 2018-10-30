from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

udcc = "https://www.dining.iastate.edu/location/union-drive-marketplace-2-2/"
convos = "https://www.dining.iastate.edu/location/conversations-2/"
windows = "https://www.dining.iastate.edu/location/friley-windows-2-2/"
seasons = "https://www.dining.iastate.edu/location/seasons-marketplace-2-2/"
storms = "https://www.dining.iastate.edu/location/storms-dining/"

url_list = [ udcc, convos, windows, seasons, storms ]
for url_item in url_list:
	driver = webdriver.Chrome()
	driver.get(url_item)
	try:
    	 WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'mh-location--menus')))
	except TimeoutException:
    	 print('No menus today.')
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	driver.quit()

	containers = soup.findAll("li",{"class":"mh-location--single-menu--item"})
	food_list = []
	for menu in containers:
		food = menu.find("span",{"class":"mh-menu-item-name"}).text

		for item in food_list:
			if food == item:
				food_list.remove(item)

		if food.find("Pancake") > 0: 
			food_list.append(food)
		if food.find("Eggs") > 0: 
			food_list.append(food)
		if food.find("Wings") > 0: 
			food_list.append(food)
		if food.find("Burger") > 0:
			food_list.append(food)
		if food.find("Fries") > 0:
			food_list.append(food)
		if food.find("Pizza") > 0:
			food_list.append(food)
		if food.find("Home") > 0:
			food_list.append(food)
		if food.find("Toast") > 0:
			food_list.append(food)


	print( "Dining Hall: " + soup.find("div",{"class":"mh-location--header"}).h1.text)
	for item in food_list:
		print( "	" + item + "\n")
	#print( food_list )
