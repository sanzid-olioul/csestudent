from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html,urlencode
from django.db.models.aggregates import Count

# Register your models here.
from .models import Quate,Catagory,Comment,CommentReaply, SubCatagory,Topic,Subscribers

@admin.register(Quate)
class QuateAdmin(admin.ModelAdmin):
    list_display = ("quate","author")


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ("catagory_name","catagory_descriptions","number_of_topics")
    prepopulated_fields = {
        "id":["catagory_name"],
    }
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            number_of_catagory = Count("subcatagory",distinct=True),
        )
        return queryset

    def number_of_topics(self,catagory):
        url = (reverse('admin:articles_subcatagory_changelist')
            + '?'
            + urlencode({
                'group__pk': catagory.id
            })
        )
        return format_html('<a href="{}">{}</a>',url,catagory.number_of_catagory)
    



@admin.register(SubCatagory)
class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = ("sub_catagory_name","sub_catagory_image","catagory","number_of_topics")
    search_fields = ("sub_catagory_name",)
    prepopulated_fields = {
        "id":["sub_catagory_name",]
    }
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            number_of_topic = Count("topic",distinct=True),
        )
        return queryset

    def number_of_topics(self,sub_catagory):
        url = (reverse('admin:articles_topic_changelist')
            + '?'
            + urlencode({
                'group__pk': sub_catagory.id
            })
        )
        return format_html('<a href="{}">{}</a>',url,sub_catagory.number_of_topic)
    


@admin.register(CommentReaply)
class CommentReaplyAdmin(admin.ModelAdmin):
    list_display = ("email","name","comment","reaply")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("email","name","comment","topic","is_reaplied","reaply_comment")
    list_filter = ['is_reaplied']
    def reaply_comment(self,comment):
        url = reverse('articles:single_article',args=[comment.topic.id])
        print(url)
        return format_html('<a href="{}">{} reaply</a>',url,comment)




@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title","author","date_created","sub_catagory","read_times")
    autocomplete_fields = ("sub_catagory",)
    search_fields = ("title",)
    readonly_fields = ("read_times",)
    prepopulated_fields = {
        "id": ["sub_catagory","title"]
    }


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ("email",)
