from django.shortcuts import render,redirect
from siteadmin.models import *
from siteuser.models import *
from django.contrib import messages
import datetime
from django.http import JsonResponse

# Create your views here.
def register(request):
    country = country_tb.objects.all()
    hobbie = hobbiename_tb.objects.all()
    state = state_tb.objects.all()
    return render(request,'register.html',{'country':country,'hobbie1':hobbie,'state':state})
def getstate(request):
    cid = request.GET['country_id']
    state = state_tb.objects.filter(countryid=cid)
    return render(request,'getstate.html',{'state':state})

def registerAction(request):
    name = request.POST['name']
    address = request.POST['address']
    dob = request.POST['dob']
    country = request.POST['country']
    gender = request.POST['gender']
    state = request.POST['state']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    security = request.POST['question']
    answer = request.POST['answer']
    

    user = register_tb(name=name,address=address,dob=dob,country_id=country,gender=gender,state_id=state,phone=phone,username=username+'@mymail.com',password=password,security_question=security,answer=answer)
    user.save()
    hobbies = request.POST.getlist('hobbie')
    for vid in hobbies:
        hobbie1 = hobbie_tb(userid_id=user.id,hobbieid_id=vid)
        hobbie1.save() 
    messages.add_message(request,messages.INFO,'Register Success') 
    return redirect('register')

def message(request):
    return render(request,'message.html')

def userhome(request):
    return render(request,'userhome.html')

def checkreceivername(request):
    receivername = request.GET['receiver']
    user = register_tb.objects.filter(username=receivername)
    if len(user)>0:
        msg='exist'
    else:
        msg='not exist'
        return JsonResponse({'valid':msg})

def messageAction(request):
    senderid = request.session['id']
    receiverid = request.POST['receiver']
    receiver1 = register_tb.objects.get(username=receiverid)
    subject = request.POST['subject']
    message = request.POST['message']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    message = message_tb(senderid_id=senderid,receiverid=receiver1,subject=subject,message=message,date=date,time=time)
    message.save()
    messages.add_message(request,messages.INFO,'Message sent')
    return redirect('message')

def viewmsg(request):
    senderid = request.session['id']
    status = ['pending','deleted by receiver']
    agefactors = customeragefactor_tb.objects.filter(userid=senderid)
    for factor in agefactors:
        msg = message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factor_name).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus='filtered')    

    hobbiefactors = customerhobbiefactor_tb.objects.filter(userid=senderid)
    for hobbie in hobbiefactors:
        msg3 = message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factor_name).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus='filtered')
    
    seasonfactors = customercountryfactor_tb.objects.filter(userid=senderid)
    for country in seasonfactors:
        msg4 = message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factor_name).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus='filtered')

    contact = contact_tb.objects.filter(userid=senderid)
    for c in contact:
        msg2 = message_tb.objects.filter(receiverid=senderid,filterstatus='pending',senderid=c.contactid).update(filterstatus='filtered')
    msg1 = message_tb.objects.filter(receiverid=senderid,status__in=status,filterstatus='filtered').exclude(id__in=trash_tb.objects.filter(receiver=senderid).values('message_id'))
    return render(request,'viewmsg.html',{'msg':msg1})
    # before aplying filter
        # msg = message_tb.objects.filter(senderid=senderid,status__in=status).exclude(id__in=trash_tb.objects.filter(receiver=senderid).values('message_id'))
        



def delete(request,id):
    message = message_tb.objects.filter(id=id)
    status = message[0].status
    if status == 'deleted by reciever':
        msg = message_tb.objects.filter(id=id).delete()
        return redirect('viewmsg')
    if status == 'pending':
        msg1 = message_tb.objects.filter(id=id).update(status='deleted by sender')
    messages.add_message(request,messages.INFO,'Message Deleted')
    return redirect('viewmsg')



    
def trash(request):
    senderid = request.session['id']
    status = ['pending','deleted by sender']
    trash = message_tb.objects.filter(receiverid=senderid,status__in=status)
    # msg1 = message_tb.objects.all()
    return render(request,'trash.html',{'msg':trash})

def movetotrash(request):
    check = request.POST.getlist('checkbox')
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    for cid in check:
        msg_obj = message_tb.objects.get(id=cid)
        senderid = request.session['id']
        trash = trash_tb(receiver_id=senderid,message=msg_obj,date=date,time=time)
        trash.save()
        messages.add_message(request,messages.INFO,'moved to trash')
    return redirect('trash')

def movetrash(request):
    senderid = request.session['id']
    trash = trash_tb.objects.filter(receiver_id=senderid)
    return render(request,'movetrash.html',{'trash':trash})

