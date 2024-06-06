from django.shortcuts import render
from .models import *
# Create your views here.
def get_student(req):
    queryset=student.objects.all()
    context={"query":queryset}
    return render(req,"home.html",context)