from django.urls import path,include
from .views import HomeView,ArticleView,AddReaply_View,AddComment_View,SubscriptionView,CatagoryView,PrivacyView,SpacificCatagoryView


app_name = 'articles'
urlpatterns = [
    path('',HomeView.as_view()),
    path('about',include("about.urls")),
    path('privacy',PrivacyView.as_view()),
    path('article/addcomment',AddComment_View.as_view(),name='add_comment'),
    path('article/addreaply',AddReaply_View.as_view(),name='add_reaply'),
    path('article/<slug:id>',ArticleView.as_view(),name = 'single_article'),
    path('motive/<int:id>',ArticleView.as_view()),

    path('subscribe',SubscriptionView.as_view()),
    path('catagory',CatagoryView.as_view()),
    path('catagory/<slug:id>',SpacificCatagoryView.as_view()),
    path('article/subscribe',SubscriptionView.as_view()),
    path('catagory/subscribe',SubscriptionView.as_view()),
    path('privacy/subscribe',SubscriptionView.as_view()),
    path('about/subscribe',SubscriptionView.as_view()),
    
]