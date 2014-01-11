#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys
from config import (EMAIL, PASSWORD)


class CourseraScraper:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.email = EMAIL
        self.password = PASSWORD
        self.courses = []

    def login(self):
        self.driver.get('https://www.coursera.org/account/signin')
        email_field = self.driver.find_element_by_id("signin-email")
        password_field = self.driver.find_element_by_id("signin-password")
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        password_field.submit()

    def get_courses(self):
        soup = BeautifulSoup(self.driver.page_source)
        course_links = soup.find_all('a', text = "Go to class")
        for course in course_links:
            self.driver.get(course.attrs['href'])
            course_page = self.driver.page_source
            page_soup = BeautifulSoup(course_page)
            cats = page_soup.find_all('div', 'course-overview-upcoming-category')
            for category in cats:
                #print cat.h4.text
                print category.text.strip()

            self.driver.back()
            time.sleep(2)


if __name__ == "__main__":
    scraper = CourseraScraper()
    scraper.driver.implicitly_wait(10)
    scraper.login()
    time.sleep(3)
    scraper.get_courses()
