from .models import CommentReaply, Quate,Topic,SubCatagory,Catagory,Comment,Subscribers
import random
class Query():
    def get_quate(self):
        try:
            count = Quate.objects.all().count()
            return Quate.objects.get(id=random.randint(1, count))
        except:
            return ""

    def get_carosels(self):
        try:
            carosel = []
            sub_catagorys =SubCatagory.objects.all()
            for sub_catagory in sub_catagorys:
                carosel_data = dict()
                carosel_data.update(sub_catagory.__dict__)
                try:
                    link = Topic.objects.filter(sub_catagory_id = sub_catagory.id)[:1][0]
                    carosel_data["link"] = link.id
                    
                except:
                    carosel_data["link"] = 1
                finally:
                    carosel.append(carosel_data)
                    
                    
            return carosel
        except:
            return []

    def get_catagories(self):
        try:
            return Catagory.objects.all()
        except:
            return []
    
    def popular_tag(self):
        try:
            return SubCatagory.objects.all()
        except:
            return []

    def sub_catagorys(self):
        article_info = []
        try:
            topics = Topic.objects.all()
            for topic in topics:
                datas = dict()
                
                sub_catagory = SubCatagory.objects.get(id = topic.sub_catagory_id)
                comment_no = Comment.objects.filter(topic_id = topic.id).count()
                datas.update(sub_catagory.__dict__)
                datas.update(topic.__dict__)
                datas["comment_no"] = comment_no
                article_info.append(datas)

            return article_info
        except:
            return []

    def get_article(self,id):
        datas = dict()
        try:
            topics = Topic.objects.get(id = id)
            datas.update(topics.__dict__)
            comment_no = Comment.objects.filter(topic_id = id).count()
            datas["comment_no"] = comment_no
            topics.read_times += 1
            topics.save()
            return datas
        except:
            return datas

    def get_popular_articles(self):

        article_info = []
        try:
            topics = Topic.objects.all()
            for topic in topics:
                datas = dict()
                sub_catagory = SubCatagory.objects.get(id = topic.sub_catagory_id)
                comment_no = Comment.objects.filter(topic_id = topic.id).count()
                datas.update(sub_catagory.__dict__)
                datas.update(topic.__dict__)
                datas["comment_no"] = comment_no
                article_info.append(datas)

            article_info.sort(key= lambda x : x.read_times,reverse=True)
            return article_info
        except:
            return article_info


class SaveComment():
    def save(self,obj):
        try:
            topic = Topic.objects.get(id = obj["comment_post_ID"])
            comment = Comment(topic = topic, name  =obj["comment_author"],email = obj["email"], comment = obj["comment"])
            comment.save()
            return
        except:
            return

class GetComment():
    def get_comment(self,id):
        try:
            comments = []
            comment = Comment.objects.filter(topic_id = id)
            for x in comment:
                temp = dict()
                reaplies = CommentReaply.objects.filter(comment_id = x.id)
                temp["comment"] = x
                temp["reaplies"] = reaplies
                comments.append(temp)

            return comments
        except:
            return []

class ArticleAside():
    def get_sidebars(self,id):
        aside_datas = dict()
        try:
            subcatagory_id = Topic.objects.get(id = id).sub_catagory_id
            sub_catagory = SubCatagory.objects.get(id = subcatagory_id )
            aside_datas["sub_catagory_name"] = sub_catagory.sub_catagory_name
            
            topics = Topic.objects.filter(sub_catagory_id = subcatagory_id).order_by("date_created")
            aside_datas["topics"] = topics
            return aside_datas
        except:
            return aside_datas

class Subscribe():
    def add_mail(self,mail):
        try:
            print("I am working",mail)
            subs = Subscribers(email = mail)
            subs.save()
            return
        except:
            return

class Catagory():
    def all_catagory(self):
        data = dict()
        try:
            catagorys = Catagory.objects.all()
            for catagory in catagorys:
                try:
                    sub_catagories = SubCatagory.objects.filter(catagory_id = catagory.id)

                    carosel = []

                    for sub_catagory in sub_catagories:
                        carosel_data = dict()
                        carosel_data.update(sub_catagory.__dict__)
                        try:
                            link = Topic.objects.filter(sub_catagory_id = sub_catagory.id)[:1][0]
                            carosel_data["link"] = link.id
                            
                        except:
                            carosel_data["link"] = 1
                        finally:
                            carosel.append(carosel_data)
                        
                    data[catagory.catagory_name] = carosel
                except:
                    continue

            return data
        except:
            return data
    
    def spacific_catagory(self,id):
        data = dict()
        try:
            catagory = Catagory.objects.get(id=id)
            try:
                sub_catagories = SubCatagory.objects.filter(catagory_id = catagory.id)
                data[catagory.catagory_name] = sub_catagories
            except:
                return data

            return data
        except:
            return data
