from lettuce import step, world
from lettuce.django import django_url
from nose.tools import assert_equals
from selenium.webdriver.common.keys import Keys

@step(u'I access the url "([^"]*)"')
def i_access_the_url(step, url):
	full_url = django_url(url)
	world.browser.get(full_url)

@step(u'Then I see the header "([^"]*)"')
def then_i_see_the_header(step, content):
	assert 'Qwiz' in world.browser.title, "Browser title was " + world.browser.title

@step(u'Given I see a display asking me to add a new question')
def given_i_see_a_display_asking_me_to_add_a_new_question(step):
	header_text = world.browser.find_element_by_tag_name('h1').text
	assert 'Add a New Question' in header_text

@step(u'And a text box titled Title')
def and_a_text_box_titled_title(step):
	title_input = world.browser.find_element_by_id('id_new_question')
	assert_equals(
    	title_input.get_attribute('placeholder'), 
    	'Add a new question'
    )

@step(u'I can write in the title for my question')
def i_can_write_in_the_title_for_my_question(step):
	title_input = world.browser.find_element_by_id('id_new_question')
	title_input.send_keys('Do you you think Fat Cat is cool?')
	title_input.send_keys(Keys.ENTER)
	
@step(u'And a text box titled Question')
def and_a_text_box_titled_question(step):
    assert False, 'This step must be implemented'

@step(u'I can write in the text of my question')
def i_can_write_in_the_text_of_my_question(step):
    assert False, 'This step must be implemented'
