from django.shortcuts import render

# Create your views here.
def index(req):
    content =
    return render (req, ‘test.html’, {“content”: “some_text”})