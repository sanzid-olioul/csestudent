from django.shortcuts import render
from django.views import View
from .models import AboutMe, Education,KnownLanguage,Skills,Description,WorkExperience
# Create your views here.
class AboutView(View):
    def get(self,request):

        obj = AboutMe.objects.get(id = 1)
        languages =[]
        skills = []
        try:
            work_experience = WorkExperience.objects.get(id = obj.work_experience_id)
            description = Description.objects.get(id = obj.description_id)
            education = Education.objects.get(id = obj.education_id)
            print(obj.image.url)

            for x in obj.languages.all():
                language = KnownLanguage.objects.get(language = x)
                languages.append(language)
            
            for x in obj.skills.all():
                skil = Skills.objects.get(name_of_skill = x)
                skills.append(skil)

            return render(request,'about.html',{"data":obj,"languages":languages,"skills":skills,"education":education,"description":description,"work_experience":work_experience})
        
        except:
            return render(request,"error404.html",{})