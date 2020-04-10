from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path('', views.home, name="home"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('media', views.media, name="media"),
    path('allvideos', views.allvideos, name="allvideos"),
    path('allphotos', views.allphotos, name="allphotos"),
    path('ourministers', views.ourministers, name="ourministers"),
    path('minprofile/<mid>', views.minprofile, name="minprofile"),
    path('videoplayer/<vid>', views.videoplayer, name="videoplayer"),
    path('imageviewer', views.imageviewer, name="imageviewer"),
    path('donationform', views.donationform, name="donationform"),
    path('takedonation', views.takedonation, name="takedonation"),
    path('handlerequest', views.handlerequest, name="handlerequest"),
    path('newsopen/<nid>',views.newsopen, name="newsopen"),
    path('allnews', views.allnews, name="allnews"),
    path('join', views.join, name="join"),
    path('bemember', views.bemember, name="bemember"),
    path('regthank', views.regthank, name="regthank"),
    path('internsubmit', views.internsubmit, name="internsubmit"),
]