from uuid import uuid4
from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from PIL import Image
# Create your models here.
class Quate(models.Model):
    quate = models.CharField(max_length= 500)
    author = models.CharField(max_length= 30)

    def __str__(self) :
        return self.author


class Catagory(models.Model):
    id = models.SlugField(max_length=50,primary_key=True)
    catagory_name = models.CharField(max_length=50)
    catagory_descriptions = models.TextField(blank=True,null=True)

    def __str__(self) :
        return self.catagory_name

class SubCatagory(models.Model):
    id = models.SlugField(max_length=50,primary_key=True)
    sub_catagory_image = models.ImageField(upload_to = 'subcatagory')
    sub_catagory_name = models.CharField(max_length=50)
    catagory = models.ForeignKey(Catagory,on_delete=CASCADE)

    def save(self,*args, **kwargs):
        try:
            prev = SubCatagory.objects.get(id=self.id)
            if prev.sub_catagory_image != self.sub_catagory_image:
                import os
                if os.path.exists(prev.sub_catagory_image.path):
                    print(prev.sub_catagory_image.name)
                    os.remove(prev.sub_catagory_image.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            c_p = Image.open(self.sub_catagory_image)
            x,y = c_p.size
            x,y = (x,(23*x)//25) if y > (23*x)//25 else ((25*y)//23,y)
            print(x,y)
            c_p = c_p.resize((x,y),Image.ANTIALIAS)
            c_p.save(self.sub_catagory_image.path)

        
    def __str__(self) :
        return self.sub_catagory_name



class Topic(models.Model):
    id = models.SlugField(max_length=250,primary_key=True)
    topic_image = models.ImageField(upload_to = 'topic',blank = True,null = True)
    sub_catagory = models.ForeignKey(SubCatagory,on_delete=CASCADE,blank = True,null = True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=25)
    date_created = models.DateField(default=datetime.today)
    read_times = models.BigIntegerField(default=0,null=True,blank=True)
    # blog_post = RichTextField(blank = True,null=True)
    blog_post = RichTextUploadingField(blank = True,null=True)

    def __str__(self) :
        return self.title
    
def topic_image_upload(instance, filename):
    return 'sanzid.png'

# class ImageModel(models.Model):
#     image = models.ImageField(blank = True,null = True,upload_to=topic_image_upload)
#     alter = models.CharField(max_length=25,blank = True,null = True)
#     topic = models.ForeignKey(TopicModel,on_delete=models.CASCADE)
    

    
#     def __str__(self) :
#         return self.alter

class Comment(models.Model):
    topic = models.ForeignKey(Topic,on_delete=CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=25)
    comment = models.TextField(max_length=1000)
    is_reaplied = models.BooleanField(default=False)

    def __str__(self) :
        return self.email

class CommentReaply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=25)
    reaply = models.TextField(max_length=1000)

    def __str__(self) :
        return self.email

class Subscribers(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
