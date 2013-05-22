from django.shortcuts import render


def server_error(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response


def page_not_found(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response
