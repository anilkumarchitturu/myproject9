from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'calendar.html')
def output(request):
    dob=request.GET["t1"]
    day=datetime.strptime(dob,"%Y-%m-%d").weekday();
    lst=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    name=lst[day]
    return render(request,'display.html',{"data":name})
