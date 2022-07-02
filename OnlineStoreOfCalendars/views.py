from datetime import date
from tabnanny import check
from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
import random

def localization(lg):
    print("HI")
    try:
        with open("./Files/localization.json", "r") as read_file:
            data = json.load(read_file)
        return data[str(lg)]
    except:
        return data['ru']

def RandomizePassword():
    symbolic="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    return str(''.join([symbolic[random.randint(0,len(symbolic)-1)] for i in range(20)]))

def Category(name,lg):
    Calendars=CALENDAR.objects.all().filter(category=CATEGORY.objects.get(name=name),language=LANGUAGE.objects.get(id_name=lg))
    dictionary=localization(lg)
    dictionary.update({"Calendars":Calendars})
    return dictionary
def Home(request,lg):
    Calendars=CALENDAR.objects.all().filter(language=LANGUAGE.objects.get(id_name=lg),check_mark=True)
    dictionary=localization(lg)
    dictionary.update({"Calendars":Calendars})
    return render(request,'home.html',dictionary)
def Release(request,lg):
    return render(request,'release.html',Category("Release",lg))

def Event(request,lg):
    return render(request,'event.html',Category("Event",lg))

def Other(request,lg):
    return render(request,'other.html',Category("Other",lg))

def Sport(request,lg):
    return render(request,'sport.html',Category("Sport",lg))

def Holidays(request,lg):
    return render(request,'holidays.html',Category("Holidays",lg))

def Install(request,lg,id):
    Calendar=CALENDAR.objects.all().get(id=id)
    dictionary=localization(lg)
    dictionary.update({"Calendar":Calendar,"event":dictionary[Calendar.category.name]})
    return render(request,'install.html',dictionary)

def Create(request,lg):
    return render(request,'create.html',localization(lg))

def Post(request,lg):
    lang=localization(lg)
    dictionary=lang
    if request.method == 'POST':
        try:
            Calendar=CALENDAR.objects.all()
            password=RandomizePassword()
            Calendar.create(name=request.POST["name"],icon=request.FILES['icon'],category=CATEGORY.objects.get(name=request.POST["category"]),password=password,author=request.POST["author"],calendarID=request.POST["calendarID"],description=request.POST["description"],language=LANGUAGE.objects.get(id_name=request.POST["language"]))
            dictionary.update({"password":password,"id":Calendar[::-1][0].id})
        except:
            pass
    category=CATEGORY.objects.all()
    for i in range(len(category)):
        category[i].lang=lang[category[i].name]
    dictionary.update({"language":LANGUAGE.objects.all()})
    dictionary.update({"categories":category})
    return render(request,'post.html',dictionary)

def How_add_to_calendar(request,lg):
    return render(request,'how_add_to_calendar.html',localization(lg))



def GetName(request):
    id=request.GET.get("id")
    name=CALENDAR.objects.all().get(id=int(id)).name
    return JsonResponse({"name":name,"id":id})


def Edit(request,lg,id):
    lang=localization(lg)
    dictionary=lang
    if request.method == 'POST':
        Calendar=CALENDAR.objects.all().get(id=int(id))
        if request.POST["password"]==Calendar.password:
            try:
                request.POST["icon"]
            except:
                Calendar.icon=request.FILES["icon"]
            Calendar.name=request.POST["name"]
            Calendar.author=request.POST["author"]
            Calendar.author=request.POST["author"]
            Calendar.calendarID=request.POST["calendarID"]
            Calendar.description=request.POST["description"]
            Calendar.save()
    category=CATEGORY.objects.all()
    for i in range(len(category)):
        category[i].lang=lang[category[i].name]
    Calendar=CALENDAR.objects.all().get(id=id)
    dictionary=localization(lg)
    dictionary.update({"Calendar":Calendar,"event":dictionary[Calendar.category.name]})
    dictionary.update({"categories":category})
    dictionary.update({"id":id})
    return render(request,'edit.html',dictionary)


def Search(request,lg,sear):
    Calendars=CALENDAR.objects.all().filter(language=LANGUAGE.objects.get(id_name=lg))
    CalendarFilters=[]
    for i in Calendars:
        if (sear in i.name) or (sear in i.description):
            CalendarFilters.append(i)
    dictionary=localization(lg)
    dictionary.update({"Calendars":CalendarFilters})
    return render(request,'search.html',dictionary)
