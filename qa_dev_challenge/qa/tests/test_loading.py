import pytest
from page_object.main_page import MainPage
from page_object.new_hotel_page import NewHotelPage
from mixin import *
import time


def test_verify_visibility_of_elements(browser):

	main_page = MainPage(browser)
	new_hotel_page = NewHotelPage(browser)
	
	main_page.visit()
	hover(browser, main_page.article_li)
	hover(browser, main_page.new_li)
	main_page.hotel_li.click()

	# Verify that Register new Hotel page is displayed when user selects Article->New->Hotel
	wait_presense_xpath(browser, '//h2[.="Register new Hotel"]')
	assert new_hotel_page.title_element.is_displayed()
	
	# Verify that Data section is displayed on Register new Hotel
	assert new_hotel_page.data_section_table_div.is_displayed()
	
	# Verify that save button is displayed on Register new Hotel
	assert new_hotel_page.save_button_element.is_displayed()
	
	# Verify that Name field is displayed in Data section of Register new Hotel page
	assert new_hotel_page.name_label_element.is_displayed()
	
	# Verify that Name field is marked with asterisk
	assert new_hotel_page.name_label_element.text[-1] == '*'
	
	# Verify that Global Rating field is displayed in Data section of Register new Hotel page
	assert new_hotel_page.name_global_rating_element.is_displayed()
	
	# Verify that Date of Construction field is displayed in Data section of Register new Hotel page
	assert new_hotel_page.date_element.is_displayed()
	
	# Verify that Date of Construction field is marked with asterisk
	assert new_hotel_page.date_element.text[-1] == '*'
	
	# Verify that Country field is displayed in Data section of Register new Hotel page
	assert new_hotel_page.country_element.is_displayed()
	
	# Verify that Country fields is marked with asterisk
	assert new_hotel_page.country_element.text[-1] == '*'
	
	# Verify that City field is displayed in Data section of Register new Hotel page
	assert new_hotel_page.city_element.is_displayed()
	
	# Verify that City field is marked with asterisk
	assert new_hotel_page.city_element.text[-1] == '*'
	
	# Verify that Short Description field is displayed in Data section of Register new Hotel
	assert new_hotel_page.short_desc_element.is_displayed()
	
	# Verify that Short Description field is marked with asterisk
	assert new_hotel_page.short_desc_element.text[-1] == '*'
	
	# Verify that Description field is displayed in Data section of Register new Hotel
	assert new_hotel_page.desc_element.is_displayed()
	
	# Verify that Description field is marked with asterisk
	assert new_hotel_page.desc_element.text[-1] == '*'
	
	# Verify that Notes field is displayed in Data section of Register new Hotel
	assert new_hotel_page.notes_element.is_displayed()


def test_warning_messages(browser):

	new_hotel_page = NewHotelPage(browser)
	invalid_date = '1212'

	new_hotel_page.visit()

	assert new_hotel_page.name_warning_element.is_displayed() == False
	assert new_hotel_page.date_warning_element.is_displayed() == False
	assert new_hotel_page.country_warning_element.is_displayed() == False
	assert new_hotel_page.city_warning_element.is_displayed() == False
	assert new_hotel_page.short_desc_warning_element.is_displayed() == False
	assert new_hotel_page.desc_warning_element.is_displayed() == False

	new_hotel_page.save_button_element.click()

	# Verify that it is not possible to save the empty Name field and a meaningful error message is displayed
	assert new_hotel_page.name_warning_element.is_displayed()
	assert new_hotel_page.name_warning_element.text == 'Name: Validation Error: Value is required.'
	
	# Verify that it is not possible to save the empty Date of Construction field and a meaningful error message is displayed
	assert new_hotel_page.date_warning_element.is_displayed()
	assert new_hotel_page.date_warning_element.text == 'Date of Construction: Validation Error: Value is required.'
	
	# Verify that it is not possible to save the empty (with default value “Select me’) Country field. And a meaningful error is displayed
	assert new_hotel_page.country_warning_element.is_displayed()
	assert new_hotel_page.country_warning_element.text == 'Country: Validation Error: Value is required.'
	
	# Verify that it is not possible to save the empty (with default value “Select me”) City field and a meaningful error message is displayed
	assert new_hotel_page.city_warning_element.is_displayed()
	assert new_hotel_page.city_warning_element.text == 'City: Validation Error: Value is required.'
	
	# Verify that it is not possible to save the empty Short Description field and a meaningful error message is displayed
	assert new_hotel_page.short_desc_warning_element.is_displayed()
	assert new_hotel_page.short_desc_warning_element.text == 'Short Description: Validation Error: Value is required.'
	
	# Verify that it is not possible to save the empty Description field and a meaningful error message is displayed
	assert new_hotel_page.desc_warning_element.is_displayed()
	assert new_hotel_page.desc_warning_element.text == 'Description: Validation Error: Value is required.'

	new_hotel_page.date_input_element.send_keys(invalid_date)
	new_hotel_page.save_button_element.click()	

	# Verify that it is not possible to save incorrect date format value Date of Construction field and a meaningful error message is displayed
	# assert new_hotel_page.date_warning_element.text == f"Date of Construction: '{invalid_date}' could not be understood as a date. Example: 5/28/19"