def delete1(request,id):
    trash = trash_tb.objects.filter(id=id)
    message = message_tb.objects.filter(id=trash[0].message_id)
    status = message[0].status
    if status == 'pending':
        message1 = message_tb.objects.filter(id=trash[0].message_id).update(status='deleted by receiver')
        # update = message_tb.objects.filter(id=id).delete()
        trash1 = trash_tb.objects.filter(id=id).delete()
    return redirect('movetrash')

def forward(request,id):
    
    forward = message_tb.objects.filter(id=id)
    return render(request,'forward.html',{'frwd':forward})


def checkreceivername(request):
    receiver = request.GET['receiver']
    user = register_tb.objects.filter(username=receiver)
    if len(user)>0:
        msg='exist'
    else:
        msg='not exist'
        return JsonResponse({'valid':msg})

def forwardAction(request):
    senderid = request.session['id']
    receiverid = request.POST['receiver']
    receiver1 = register_tb.objects.get(username=receiverid)
    subject = request.POST['subject']
    message = request.POST['message']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    user = message_tb(senderid_id=senderid,receiverid=receiver1,subject=subject,message=message,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'Message forward')
    return redirect('viewmsg')

def reply(request,id):
    reply = message_tb.objects.filter(id=id)
    return render(request,'reply.html',{'reply':reply})
def replyAction(request):
    senderid = request.session['id']
    receiverid = request.POST['receiver']
    receiver1 = register_tb.objects.get(username=receiverid)
    subject = request.POST['subject']
    message = request.POST['message']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    user = message_tb(senderid_id=senderid,receiverid=receiver1,subject=subject,message=message,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'Message Replied')
    return redirect('viewmsg')


def contact(request):
    return render(request,'contact.html')

def checkcontactname(request):
    username = request.GET['username']
    user = register_tb.objects.filter(username=username)
    if len(user)>0:
        msg = 'exist'
    else:
        msg = 'not exist'
        return JsonResponse({'valid':msg})

def contactAction(request):
    senderid = request.session['id']
    userid1 = request.POST['username']
    userid = register_tb.objects.get(username=userid1)
    name= request.POST['name']
    remarks = request.POST['remarks']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    user = contact_tb(userid_id=senderid,contactid=userid,name=name,remarks=remarks,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'Contact Created')
    return redirect('contact')

def blacklist(request):
    return render(request,'blacklist.html')

def checkblacklist(request):
    blacklist = request.GET['username']
    user = register_tb.objects.filter(username=blacklist)
    if len(user)>0:
        msg = 'exist'
    else:
        msg = 'not exist'
        return JsonResponse({'valid':msg})

def blacklistAction(request):
    senderid = request.session['id']
    username = request.POST['username']
    username1 = register_tb.objects.get(username=username)
    name= request.POST['name']
    remarks = request.POST['remarks']
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    user = blacklist_tb(userid_id=senderid,contactid=username1,name=name,remarks=remarks,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'Contact Added to Blacklist')
    return redirect('blacklist')

def viewcontact(request):
    senderid = request.session['id']
    user = contact_tb.objects.filter(userid=senderid)
    return render(request,'viewcontact.html',{'user':user})

def delete3(request,id):
    delete3 = contact_tb.objects.filter(id=id).delete()
    return redirect('viewcontact')

def viewblacklist(request):
    senderid = request.session['id']
    user = blacklist_tb.objects.filter(userid=senderid)
    return render(request,'viewblacklist.html',{'user':user})
def delete4(request,id):
    delete4 = blacklist_tb.objects.filter(id=id).delete()
    return redirect('viewblacklist')

def movetoblacklist(request,id):
    senderid = request.session['id']
    contact = contact_tb.objects.filter(id=id)
    contactid = contact[0].contactid
    name = contact[0].name
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M')
    remarks = contact[0].remarks
    user = blacklist_tb(userid_id=senderid,contactid=contactid,name=name,date=date,time=time,remarks=remarks)
    user.save()
    messages.add_message(request,messages.INFO,'Moved to blacklist')
    contact.delete() 
    return redirect('viewcontact')

def customerhobbiefactor(request):
    senderid = request.session['id']
    user = hobbie_tb.objects.filter(userid=senderid)
    return render(request,'customerhobbiefactor.html',{'user':user})

def getfactor1(request):
    cid = request.GET['hobbie']
    factor = hobbiefactor_tb.objects.filter(hobbie_id=cid)
    return render(request,'getfactor1.html',{'factor':factor})

def costumerAction(request):
    senderid = request.session['id']
    hobbieid = request.POST['hobbie']
    factorid= request.POST['factor']
    user = customerhobbiefactor_tb(userid_id=senderid,hobbieid_id=hobbieid,factorid_id=factorid)
    user.save()
    messages.add_message(request,messages.INFO,'Added successfully')
    return redirect('customerhobbiefactor')

