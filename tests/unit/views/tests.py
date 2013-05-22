# -*- coding: utf-8 -*-

from __future__ import absolute_import

import mock

from {{ project_name }}.views import server_error, page_not_found
from {{ project_name }}.testutils import TestCase


class ServerErrorTest(TestCase):

    @mock.patch('{{ project_name }}.views.render')
    def test_server_error(self, render_mock):
        server_error("RequestMock")

        render_mock.assert_called_with("RequestMock", "500.html")

    @mock.patch('{{ project_name }}.views.render')
    def test_page_not_found(self, render_mock):
        page_not_found("RequestMock")

        render_mock.assert_called_with("RequestMock", "404.html")
