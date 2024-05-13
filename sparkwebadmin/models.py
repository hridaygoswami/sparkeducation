from django.db import models
from django.shortcuts import render,redirect
from sparkwebadmin.models import *

# Create your models here.
class slide(models.Model):
    heading=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to="images/",blank=True,null=True)

def _str_(self):
    return f"{self.heading,self.title,self.img}"

class about(models.Model):
    heading=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    img1=models.ImageField(upload_to="images/",blank=True,null=True)
   
def _str_(self):
    return f"{self.heading,self.content,self.img1}"

class Blogs(models.Model):
    heading=models.CharField(max_length=50)
    sub_content=models.CharField(max_length=150)
    content=models.CharField(max_length=250)
    authorname=models.CharField(max_length=20)
    img1=models.ImageField(upload_to="images/",blank=True,null=True)
   
def _str_(self):
    return f"{self.heading,self.sub_content,self.content,self.authorname,self.img1}"

class Gallery(models.Model):
    img1=models.ImageField(upload_to="images/",blank=True,null=True)
    
def _str_(self):
    return f"{self.img1}"

class course1(models.Model):
     img=models.ImageField(upload_to="images/",blank=True,null=True)
     name=models.CharField(max_length=50,null=True)
     description=models.CharField(max_length=200)
     short_description=models.CharField(max_length=100,null=True)

def _str_(self):
    return f"{self.img,self.date,self.link,self.description}"


class contact3(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=15,blank=True,null=True)
    category=models.CharField(max_length=20)
    message=models.CharField(max_length=20)

def _str_(self):
    return f"{self.name,self.email,self.number,self.category,self.message}"

class review(models.Model):
    reviews=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
 

def _str_(self):
    return f"{self.reviews,self.name,self.designation}"

