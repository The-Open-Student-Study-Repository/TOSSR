def theme(request):
    return {
        "theme": request.COOKIES.get("theme", "light")
    }