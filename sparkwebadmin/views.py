from django.shortcuts import render
from django.shortcuts import render,redirect
from sparkwebadmin.models import * 
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


# Create your views here.

def index(request):
    return render(request,'header1.html')

def main6(request):
    if request.method == 'POST':
            data=request.POST
            heading=data.get('heading')
            title=data.get('title')
            img=request.FILES.get('img')

            print(heading,title,img)
            
            slide.objects.create(
                heading=heading,
                title=title,
                img=img
            )
    queryset=slide.objects.all()
    context={'slide':queryset}
    return render(request,'slider.html',context)

def main5(request):
    if request.method == 'POST':
            data=request.POST
            heading=data.get('heading')
            content=data.get('content')
            img1=request.FILES.get('img1')
            

            print(heading,content,img1)
            
            about.objects.create(
                heading=heading,
                content=content,
                img1=img1,
                )
    queryset=about.objects.all()
    context={'about':queryset}
    return render(request,'aboutus.html',context)


def main9(request):
    if request.method == 'POST':
            data=request.POST
            img=request.FILES.get('img')
            name=data.get('name')
            short=data.get('short')
            description=data.get('description')

            
            course1.objects.create(
                img=img,
                name=name,
                short_description=short,
                description=description
            )
    queryset=course1.objects.all()
    context={'course1':queryset}
    return render(request,'course1.html',context)

def main4(request):
    if request.method == 'POST':
            data=request.POST
            name=data.get('name')
            email=data.get('email')
            number=data.get('number')
            category=data.get('category')
            message=data.get('message')

            print(name,email,number,category,message)
            
            contact3.objects.create(
                name=name,
                email=email,
                number=number,
                category=category,
                message=message
            )
    queryset=contact3.objects.all()
    context={'contact3':queryset}
    return render(request,'contactus.html',context)
    
    
def main7(request):
    if request.method == 'POST':
            data=request.POST
            reviews=data.get('reviews')
            name=data.get('name')
            designation=data.get('designation')            
            review.objects.create(
                reviews=reviews,
                name=name,
                designation=designation,
            )
    queryset=review.objects.all()
    context={'review':queryset}
    return render(request,'testimonials.html',context)

def deleterow6(request,id):
      print(id)
      queryset=review.objects.get(id=id)
      queryset.delete()
      return redirect('/sparkwebadmin/review/')
  
def deleterow5(request,id):
      print(id)
      queryset=slide.objects.get(id=id)
      queryset.delete()
      return redirect('/sparkwebadmin/slide/')
  
def deleterow4(request,id):
      print(id)
      queryset=about.objects.get(id=id)
      queryset.delete()
      return redirect('/sparkwebadmin/about/')
  
def deleterow3(request,id):
      print(id)
      queryset=contact3.objects.get(id=id)
      queryset.delete()
      return redirect('/sparkwebadmin/contactus/')
  
def deleterow8(request,id):
      print(id)
      queryset=course1.objects.get(id=id)
      queryset.delete()
      return redirect('/sparkwebadmin/course1')
  
def slideup(request,id):
    print(id)
    queryset=slide.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        heading=data.get('heading')
        title=data.get('title')
        img=request.FILES.get('img')

        queryset.heading=heading
        queryset.title=title
        queryset.img=img  
        queryset.save()
        return redirect('../../slide/')
    context={'slide':queryset}
    
    return render(request,'updateslider.html',context)

def testimonials(request,id):
    print(id)
    queryset=review.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        reviews=data.get('reviews')
        name=data.get('name')
        designation=data.get('designation')
        

        queryset.reviews=reviews
        queryset.name=name
        queryset.designation=designation
        
        queryset.save()
        return redirect('../../review/')
    context={'review':queryset}
    
    return render(request,'updatetestimonials.html',context)

def contactup(request,id):
    print(id)
    queryset=contact3.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        number=data.get('number')
        category=data.get('category')
        message=data.get('message')
        queryset.name=name
        queryset.email=email
        queryset.number=number
        queryset.category=category
        queryset.message=message   
        queryset.save()
        return redirect('../../contactus/')
    context={'contact3':queryset}
    
    return render(request,'update_contactus.html',context)

def aboutup(request,id):
    print(id)
    queryset=about.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        heading=data.get('heading')
        content=data.get('content')
        img1=request.FILES.get('img1')
        queryset.heading=heading
        queryset.content=content
        queryset.img1=img1
        queryset.save()
        return redirect('../../about/')
    context={'about':queryset}
    
    return render(request,'update_about.html',context)

def course1up(request,id):
    print(id)
    queryset=course1.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        img=request.FILES.get('img')
        name=data.get('name')
        short_description=data.get('short')
        description=data.get('description')

        queryset.img=img
        queryset.name=name
        queryset.short_description=short_description
        queryset.description=description
        queryset.save()
        return redirect('../../course1/')
    context={'course1':queryset}
    
    return render(request,'update_course.html',context)

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('username')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            request.session['email'] = email
            return redirect('../slide/')  # Replace 'home' with the appropriate URL name
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


def logout(request):
    del request.session['email']
    return redirect('login')
