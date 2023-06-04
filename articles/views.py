from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .query import Query,SaveComment,GetComment,ArticleAside,Subscribe,Catagory
from .models import CommentReaply,Comment
# Create your views here.
from django.views import View
class HomeView(View):
    def get(self,request):
        try:
            query = Query()
            #for getting quate
            quate = query.get_quate()
            
            #for getting carosel
            carosels = query.get_carosels()
            #for getting catagories
            catagorys = query.get_catagories()
            
            #for getting sub catagories
            topics = query.sub_catagorys()
            popular_tags = query.popular_tag()
            populars = query.get_popular_articles()
            
            paginator = Paginator(topics,3)
            page = 1
            try:
                page = request.GET["page"]
            except:
                page = 1
            posts = paginator.get_page(page)


            obj = {
                "quate": quate,
                "topics":posts,
                "carosels":carosels,
                "catagorys":catagorys,
                "populars":populars,
                "popular_tags": popular_tags
            }
            return render(request,'home.html',obj)
        except:
            return render(request,"error404.html")

class ArticleView(View):
    def get(self,request,id):
        try:
            comments = GetComment().get_comment(id)
            aside_datas = ArticleAside().get_sidebars(id)
            links = dict()
            for num,item in enumerate(aside_datas["topics"]):
                links[item.id] = num+1
            paginator = Paginator(list(links.keys()),1)
            try:
                page = request.GET['page']
                page = paginator.get_page(page)
            except:
                page = paginator.get_page(links.get(id,1))
            link = page.object_list[0]
            query = Query()
            topic = query.get_article(link)
            user = request.user
            obj = {
                "topic":topic,
                "comments":comments,
                "aside_datas":aside_datas,
                "page":page,
                "user": user
            }
            return render(request,'article.html',obj)
        except:
            return render(request,"error404.html",status=404)


class AddComment_View(View):
    def post(self,request):
        try:
            datas = request.POST
            comment = SaveComment()
            comment.save(datas)
            
            return redirect(to="/article/{}".format(datas['comment_post_ID']))
        except:
            return render(request,"error404.html")

def add_comment(request,*args,**kwargs):
    if request.method == 'POST':
        print('I am so luckey')
    return redirect(to="/article/hellow-there-how-are-you-another-new-things")


class AddReaply_View(View):
    def post(self,request):
        try:
            datas = request.POST
            comment = Comment.objects.get(id = datas["cmnt"])
            rply = CommentReaply(comment = comment,email = datas["email"],name= datas["name"],reaply = datas["reaply"])
            rply.save()
            
            obj = dict()
            obj['body'] = datas["reaply"]
            obj['receiver'] = comment.email
            print(obj)
            # send(obj)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except:
            return render(request,"error404.html")


class SubscriptionView(View):
    def post(self,request):
        try:
            email = request.POST['email']
            print(request.path)
            subscribe = Subscribe()
            subscribe.add_mail(email)
            return redirect(to="/")
        except:
            return render(request,"error404.html")

class CatagoryView(View):
    def get(self,request):
        try:
            datas = Catagory().all_catagory()
            return render(request,"catagory page.html",{"datas":datas})
        except:
            return render(request,"error404.html")
        
class SpacificCatagoryView(View):
    def get(self,request,id):
        try:
            data =  Catagory().spacific_catagory(id)
            return render(request,"catagory page.html",{"datas":data})
        except:
            return render(request,"error404.html")


class PrivacyView(View):
    def get(self,request):
        try:
            return render(request,"privacy.html",)
        except:
            return render(request,"error404.html")