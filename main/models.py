from django.db import models
from django.utils.timezone import now

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    slug=models.SlugField(max_length=150, unique=True, db_index=True)
    createdate = models.DateTimeField(default=now)

    class Meta:
        ordering = ('createdate',)

class Videos(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='videos', on_delete=models.CASCADE,default=None,null=True,blank=True)
    video_id = models.CharField(max_length=100, default=None, null=True, blank=True)
    title = models.CharField(max_length=100, default=None, null=True, blank=True)
    video_date = models.DateTimeField(default=now)

    class Meta:
        ordering=('video_date',)

class Photos(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE,default=None,null=True,blank=True)
    image_file = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=100, default=None, null=True, blank=True)
    image_date = models.DateTimeField(default=now)

    class Meta:
        ordering=('image_date',)

class News(models.Model):
    title = models.CharField(max_length=500, default=None, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='news_thumb/%Y/%m/%d', blank=True)
    content = models.TextField(default=None)
    news_date = models.DateTimeField(default=now)

    class Meta:
        ordering=('-news_date',)

class NewsLetter(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    email = models.EmailField(max_length=254)
    news_date = models.DateTimeField(default=now)

    class Meta:
        ordering=('name',)


class Banner(models.Model):
    image_file = models.ImageField(upload_to='banner/%Y/%m/%d', blank=True)
    caption = models.CharField(max_length=500, default=None, null=True, blank=True)


class Donations(models.Model):
    fullname = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=254)
    address = models.TextField(default=None)
    city = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    dob = models.DateField(default=None)
    donation_date = models.DateTimeField(auto_now_add=True)
    pan_no = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    txnid = models.CharField(max_length=100, default=None, null=True, blank=True)
    currency = models.CharField(max_length=10, default=None, null=True, blank=True)
    gateway = models.CharField(max_length=100, default=None, null=True, blank=True)
    response = models.CharField(max_length=100, default=None, null=True, blank=True)
    bankname = models.CharField(max_length=100, default=None, null=True, blank=True)
    paymentmode = models.CharField(max_length=100, default=None, null=True, blank=True)
    responsecode = models.CharField(max_length=100, default=None, null=True, blank=True)
    bank_transaction_id = models.CharField(max_length=100, default=None, null=True, blank=True)
    transaction_date = models.CharField(max_length=100,default=None, null=True, blank=True)
    done = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering=('donation_date',)

class Ministers(models.Model):
    name = models.CharField(max_length=100,default=None, null=True, blank=True)
    rank = models.PositiveIntegerField(default=1000,)
    role = models.CharField(max_length=100,default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    image = models.ImageField(upload_to='minister/%Y/%m/%d', blank=True)
    fblink = models.CharField(max_length=100,default=None, null=True, blank=True)
    twitterlink = models.CharField(max_length=100,default=None, null=True, blank=True)
    linkedinlink = models.CharField(max_length=100,default=None, null=True, blank=True)
    address = models.CharField(max_length=100,default=None, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20,default=None, null=True, blank=True)
    executive = models.BooleanField(default = False)

    class Meta:
        ordering=("rank",)

class sitesocial(models.Model):
    fblink = models.CharField(max_length=100,default=None, null=True, blank=True)
    twitterlink = models.CharField(max_length=100,default=None, null=True, blank=True)
    instalink = models.CharField(max_length=100,default=None, null=True, blank=True)
    linkedlink = models.CharField(max_length=100,default=None, null=True, blank=True)
    ytlink = models.CharField(max_length=100,default=None, null=True, blank=True)

class Member(models.Model):
    fullname = models.CharField(max_length=100,default=None, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100,default=None, null=True, blank=True)
    dob = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=10,default=None, null=True, blank=True)
    state = models.CharField(max_length=100,default=None, null=True, blank=True)
    city = models.CharField(max_length=100,default=None, null=True, blank=True)
    address = models.CharField(max_length=500,default=None, null=True, blank=True)
    pincode = models.CharField(max_length=100,default=None, null=True, blank=True)
    voterid = models.CharField(max_length=100,default=None, null=True, blank=True)
    joindate = models.DateTimeField(auto_now_add=True)
    volunteer = models.BooleanField(default=False)
    contribute = models.CharField(max_length=500,default=None, null=True, blank=True)
    aboutself = models.TextField(default = None, null=True, blank=True)

    class Meta:
        ordering=('-joindate',)

class Intern(models.Model):
    fullname = models.CharField(max_length=100,default=None, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100,default=None, null=True, blank=True)
    duration = models.CharField(max_length=100,default=None, null=True, blank=True)
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=100,default=None, null=True, blank=True)
    city = models.CharField(max_length=100,default=None, null=True, blank=True)
    college = models.CharField(max_length=200,default=None, null=True, blank=True)
    course = models.CharField(max_length=100,default=None, null=True, blank=True)
    interest = models.CharField(max_length=100,default=None, null=True, blank=True)
    laptop = models.CharField(max_length=100,default=None, null=True, blank=True)
    startdate = models.DateField(default=None)
    applydate = models.DateTimeField(auto_now_add=True) 
    resume = models.FileField(upload_to="resumes/%Y/%m/%d", blank=True)

    class Meta:
        ordering=('applydate',)