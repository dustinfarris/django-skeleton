# -*- coding: utf-8 -*-

from __future__ import absolute_import

from exam import Exam, fixture, patcher  # NOQA

from django.conf import settings as django_settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse  # NOQA
from django.http import HttpRequest
from django.test import (TestCase, LiveServerTestCase, RequestFactory,  # NOQA
                         Client)  # NOQA
from django.test.utils import override_settings  # NOQA
from django.utils import timezone
from django.utils.importlib import import_module
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver


class Ajax(Client):

    def get(self, *args, **kwargs):
        kwargs.update({'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        return super(Ajax, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs.update({'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        return super(Ajax, self).post(*args, **kwargs)


class BaseTestCase(Exam):

    ajax = Ajax()

    @fixture
    def user(self):
        user = User.objects.create(
            username="bob@example.com",
            email="bob@example.com",
            is_staff=False,
            is_superuser=False)
        user.set_password("user")
        user.save()
        user.reload = lambda: User.objects.get(id=user.id)
        return user

    @fixture
    def superuser(self):
        superuser = User.objects.create(
            username="admin",
            email="admin@localhost",
            is_staff=True,
            is_superuser=True)
        superuser.set_password("admin")
        superuser.save()
        return superuser

    def login_uri(self, next=None, dont_reverse=False):
        redirect_uri = reverse('login')
        if next is not None:
            if dont_reverse:
                redirect_uri += '?next=%s' % next
            else:
                redirect_uri += '?next=%s' % reverse(next)
        return redirect_uri

    def login_as(self, user):
        user.backend = django_settings.AUTHENTICATION_BACKENDS[0]

        request = HttpRequest()
        request.session = self.get_session(self.client)
        login(request, user)
        request.session.save()
        self.set_session_cookies(request.session, self.client)

        request = HttpRequest()
        request.session = self.get_session(self.ajax)
        login(request, user)
        request.session.save()
        self.set_session_cookies(request.session, self.ajax)

    def get_session(self, agent):
        if agent.session:
            session = agent.session
        else:
            engine = import_module(django_settings.SESSION_ENGINE)
            session = engine.SessionStore()
        return session

    def set_session_cookies(self, session, agent):
        # Set the cookie to represent the session
        session_cookie = django_settings.SESSION_COOKIE_NAME
        agent.cookies[session_cookie] = session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': django_settings.SESSION_COOKIE_DOMAIN,
            'secure': django_settings.SESSION_COOKIE_SECURE or None,
            'expires': None}
        agent.cookies[session_cookie].update(cookie_data)

    def login(self):
        self.login_as(self.user)

    def tzdatetime(self, *args):
        if args[0] == "now":
            dt = timezone.now()
        else:
            dt = timezone.datetime(*args)
        return timezone.make_aware(dt, timezone.get_current_timezone())

    def assertHasMessage(self, response, message, tag=None):
        for resp_message in list(response.context['messages']):
            if message == resp_message.message:
                if tag is not None and tag not in resp_message.tags:
                    continue
                return True
        error_message = "Message not created: \"%s\"" % message
        if tag is not None:
            error_message += ", tagged \"%s\"" % tag
        raise AssertionError(error_message)


class TestCase(BaseTestCase, TestCase):
    pass


class LiveServerTestCase(BaseTestCase, LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(8)
        super(LiveServerTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LiveServerTestCase, cls).tearDownClass()

    def admin_login(self):
        self.browser.get(self.live_server_url + "/admin/")
        username_field = self.browser.find_element_by_name("username")
        password_field = self.browser.find_element_by_name("password")
        username_field.send_keys(self.superuser.username)
        password_field.send_keys("admin")
        password_field.send_keys(Keys.RETURN)

    def admin_logout(self):
        self.browser.get(self.live_server_url + "/admin/")
        self.browser.find_element_by_link_text("Log out").click()
