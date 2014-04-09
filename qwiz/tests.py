from django.core.urlresolvers import resolve
from django.http import HttpRequest
import unittest
from django.template.loader import render_to_string

from qwiz.views import home


class HomePageTest(unittest.TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home(request)
		expected_html = render_to_string('qwiz.html')
		self.assertEqual(response.content.decode(), expected_html)
