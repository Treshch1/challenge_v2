class NewHotelPage:
    
    title_xpath = '//h2[.="Register new Hotel"]'
    data_section_xpath = '//table'
    save_button_xpath = '//button[@id="add_hotel:j_idt62"]'
    
    name_label_xpath = '//label[@id="add_hotel:j_idt42"]'
    name_warning_xpath = '//div[@id="add_hotel:j_idt43"]'
    name_input_xpath = '//input[@id="add_hotel:name"]'
    
    global_rating_xpath = '//label[@id="add_hotel:j_idt44"]'
    global_rating_stars_xpath = '//div[@class="ui-rating-star"]'
    
    date_xpath = '//label[@id="add_hotel:j_idt46"]'
    date_input_xpath = '//input[@id="add_hotel:dateOfConstruction_input"]'
    date_warning_xpath = '//div[@id="add_hotel:j_idt47"]'
    
    country_xpath = '//label[@id="add_hotel:j_idt48"]'
    country_dropdown_xpath = '//label[@id="add_hotel:country_label"]'
    ukraine_xpath = '//li[.="Ukraine"]'
    country_warning_xpath = '//div[@id="add_hotel:j_idt51"]'
    
    city_xpath = '//label[@id="add_hotel:j_idt52"]'
    city_dropdown_xpath = '//label[@id="add_hotel:city_label"]'
    kyiv_xpath = '//li[.="Kyiv"]'
    city_warning_xpath = '//div[@id="add_hotel:j_idt55"]'
    
    short_desc_xpath = '//label[@id="add_hotel:j_idt56"]'
    short_desc_input_xpath = '//input[@id="add_hotel:short_description"]'
    short_desc_warning_xpath = '//div[@id="add_hotel:j_idt57"]'
    
    desc_xpath = '//label[@id="add_hotel:j_idt58"]' 
    desc_input_xpath = '//textarea[@id="add_hotel:description"]'
    desc_warning_xpath = '//div[@id="add_hotel:j_idt59"]' 
    
    notes_xpath = '//label[@id="add_hotel:j_idt60"]'
    notes_input_xpath = '//textarea[@id="add_hotel:notes"]'


    def __init__(self, browser):
        self.browser = browser

    @property
    def title_element(self):
        return self.browser.find_element_by_xpath(self.title_xpath)

    @property
    def data_section_table_div(self):
        return self.browser.find_element_by_xpath(self.data_section_xpath)

    @property
    def save_button_element(self):
        return self.browser.find_element_by_xpath(self.save_button_xpath)

    @property
    def name_label_element(self):
        return self.browser.find_element_by_xpath(self.name_label_xpath)

    @property
    def name_input_element(self):
        return self.browser.find_element_by_xpath(self.name_input_xpath)

    @property
    def name_warning_element(self):
        return self.browser.find_element_by_xpath(self.name_warning_xpath)

    @property
    def name_global_rating_element(self):
        return self.browser.find_element_by_xpath(self.global_rating_xpath)

    @property
    def global_rating_star_elements(self):
        return self.browser.find_elements_by_xpath(self.global_rating_stars_xpath)

    @property
    def date_element(self):
        return self.browser.find_element_by_xpath(self.date_xpath)

    @property
    def date_input_element(self):
        return self.browser.find_element_by_xpath(self.date_input_xpath)        

    @property
    def date_warning_element(self):
        return self.browser.find_element_by_xpath(self.date_warning_xpath)

    @property
    def country_element(self):
        return self.browser.find_element_by_xpath(self.country_xpath)

    @property
    def country_dropdown_element(self):
        return self.browser.find_element_by_xpath(self.country_dropdown_xpath)        

    @property
    def ukraine_element(self):
        return self.browser.find_element_by_xpath(self.ukraine_xpath)        

    @property
    def country_warning_element(self):
        return self.browser.find_element_by_xpath(self.country_warning_xpath)

    @property
    def city_element(self):
        return self.browser.find_element_by_xpath(self.city_xpath)

    @property
    def city_dropdown_element(self):
        return self.browser.find_element_by_xpath(self.city_dropdown_xpath)

    @property
    def kyiv_element(self):
        return self.browser.find_element_by_xpath(self.kyiv_xpath)

    @property
    def city_warning_element(self):
        return self.browser.find_element_by_xpath(self.city_warning_xpath)

    @property
    def short_desc_element(self):
        return self.browser.find_element_by_xpath(self.short_desc_xpath)

    @property
    def short_desc_input_element(self):
        return self.browser.find_element_by_xpath(self.short_desc_input_xpath)

    @property
    def short_desc_warning_element(self):
        return self.browser.find_element_by_xpath(self.short_desc_warning_xpath)

    @property
    def desc_element(self):
        return self.browser.find_element_by_xpath(self.desc_xpath)

    @property
    def desc_input_element(self):
        return self.browser.find_element_by_xpath(self.desc_input_xpath)

    @property
    def desc_warning_element(self):
        return self.browser.find_element_by_xpath(self.desc_warning_xpath)

    @property
    def notes_element(self):
        return self.browser.find_element_by_xpath(self.notes_xpath)

    @property
    def notes_input_element(self):
        return self.browser.find_element_by_xpath(self.notes_input_xpath)

    def visit(self):
        self.browser.get('http://wildfly:8080/article/faces/hotel.xhtml')
    