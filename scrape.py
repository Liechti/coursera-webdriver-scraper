#!/usr/local/bin/python                                                             
# -*- coding: utf-8 -*-                                                             
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import sys
from config import (EMAIL, PASSWORD)


def login(driver, signin_url, email, password):
    driver.get(signin_url)
    email_field = driver.find_element_by_id("signin-email")
    password_field = driver.find_element_by_id("signin-password")
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.submit()
    return driver
    
def get_courses(driver):
    course_buttons = driver.find_elements_by_css_selector("a[class*='coursera-course-button']")
    courses = driver.find_elements_by_class_name("coursera-course-listing-name")

    course_names = []
    course_urls = []

    for n in range(len(courses)):
        if course_buttons[n].text == 'Go to class':
            course_names.append(courses[n].text)
            course_buttons.append(course_buttons[n].text)
            course_urls.append(course_buttons[n].get_attribute("href"))
    
    for n in range(len(course_urls)):
        driver.get(course_urls[n])
        time.sleep(0.5)
        deadlines = driver.find_elements_by_class_name("course-assignment-deadline")
        print '------------------------'
        print course_names[n]
        print '------------------------'
        if len(deadlines) > 0:
            for deadline in deadlines:
                print deadline.get_attribute("data-event-title")
                print deadline.text #For Displaying the deadline date
        else:
            print "No upcoming deadlines!"
    
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    home_url = "https://www.coursera.org"
    signin_url = 'https://www.coursera.org/account/signin'
    email = EMAIL # See config.py
    password = PASSWORD # See config.py
    driver = login(driver,signin_url, email, password)
    time.sleep(2)
    get_courses(driver)
