from django.contrib import admin

# Register your models here.
from .models import KnownLanguage,Skills,Education,Description,AboutMe, SocialMediaLinks,WorkExperience
@admin.register(KnownLanguage)
class KnownLanguage(admin.ModelAdmin):
    list_display = ("language","known_parcent")
    
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name_of_skill","known_parcent")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("name_of_university","name_of_depertment","type_of_degree")


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("header","descroption")


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone_no")

@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ("facebook","github","instagram","linkedin")

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("name_of_company","duration","description")
