from django.shortcuts import render
from django.shortcuts import render,redirect
from sparkwebapp.models import *
from sparkwebadmin.models import * 
from django.core.mail import send_mail
from django.conf import settings
from sparkwebadmin.models import Gallery
from sparkwebadmin.models import Blogs
# Create your views here.


def index(request):
    queryset=slide.objects.all()
    queryset1=about.objects.first()
    course=course1.objects.all()    
    reviews=review.objects.all() 
    contact=contact3.objects.all()
    context={'slide':queryset,
             'about':queryset1,
             'course':course,
             'reviews':reviews,
             'contact':contact
             }
    return render(request,'index.html',context)

def about1(request):
    queryset=about.objects.first()
    context={'about':queryset}
    return render(request,'about.html',context)

def gallery(request):
    # Retrieve all Gallery objects using the .objects attribute
    galleries = Gallery.objects.all()
    return render(request, 'gallery.html', {'galleries': galleries})

def blogs(request):
    queryset=Blogs.objects.all()
    context={'blogs':queryset}
    return render(request,'blogs.html',context)


def blog_details(request, id):
    blog = Blogs.objects.get(id=id)
    return render(request, 'blog-details.html', {'blog': blog})
    

def course(request):
    course=course1.objects.all()
    context={'course':course}
    return render(request,'course.html',context)

def coursedetails(request,id):
    queryset=course1.objects.get(id=id)
    context={'course':queryset}
    return render(request,'courses_details.html',context)

def contact_page(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, contact=contact, message=message)
        message = f"Hello SparkEducation, someone has sent a message to you with following details:\nName:{name}\nEmail:{email}\ncontact:{contact}\nmessage:{message}"

        send_mail("SparkEducation!", message, settings.EMAIL_HOST_USER, ['naitikmishra1232@gmail.com'])
    return render(request, "contact.html")
