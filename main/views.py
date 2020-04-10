from django.shortcuts import render, HttpResponse, redirect
from .models import Banner, News, Videos, Donations,Ministers, Member, Intern
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .paytm import Checksum
import random
import string
import smtplib

MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
MERCHAND_ID = settings.PAYTM_MERCHANT_ID

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    news = News.objects.all() 
    ministers = Ministers.objects.filter(executive=True)
    return render(request,"home.html", {'banners':banner, 'news':news, 'ministers':ministers})

def aboutus(request):
    title = "About us"
    return render(request, "aboutus.html", {'title':title})

def media(request):
    videos = Videos.objects.all()
    title = "Media"
    return render(request, "media.html", {'videos':videos, 'title':title})

def allvideos(request):
    videos = Videos.objects.all()
    title = "All Videos"
    return render(request, "allvideos.html", {'videos':videos, 'title':title})

def allphotos(request):
    title="All Photos"
    return render(request, "allphotos.html",{'title':title})

def ourministers(request):
    ministers = Ministers.objects.all()
    title = "Our Ministers"
    return render(request, "ourministers.html", {'ministers':ministers, 'title':title})

def minprofile(request,mid):
    minister = Ministers.objects.get(id=mid)
    title=minister.name
    return render(request, "ministerprofile.html", {'minister':minister,'title':title})

def videoplayer(request, vid):
    videos = Videos.objects.all()
    return render(request, "videoplayer.html", {'vid':vid, 'videos':videos})

def imageviewer(request):
    return render(request, "imageviewer.html")

def donationform(request):
    title="Donate"
    return render(request, "donationform.html",{'title':title})

def newsopen(request, nid):
    news = News.objects.get(id=nid)
    title = news.title
    return render(request, "news.html", {'news':news, 'title':title})

def allnews(request):
    news = News.objects.all()
    title="ALL News"
    return render(request, "allnews.html", {'news':news, 'title':title})

def join(request):
    title="Become a member"
    return render(request, "join.html", {'title':title})

def bemember(request):
    if request.method == "POST":
        fullname = request.POST.get("vname")
        email = request.POST.get("vemail")
        phone = request.POST.get("vphone")
        dob = request.POST.get("vdob")
        gender = request.POST.get("vgender")
        state = request.POST.get("vstate")
        city = request.POST.get("vcity")
        address = request.POST.get("vaddress")
        pincode = request.POST.get("vpin")
        formtype = request.POST.get("vtype")
        voterid = request.POST.get("vvoter")
        password = request.POST.get("vpassword")
        
        it = request.POST.get("vit")
        digital = request.POST.get("vdigital")
        party = request.POST.get("vparty")
        content = request.POST.get("vcontent")
        other = request.POST.get("vother")
        more = request.POST.get("vmore")

        volunteer = False
        if(formtype == "1"):
            volunteer=True

        contrib=""
        if(it):
            contrib = contrib+"IT support (coding, web design etc.)"+"%:%:%:%"
        
        if(digital):
            contrib = contrib + "Become a digital activist"+"%:%:%:%"
        
        if(party):
            contrib = contrib + "Attend party events"+"%:%:%:%"
        
        if(content):
            contrib = contrib + "Content writing (mention preferred language below)"+"%:%:%:%"
        
        if(other):
            contrib = contrib + "Other"

        mydict = {'fullname':fullname, 'email':email, 'phone':phone, 'dob':dob, 'gender':gender, 
            'state':state, 'city':city, 'address':address, 'pincode':pincode, 'voterid':voterid, 'volunteer':volunteer,
            'contribute':contrib, 'aboutself':more}

        #uu = User.objects.filter(username = email,email=email)
        #uu1 = Member.objects.filter(phone = phone)
        #if(len(uu)==0 and len(uu1) == 0):
         #   user = User.objects.create_user(username=email,first_name = fullname, email = email, password = password)
            
            #auth_login(request, user)

        p = Member(**mydict)
        p.save()

        if(volunteer == False):
            send_mail("adityanathtiwari25@gmail.com", "New member application"
            ,fullname+" applied to be a member.\n"+"Details:"+"\n"+"Name: "+ fullname + "\n" + "Email: " +email+"\n"+ "Phone: " + phone +
            "\n"+"State: "+state+"\n"+"City: "+city)
        else:
            send_mail("adityanathtiwari25@gmail.com", "New volunteer application" ,fullname+" applied to be a member.\n"+"Details:"+"\n"+"Name: "+ fullname + "\n" + "Email: " +email+"\n"+ "Phone: " + phone +
            "\n"+"State: "+state+"\n"+"City: "+city)
            
        return redirect("main:regthank")
        
        # else:
        #     messages.error(request, "Email ID or Phone number already exists")
        #     return render(request, 'join.html', {'formdata':mydict})
    else:
        return redirect("main:join")

