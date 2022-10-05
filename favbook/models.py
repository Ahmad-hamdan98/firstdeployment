
from email.policy import default
from tkinter import CASCADE
from django.db import models
import re
# Create your models here.


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
            return errors

        if len(postData['pass']) < 8:
            errors["pass"] = "I dont like your password ! try again"
        if postData['confirm'] != postData['pass']:
            errors["confirm"] = " you confirm wronge passwored try again"    
        return errors

        


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email=models.CharField(max_length=255,default="ahmad@hamdan.com")
    password=models.CharField(max_length=255,default="password")
    confirm_PW=models.CharField(max_length=255,default="password")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    # booksupload

class val(models.Manager):
     def basic(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "Title should be at least 5 characters"
        if len(postData['desc']) < 5:
            errors["desc"] = "Description should be at least 5 characters"
        return errors
        
class Book(models.Model):
    title = models.CharField(max_length=255)
    uploder = models.ForeignKey(User ,related_name="booksupload" ,on_delete=CASCADE)
    desc=models.CharField(max_length=255,default="no description for this one")
    userlike = models.ManyToManyField(User,related_name="likedbooks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = val()