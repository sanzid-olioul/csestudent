from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from .send_mail import send
from .models import CommentReaply,SubCatagory


@receiver(post_save, sender=CommentReaply)
def send_mail(sender, instance, created, **kwargs):
    #Sending mail after creaing a reaply
    obj = {
        'body': instance.reaply,
        'receiver': str(instance.comment)
    }
    instance.comment.is_reaplied = True
    instance.comment.save()
    send(obj)


@receiver(post_delete, sender=SubCatagory)
def remove_image(sender, instance, **kwargs):
    import os
    try:
        if os.path.exists(instance.sub_catagory_image.path):
            print(instance.sub_catagory_image.name)
            os.remove(instance.sub_catagory_image.path)
    except:
        print('something went wrong')


