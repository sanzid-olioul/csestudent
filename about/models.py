from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

class KnownLanguage(models.Model):
    language = models.CharField(max_length=25)
    known_parcent = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.language

class Skills(models.Model):
    name_of_skill = models.CharField(max_length=250)
    known_parcent = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name_of_skill

class Education(models.Model):
    name_of_university = models.CharField(max_length=150)
    start_and_end_year_of_university = models.CharField(max_length=50)
    name_of_depertment = models.CharField(max_length=50)
    type_of_degree = models.CharField(max_length=25) 
    desc_of_university = models.CharField(max_length=300)
    uni_link = models.CharField(max_length=300)
    def __str__(self):
        return self.name_of_university

class WorkExperience(models.Model):
    name_of_company = models.CharField(max_length=250)
    duration = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self) :
        return self.name_of_company


class Description(models.Model):
    header = models.CharField(max_length=250)
    descroption = models.TextField()
    def __str__(self):
        return self.header

class AboutMe(models.Model):
    email = models.EmailField(primary_key=True)
    image = models.ImageField(upload_to = "about_me")
    name = models.CharField(max_length=100)
    locations = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100,default="Blogger")
    phone_no = models.CharField(max_length = 15)
    languages = ManyToManyField(KnownLanguage)
    skills = ManyToManyField(Skills)
    education = OneToOneField(Education,on_delete=CASCADE)
    description = OneToOneField(Description,on_delete=CASCADE)
    work_experience = OneToOneField(WorkExperience,on_delete=CASCADE,null=True) 

    def __str__(self):
        return self.name

class SocialMediaLinks(models.Model):
    facebook = models.CharField(max_length=50)
    twitter  = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin  = models.CharField(max_length=50)
    youtube  = models.CharField(max_length=50)
    github  = models.CharField(max_length=50)

    def __str__(self):
        return "Sanzid Olioul"