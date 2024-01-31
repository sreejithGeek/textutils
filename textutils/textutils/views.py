from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    values = "Hi, I am Sreejith"
    data = {
        "value": values
    }
    return render(request, "index.html", data)

def analyze(request):
    if request.method == "GET":
        text = request.GET.get("text")
        re_option = request.GET.get("re", "off")
        capi = request.GET.get("capi", "off")

        # Initialize the newtext variable
        newtext = ""

        if re_option == "on":
            # Clean text by removing punctuation
            pun = ".,?!:;\"'-()[]{}.../\\&@#%$€+-*/=<>&_~•©®™°§¶"
            for char in text:
                if char not in pun:
                    newtext += char

        else:
            # If re_option is not 'on', keep the original text
            newtext = text

        if capi == "on":
    # Capitalize the original text if capi is 'on'
            newtext = text.upper()


        # Prepare data for rendering in the template
        data = {
            "t": text,
            "r": newtext,
        }

        return render(request, "analyze.html", data)

    return HttpResponse("Invalid request method or missing parameters.")
