from django.shortcuts import get_object_or_404, render
from .models import Image, Link, Text

# Create your views here.

def index(request):
    image = get_object_or_404(Image, id=1)
    facebook = get_object_or_404(Link, id=3)
    github = get_object_or_404(Link, id=1)
    gmail = get_object_or_404(Link, id=4)
    text = get_object_or_404(Text, id=1)
    text2 = get_object_or_404(Text, id=2)
    text3 = get_object_or_404(Text, id=3)
    text5 = get_object_or_404(Text, id=5)
    text6 = get_object_or_404(Text, id=6)
    text7 = get_object_or_404(Text, id=7)
    text11 = get_object_or_404(Text, id=11)
    image1 = get_object_or_404(Image, id=4)
    text8 = get_object_or_404(Text, id=8)
    text12 = get_object_or_404(Text, id=12)
    image2 = get_object_or_404(Image, id=6)
    text9 = get_object_or_404(Text, id=9)
    text13 = get_object_or_404(Text, id=13)
    image3 = get_object_or_404(Image, id=3)
    text10 = get_object_or_404(Text, id=10)
    text14 = get_object_or_404(Text, id=14)
    image4 = get_object_or_404(Image, id=5)

    
    return render(request, 'myapp/index.html',{'image': image,
    'facebook' : facebook, 
    'github' : github,
    'gmail' : gmail,
    'text' : text,
    'text2' : text2,
    'text3' : text3,
    'text5' : text5,
    'text6' : text6,
    'text7' : text7,
    'text11' : text11,
    'text8' : text8,
    'text12' : text12,
    'text9' : text9,
    'text13' : text13,
    'text10' : text10,
    'text14' : text14,})


def Portfolio(request):
    return render(request, 'myapp/portfolio.html')