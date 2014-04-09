from lettuce import *
from lettuce.django import django_url
from selenium import webdriver


@before.all
def setup_browser():
	world.browser = webdriver.Firefox()
	print "Starting tests..."

@after.all
def teardown_browser(total):
	print "Results: %d of %d scenarios passed! " % (
		total.scenarios_ran,
		total.scenarios_passed
		)
	print "Goodbye!"
	world.browser.quit()

