from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403(request, exception):
    """ Error Handler 403 - Page Not Found """
    return render(request, "errors/403.html", status=404)


def handler401(request, exception):
    """ Error Handler 401 - Page Not Found """
    return render(request, "errors/401.html", status=404)


def handler500(request, exception):
    """ Error Handler 500 - Page Not Found """
    return render(request, "errors/500.html", status=404)
