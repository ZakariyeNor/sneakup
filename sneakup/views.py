from django.shortcuts import render

# Error view
def custom_404_view(request, exception):
    # Page not found 404 handler
    return render(request, 'errors/404.html', status=404)
