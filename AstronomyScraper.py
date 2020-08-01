from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions as SelError
from selenium.webdriver.chrome.options import Options
import datetime
import DbHandler
import logging

url = "https://www.calsky.com/cs.cgi?cha=3"


def select_check_boxes(browser):
    el = browser.find_element_by_id("idspacecalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("ideventscalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("ideventstv")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idcivilcalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsaintscalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idzodiac")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idforeigncalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idweekcalendar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idgpstime")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idjuliandate")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsiderealtime")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idgeomagnetism")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsky-today")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idheadlines")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idoccultations")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idplanetstars")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idlunareclipse")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsolareclipse")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idmeteors")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idplanetphenom")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idmoonmonthly")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsunyearly")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idasteroidsopp")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idcometsopp")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsats")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idiridium")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idbrightsats")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("iddiurnalarcchart")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsunmoon")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idplanetDaily")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idasteroidDaily")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idcometDaily")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idmeteorsDaily")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idpolarstar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idweatherballoon")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idjoviansats")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idjovianmoonbar")
    # browser.execute_script("window.scrollTo(0, 600)")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsaturniansats")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsaturnianmoonbar")
    if not el.is_selected():
        el.click()
    el = browser.find_element_by_id("idzodiacallight")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idvariables")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idsupernova")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idbinarystar")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idstar-chart")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idmilkyway")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idgalaxy")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idopencluster")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idglobularcluster")
    if el.is_selected():
        el.click()
    el = browser.find_element_by_id("idnebula")
    if el.is_selected():
        el.click()


def set_time_range(browser):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    el = Select(browser.find_element_by_name("startDay"))
    el.select_by_value(str(day))
    el = Select(browser.find_element_by_name("startMonth"))
    el.select_by_value(str(month))
    el = Select(browser.find_element_by_name("startYear"))
    el.select_by_value(str(year))
    el = Select(browser.find_element_by_name("startHour"))
    el.select_by_value(str(hour))
    el = Select(browser.find_element_by_name("startMin"))
    el.select_by_value(str(minute))
    el = Select(browser.find_element_by_name("startSec"))
    el.select_by_value(str(second))
    el = Select(browser.find_element_by_name("interval"))
    el.select_by_value('1')


def calculate_events(browser):
    el = browser.find_element_by_name("Go")
    el.click()


def get_events(browser):
    events = browser.find_elements_by_class_name("caltr")
    return_list = []
    for event in events:
        if not event.get_attribute("tabindex"):
            events.remove(event)
            continue
        if "Beobachtungsort" in event.text:
            events.remove(event)
            continue
        event_dict = {}
        try:
            time = event.find_element_by_class_name("caltime").text
            event_obj = event.find_element_by_class_name("calname").text
            details = event.find_element_by_class_name("calinfo").text
            event_dict["time"] = time
            event_dict["object"] = event_obj
            event_dict["details"] = details
            return_list.append(event_dict)
        except AttributeError as e:
            logging.error("Class of element not present: " + str(e) + ": " + event.text)
    return return_list


def insert_events(db, events):
    db.insert_events(events)


def scrape():
    try:
        db = DbHandler.DbHandler()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(url)
        try:
            cookie = browser.find_element_by_xpath("//*[@id='body']/div[4]/div")
            cookie.click()
        except SelError.NoSuchElementException:
            pass
        select_check_boxes(browser)
        set_time_range(browser)
        calculate_events(browser)
        events = get_events(browser)
        insert_events(db, events)
    except Exception as e:
        logging.error("Scraping failed: " + str(e) + ". Trying again in 1 minute.")
        scrape()


if __name__ == '__main__':
    scrape()
