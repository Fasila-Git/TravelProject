from django.shortcuts import render
from .models import Place
from .models import people

# Create your views here.
def index(reqeust):
    obj=Place.objects.all()
    team=people.objects.all()
    return render(reqeust,"index.html",{'result':obj, 'val':team})


