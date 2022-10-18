from django.shortcuts import render,redirect
from siteadmin.models import *
from siteuser.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def adminhome(request):
    return render(request,'home.html')

def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    admin = admin_tb.objects.filter(username=username,password=password)
    user = register_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,'home.html',{'admin':admin})
    elif user.count()>0:
        request.session['id']=user[0].id
        return render(request,'userhome.html',{'user':user})
    else:
        return redirect('login')

def hobbie(request):
    return render(request,'hobbie.html')

def hobbieAction(request):
    hname = request.POST['hobbie']
    hobbies = hobbiename_tb(name=hname)
    hobbies.save()
    messages.add_message(request,messages.INFO,'Hobbies Added')
    return redirect('hobbie')

def factor(request):
    hobbie = hobbiename_tb.objects.all()
    return render(request,'factor.html',{'hobbie':hobbie})

def factorAction(request):
    factor = request.POST['factorname']
    hobbie = request.POST['hobbie']
    factors = hobbiefactor_tb(factor_name=factor,hobbie_id_id=hobbie)
    factors.save()
    messages.add_message(request,messages.INFO,'factor Added')
    return redirect('factor')

def checkusername(request):
    username = request.GET['username']
    username1 = username+'@mymail.com'
    user = register_tb.objects.filter(username=username1)
    if len(user)>0:
        msg='exist'
    else:
        msg='not exist'
    return JsonResponse({'valid':msg})

def season(request):
    return render(request,'season.html')

def seasonAction(request):
    season = request.POST['season']
    seasons = season_tb(name=season)
    seasons.save()
    messages.add_message(request,messages.INFO,'season Added')
    return redirect('season')

def seasonfactor(request):
    season = season_tb.objects.all()
    return render(request,'seasonfactor.html',{'season':season})
def seasonfactorAction(request):
    season = request.POST['seasonfactor']
    factorname = request.POST['factorname']
    factors = seasonfactor_tb(seasonid_id=season,factor_name=factorname)
    factors.save()
    messages.add_message(request,messages.INFO,'Factor Added')
    return redirect('seasonfactor')

def seasoncountry(request):
    season = season_tb.objects.all()
    country = country_tb.objects.all()
    return render(request,'seasoncountry.html',{'season':season,'country':country})

def getstate1(request):
    cid = request.GET['country_id']
    state = state_tb.objects.filter(countryid=cid)
    return render(request,'getstate1.html',{'state':state})
def getfactor(request):
    sid = request.GET['season_id']
    factor = seasonfactor_tb.objects.filter(seasonid=sid)
    return render(request,'getfactor.html',{'factor':factor})

def seasoncountryAction(request):
    season = request.POST['season']
    factor = request.POST['factor']
    country = request.POST['country']
    state = request.POST['state']
    month = request.POST['months']
    user = seasoncountry_tb(seasonid_id=season,factorid_id=factor,countryid_id=country,stateid_id=state,month=month)
    user.save()
    messages.add_message(request,messages.INFO,'successfully Added')
    return redirect('seasoncountry')
def age(request):
    return render(request,'age.html')

def ageAction(request):
    min = request.POST['minimum']
    max = request.POST['maximum']
    factor = request.POST['factor']
    factors = age_tb(min_age=min,max_age=max,factor_name=factor)
    factors.save()
    messages.add_message(request,messages.INFO,'succussfully added')
    return redirect('age')

def logout1(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,'Logout success')
    return redirect('index')


