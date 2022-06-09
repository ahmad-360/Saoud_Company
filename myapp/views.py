from django.http import HttpResponse
from django.shortcuts import render
from .models import Service,About

# Create your views here.
def index(request):

##### Services Section ##############################
    service1 =Service()
    service1.id=1
    service1.name= "Python Coding"
    service1.text=" In this service we can create for you a fully python app "

    service2 =Service()
    service2.id=2
    service2.name= "Front End Coding"
    service2.text=" In this service we can create for you a fully website using Css & Html & Javascript "
    
    
    service3 =Service()
    service3.id=3
    service3.name= "Back End Coding"
    service3.text=" In this service we can create for you a fully Web app Using Django FrameWork and Python "

    service4 =Service()
    service4.id=4
    service4.name= "Management app"
    service4.text=" In this service we can create for you a fully Mangement app for your Business "
    

    Services=Service()
    Services.text="Welcome to my Service Station , So bellow they are my Services , you can take a look if you want"

##### About US section ###########################
    about1=About()
    about1.text1= "Welcome into ABOUT US Section :)"

    about2=About()
    about2.text1="""Our business is start by a one of professional programmer who do a lot of projects with a lot of companies above, he is Ahmed Saoud."""
    about2.text2="Programming is something Hard Honestly, no anyone can converte his idea to an app , but we can due to our experience in this domaine"
    about2.text3="We won alot of challenge worldwide , FFA, CAWS, CEH , WWHA"

    about3=About()
    about3.text1="Our Company is Avaible 24/7 or any projects.\n We know programming is complicated, that's why we are here. "
#### Why us #####################################





#### Rendering Section ################################
    return render (request, "templates/index.html",{"Service1":service1,"Service2":service2,"Service3":service3,"Service4":service4, "Services":Services, "Ab1":about1, "Ab2":about2, "Ab3":about3})

###### About Section #############################

def about (request):
    return render(request,"templates/about.html")











#### Counter Section ###################################
def counter(request):
    text = request.POST["text"]
    am= len(text.split())
    return render (request, "templates/counter.html",{'amount':am})
#### Home Section ######################################
def home(request):
    return render (request,"templates/home.html")
#### Porto Section ###############################
def porto(request):
    return render(request, "templates/porto.html")