def test_fields_editing(browser):

	new_hotel_page = NewHotelPage(browser)
	valid_date = '5/28/19'
	alphanumeric_value = 'AwertyU123456'

	new_hotel_page.visit()

	# Verify that Name field is editable
	# Verify that Name field allows to input alphanumeric characters
	new_hotel_page.name_input_element.send_keys(alphanumeric_value)
	assert new_hotel_page.name_input_element.get_attribute('value') == alphanumeric_value
	
	# Verify that Date of Construction is editable
	# Verify Date of Construction field allows to input in date format
	new_hotel_page.date_input_element.send_keys(valid_date)
	assert new_hotel_page.date_input_element.get_attribute('value') == valid_date
	
	# Verify that Country field is editable
	new_hotel_page.country_dropdown_element.click()
	new_hotel_page.ukraine_element.click()
	assert new_hotel_page.country_dropdown_element.text == 'Ukraine'
	
	# Verify that City field is editable
	wait_presense_xpath(browser, '//label[@id="add_hotel:city_label"]')
	new_hotel_page.city_dropdown_element.click()
	new_hotel_page.kyiv_element.click()
	assert new_hotel_page.city_dropdown_element.text == 'Kyiv'
	
	# Verify that Short Description field is editable
	# Verify that Short Description field allows to input alphanumeric characters
	new_hotel_page.short_desc_input_element.send_keys(alphanumeric_value)
	assert new_hotel_page.short_desc_input_element.get_attribute('value') == alphanumeric_value
	
	# Verify that Description field is editable
	# Verify that Description field allows to input alphanumeric characters
	new_hotel_page.desc_input_element.send_keys(alphanumeric_value)
	assert new_hotel_page.desc_input_element.get_attribute('value') == alphanumeric_value
	
	# Verify that Notes field is editable
	# Verify that Notes field allows to input alphanumeric characters
	new_hotel_page.notes_input_element.send_keys(alphanumeric_value)
	assert new_hotel_page.notes_input_element.get_attribute('value') == alphanumeric_value
	
	# Verify that it is possible to save the valid name field
	# Verify that it is possible to save valid Global Rating field
	# Verify that it is possible to save valid Date of Construction field
	# Verify that it is possible to save the valid Country field
	# Verify that it is possible to save the valid City field
	# Verify that it is possible to save the valid Short Description field
	# Verify that it is possible to save the valid Description field
	# Verify that it is possible to save the valid Notes field
	new_hotel_page.save_button_element.click()
	last_page_button =  browser.find_elements_by_xpath('//div[@id="j_idt40:hotels_paginator_bottom"]/span')[-1]
	last_page_button.click()
	wait_presense_xpath(browser, '//td')
	hotel_name_element = browser.find_elements_by_xpath('//td')[-6]
	assert hotel_name_element.text == alphanumeric_value


def test_empty_notes_5_stars(browser):

	new_hotel_page = NewHotelPage(browser)
	valid_date = '5/28/19'
	alphanumeric_value = 'No notes, 5 stars'
	
	new_hotel_page.visit()

	new_hotel_page.name_input_element.send_keys(alphanumeric_value)
	new_hotel_page.global_rating_star_elements[4].click()
	new_hotel_page.date_input_element.send_keys(valid_date)
	new_hotel_page.country_dropdown_element.click()
	new_hotel_page.ukraine_element.click()
	wait_presense_xpath(browser, '//label[@id="add_hotel:city_label"]')
	new_hotel_page.city_dropdown_element.click()
	new_hotel_page.kyiv_element.click()
	new_hotel_page.short_desc_input_element.send_keys(alphanumeric_value)
	new_hotel_page.desc_input_element.send_keys(alphanumeric_value)

	# Verify that it is possible to save the empty Notes field
	# Verify that it is possible to save the Global Rating field
	new_hotel_page.save_button_element.click()
	last_page_button =  browser.find_elements_by_xpath('//div[@id="j_idt40:hotels_paginator_bottom"]/span')[-1]
	last_page_button.click()
	wait_presense_xpath(browser, '//td')
	hotel_name_element = browser.find_elements_by_xpath('//td')[-6]
	assert hotel_name_element.text == alphanumeric_value




