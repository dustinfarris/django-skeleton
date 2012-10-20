import logging

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.test import TestCase
from django.test.client import Client
from django_nose.tools import *


logger = logging.getLogger(__name__)


def _get_url(obj):
  if models.Model in obj.__class__.__bases__:
    url = obj.get_absolute_url()
  else:
    url = reverse(obj)
  return url
  

def _better_response(response):
  response.should_contain = lambda needle: assert_contains(response, needle)
  response.should_have_html = lambda needle: assert_contains(response, needle, html=True)
  return response


def _better_ajax_response(response):
  response.should_succeed = property(
    lambda: assert_equal(response.status_code, 200))
  return response
  

def visit(obj, data={}):
  url = _get_url(obj)
  response = _better_response(Client().get(url, data))
  logger.debug(response)
  return response
  

def post(obj, data={}):
  url = _get_url(obj)
  response = _better_response(Client().post(url, data))
  logger.debug(response)
  return response


def ajax(method, obj, data={}):
  url = _get_url(obj)
  response = _better_ajax_response(
    Client().post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest'))
  logger.debug(response)
  return response
  

class ModelTester():
  def __init__(self, model, **kwargs):
    if isinstance(model, models.Model):
      self.model_instance = model
    else:
      self.model_instance = model(**kwargs)
    self.fields = [f.__dict__['name'] for f in model._meta.fields]
    self.methods = dir(model)
  
  def should_respond_to(self, query):
    assert_in(query, self.fields + self.methods)

  @property
  def should_be_valid(self):
    assert_is_none(self.model_instance.full_clean())
    return True
  
  @property
  def should_not_be_valid(self):
    assert_raises(ValidationError, self.model_instance.full_clean)
    return True
  

def get_model(model_class, **kwargs):
  return ModelTester(model_class, **kwargs)
  
  
def subject(item):
  def wrapper(f):
    def new_f(*args, **kwargs):
      if 'it' in globals():
        old_it = (globals()['it'],)
      else:
        old_it = None
      try:
        if models.Model in item.__class__.__bases__:
          item = get_model(item)
        globals()['it'] = item
        res = f(*arg, **kwargs)
      finally:
        if old_it:
          globals()['it'] = old_it[0]
        else:
          del(globals()['it'])
      return res
    return new_f
  return wrapper