def customeragefactor(request):
    senderid =request.session['id']
    user = register_tb.objects.filter(id=senderid)
    birthdate = user[0].dob
    by = birthdate.split('-')
    byear = by[0]
    date = datetime.date.today()
    bdate = date.year
    age = bdate-int(byear)
    user1 = age_tb.objects.filter(min_age__lte=age,max_age__gte=age)
    return render(request,'customeragefactor.html',{'user1':user1})

def ageAction1(request):
    senderid = request.session['id']
    factorid = request.POST['factor']
    user = customeragefactor_tb(userid_id=senderid,factorid_id=factorid)
    user.save()
    messages.add_message(request,messages.INFO,'Added Successfully')
    return redirect('customeragefactor')

def customercountryfactor(request):
    senderid = request.session['id']
    user = register_tb.objects.filter(id=senderid)
    country = user[0].country
    state = user[0].state
    date = datetime.date.today()
    month = date.month
    user1 = seasoncountry_tb.objects.filter(countryid_id=country,stateid_id=state,month=month)
    return render(request,'customercountryfactor.html',{'user':user1})

def countryAction1(request):
    senderid = request.session['id']
    factorid = request.POST['factor']
    user = customercountryfactor_tb(userid_id=senderid,factorid_id=factorid)
    user.save()
    messages.add_message(request,messages.INFO,'Added Successfully')
    return redirect('customercountryfactor')

def viewspam(request):
    status = ['deleted by sender','pending']
    msg = message_tb.objects.filter(filterstatus='pending',status__in=status)
    return render(request,'viewapam.html',{'msg':msg})

def delete5(request,id):
    message = message_tb.objects.filter(id=id)
    status = message[0].status
    if status == 'deleted by sender':
        msg = message_tb.objects.filter(id=id).delete()
        return redirect('viewspam')
    else:
        msg1 = message_tb.objects.filter(id=id).update(status='deleted by receiver')
        messages.add_message(request,messages.INFO,'Spam Deleted')
        return redirect('viewspam')

def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,'Logout success')
    return redirect('index')


def forgot(request):
    return render(request,'forgotpassword.html')

def forgotAction(request):
    username = request.POST['username']
    user = register_tb.objects.filter(username=username)
    if user.count()>0:
        user = register_tb.objects.filter(username=username)
        request.session['id']=user[0].id
        vid = request.session['id']
        user = register_tb.objects.filter(id=vid)
        country = country_tb.objects.all()
        return render(request,'newpassword.html',{'user':user,'country':country})
    else:
        messages.add_message(request,message.INFO,'message')
        return redirect('login')

def newpasswordAction(request):
    # username=request.POST['username']
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    user = register_tb.objects.filter(name=name,dob=dob,country=country)
    if user.count()>0:
        request.session['id']=user[0].id
        return render(request,'enternewpassword.html',{'user':user})
    else:
        return redirect('login')

    #     messages.add_message(request,messages.INFO,'failed')
        

def enternewAction(request):
    # username=request.POST['username']
    npassword=request.POST['password']
    cpassword=request.POST['confirmpassword']
    # user = register_tb.objects.filter(username=username)
    if npassword==cpassword:
            userid = request.session['id']
            user = register_tb.objects.filter(id=userid).update(password=npassword)
            messages.add_message(request,messages.INFO,"password changed succussfuly")
            request.session.flush()
            return redirect('index')
    else:
        return render(request,'enternewpassword.html')

def update(request):
    senderid = request.session['id']
    country = country_tb.objects.all()
    state = state_tb.objects.all()
    hobbies = hobbiename_tb.objects.all()
    hobbie = hobbie_tb.objects.filter(userid=senderid)
    user = register_tb.objects.filter(id=senderid)
    return render(request,'updateuser.html',{'user':user,'country':country,'state':state,'hobbies':hobbies,'hobbie':hobbie})

def getstate(request):
    cid = request.GET['country_id']
    state = state_tb.objects.filter(countryid=cid)
    return render(request,'getstate.html',{'state':state})

def updateAction(request):
    senderid = request.session['id']
    user = register_tb.objects.filter(id=senderid)
    name = request.POST['name']
    address = request.POST['address']
    gender = request.POST['gender']
    dob = request.POST['dob']
    country = request.POST['country']
    state = request.POST['state']
    hobbie = request.POST['hobbie']
    phone = request.POST['phone']
    question = request.POST['question']
    answer = request.POST['answer']
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb.objects.filter(id=senderid).update(name=name,address=address,dob=dob,country_id=country,gender=gender,state_id=state,phone=phone,username=username+'@mymail.com',password=password,security_question=question,answer=answer)
    messages.add_message(request,messages.INFO,'updated successfully')
    return render(request,'userhome.html')