from django.contrib import admin
from .models import Gallery, Photos, Videos, Banner, News, NewsLetter, Donations, Ministers, sitesocial,Intern, Member
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Gallery,GalleryAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display=['video_id', 'title', 'video_date']

admin.site.register(Videos,VideoAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'image_file', 'title', 'image_date']

admin.site.register(Photos, PhotoAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'news_date']

admin.site.register(News, NewsAdmin)

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'news_date']

admin.site.register(NewsLetter, NewsLetterAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','image_file', 'caption']

admin.site.register(Banner, BannerAdmin)

class DonationsAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'txnid', 'state','done']

admin.site.register(Donations, DonationsAdmin)

class MinistersAdmin(admin.ModelAdmin):
    list_display = ['name', 'role','rank']
    list_editable = ['rank']

admin.site.register(Ministers, MinistersAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display = ['fblink']

admin.site.register(sitesocial, SocialAdmin)

class InternAdmin(admin.ModelAdmin):
    list_display=['fullname', 'email']

admin.site.register(Intern, InternAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'volunteer']

admin.site.register(Member, MemberAdmin)