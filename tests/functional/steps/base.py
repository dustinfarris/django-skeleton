from behave import *
from django.core.urlresolvers import reverse
from nose.tools import *


@given('I visit the url "{url}"')
def step(c, url):
    c.browser.get(c.url(url))
    if url == c.browser.current_url:
        c.browser.refresh()
    else:
        c.browser.get(c.url(url))


@given('I visit the {name} page')
def step(c, name):
    url = c.url(reverse(name))
    if url == c.browser.current_url:
        c.browser.refresh()
    else:
        c.browser.get(c.url(reverse(name)))


@when('I visit the {name} page')
def step(c, name):
    c.execute_steps(u"Given I visit the %s page" % name)


@when('I visit the url "{url}"')
def step(c, url):
    c.execute_steps(u"Given I visit the url \"%s\"" % url)


@given('I am logged in as a superuser')
def step(c):
    c.execute_steps(u"""
        Given I visit the url "/admin/"
        When I enter the correct admin username and password
        And I click submit
        """)


@when('I enter the correct admin username and password')
def step(c):
    username_field = c.browser.find_element_by_name("username")
    password_field = c.browser.find_element_by_name("password")
    username_field.send_keys("admin")
    password_field.send_keys("admin")


@when('I enter the correct username and password')
def step(c):
    username_field = c.browser.find_element_by_name("username")
    password_field = c.browser.find_element_by_name("password")
    username_field.send_keys("bob@bob.com")
    password_field.send_keys("bob")


@when('I enter the wrong username and password')
def step(c):
    username_field = c.browser.find_element_by_name("username")
    password_field = c.browser.find_element_by_name("password")
    username_field.send_keys("bob@bob.com")
    password_field.send_keys("aasdfasdf")


@when('I fill in {name} with "{text}"')
def step(c, name, text):
    field = c.browser.find_element_by_name(name)
    field.send_keys(text)


@when('I add "{obj}" to chosen {objs}')
def step(c, obj, objs):
    """Assuming we are using a horizontal filter here."""
    select_element = c.browser.find_element_by_id('id_%s_from' % objs)
    option_element = select_element.find_element_by_xpath(
        '//option[text()="%s"]' % obj)
    add_link = c.browser.find_element_by_id('id_%s_add_link' % objs)
    option_element.click()
    add_link.click()


@when('I select the "{obj}" {name}')
def step(c, obj, name):
    select = c.browser.find_element_by_xpath('//select[@name="%s"]' % name)
    option = select.find_element_by_xpath('//option[text()="%s"]' % obj)
    option.click()


@when('I click the link "{text}"')
def step(c, text):
    c.browser.find_element_by_link_text(text).click()


@when('I click the login button')
def step(c):
    c.browser.find_element_by_id("login").click()


@when('I click the button "{text}"')
def step(c, text):
    c.browser.find_element_by_xpath('//button[text()="%s"]' % text)


@when('I click the submit button "{text}"')
def step(c, text):
    c.browser.find_element_by_xpath(
        '//input[@type="submit" and @value="%s"]' % text).click()


@when('I click submit')
def step(c):
    c.browser.find_element_by_css_selector('input[type="submit"]').click()


@then('I should be redirected to the {name} page')
def step(c, name):
    assert_equal(c.url(reverse(name)), c.browser.current_url)


@then('I should see the text "{text}"')
def step(c, text):
    body = c.browser.find_element_by_xpath('//body').text
    assert_in(text, body)


@then('I should see the xpath "{xpath}"')
def step(c, xpath):
    result = c.browser.find_elements_by_xpath(xpath)
    assert_greater(len(result), 0)


@then('I should not see the xpath "{xpath}"')
def step(c, xpath):
    result = c.browser.find_elements_by_xpath(xpath)
    assert_equal(len(result), 0)


@then('I should not see the text "{text}"')
def step(c, text):
    body = c.browser.find_element_by_xpath('//body').text
    assert_not_in(text, body)


@then('I should see the link "{text}"')
def step(c, text):
    result = c.browser.find_elements_by_link_text(text)
    assert_greater(len(result), 0)