def send_mail(receiver, subj ,message):
    sender_email = "adityanathtiwari62@gmail.com"
    rec_email = receiver
    passw = "cyfoesllp2020"
    msg = 'Subject: {}\n\n{}'.format(subj, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, passw)
    server.sendmail(sender_email, rec_email, msg)

def internsubmit(request):
    if request.method == "POST":
        fullname = request.POST.get("iname")
        email = request.POST.get("iemail")
        phone = request.POST.get("iphone")
        tsd = request.POST.get("itsd")
        duration = request.POST.get("iduration")
        state = request.POST.get("istate")
        city = request.POST.get("icity")
        course = request.POST.get("icourse")
        age = request.POST.get("iage")
        college = request.POST.get("icollege")
        interest = request.POST.get("iinterest")
        password = request.POST.get("vpassword")
        laptop = request.POST.get("ilaptop")
        
        resume = request.FILES["idoc"]

        mydict = {'fullname':fullname, 'email':email, 'phone':phone, 'duration':duration, 'age':age, 
            'state':state, 'city':city, 'college':college, 'course':course, 'interest':interest, 'laptop':laptop,
            'startdate':tsd, 'resume':resume}

        #uu = User.objects.filter(username = email,email=email)
        #uu1 = Member.objects.filter(phone = phone)
        #if(len(uu)==0 and len(uu1) == 0):
        #    user = User.objects.create_user(username=email,first_name = fullname, email = email, password = password)


        p = Intern(**mydict)
        p.save()

        send_mail("adityanathtiwari25@gmail.com", "New internship application" ,fullname+" applied to be a member.\n"+"Details:"+"\n"+"Name: "+ fullname + "\n" + "Email: " +email+"\n"+ "Phone: " + phone +
            "\n"+"State: "+state+"\n"+"City: "+city+"\n"+"Internship area: "+interest)

        return redirect("main:regthank")

        # else:
        #     messages.error(request, "Email ID or Phone number already exists")
        #     return render(request, 'join.html', {'formdata':mydict})
    
    else:
        return redirect("main:join")

def regthank(request):
    title="Thank you"
    return render(request, "registerthank.html",{'title':title})

def takedonation(request):
    if request.method == "POST":
        orandom = randomString(15)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        address = request.POST.get("address")
        amount = request.POST.get("amount")
        dob = request.POST.get("dob")
        pan = request.POST.get("pan")
        state = request.POST.get("state")

        donation = Donations()
        
        donation.fullname = name
        donation.mobilenumber = phone
        donation.orderid = orandom
        donation.emailid = email
        donation.phone = phone
        donation.city = city
        donation.address = address
        donation.amount = amount
        donation.dob = dob
        donation.pincode = pincode
        donation.pan_no = pan
        donation.state = state


        donation.save()

        param_dict = {
            'MID':MERCHAND_ID,
            'ORDER_ID':orandom,
            'TXN_AMOUNT':amount,
            'CUST_ID':orandom,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',
            }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        title="Payment"
        return render(request, 'payment.html',{'params_dict':param_dict,'title':title})
    
    else:
        #return render(request, "donationdone.html")
        return HttpResponse("Error!")

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == "CHECKSUMHASH":
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY ,checksum)
    if verify:
        ooid = request.POST.get('ORDERID')

        pay = Donations.objects.get(orderid = ooid)
        pay.currency = request.POST.get('CURRENCY')
        pay.gateway = request.POST.get('GATEWAYNAME')
        pay.response = request.POST.get('RESPMSG')
        pay.bankname = request.POST.get('BANKNAME')
        pay.paymentmode = request.POST.get('PAYMENTMODE')
        pay.responsecode = request.POST.get('RESPCODE')
        pay.txnid = request.POST.get('TXNID')
        pay.bank_transaction_id = request.POST.get('BANKTXNID')
        pay.transaction_date = request.POST.get('TXNDATE')

        if response_dict['RESPCODE'] == "01":
            pay.done = True
            pay.save();
            title="Payment Successful"
            return render(request, 'donationdone.html',{'response':response_dict,'title':title})
        else:
            pay.save();
            title="Payment Failed!"
            return render(request, "paymentfailed.html", {'response':response_dict, 'title':title})
    return HttpResponse("Transaction successful")
    pass