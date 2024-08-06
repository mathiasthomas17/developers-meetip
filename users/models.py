from django.db import models
# Import built in User Model
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank = True)
    username = models.CharField(max_length=200,blank = True,null = True)
    location = models.CharField(max_length=200,blank = True,null = True)

    name= models.CharField(max_length=200,blank = True,null = True)
    email = models.EmailField(max_length=500,blank=True,null= True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    github= models.CharField(max_length=200,blank = True,null = True)
    twitter= models.CharField(max_length=200,blank = True,null = True)
    linkedin= models.CharField(max_length=200,blank = True,null = True)
    youtube= models.CharField(max_length=200,blank = True,null = True)
    website= models.CharField(max_length=200,blank = True,null = True)
    created = models.DateTimeField(auto_now_add = True)
    # Django Provide A ID By Default
    # We can still Override ID Attribute
    id = models.UUIDField(default = uuid.uuid4,unique = True,primary_key = True, editable = False)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile,models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank = True,null = True)
    description = models.TextField(null=True,blank=True)
    id =  models.UUIDField(default = uuid.uuid4,unique = True,primary_key = True, editable = False)

    def __str__(self):
        return self.name

