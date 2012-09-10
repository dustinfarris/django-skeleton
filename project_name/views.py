from django.shortcuts import render


def server_error(request):
  return render(request, '500.jade')


def page_not_found(request):
  return render(request, '404.jade')