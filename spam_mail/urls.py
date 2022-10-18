"""spam_mail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from siteadmin import views as siteadmin
from siteuser import views as siteuser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',siteadmin.index,name='index'),
    path('userhome/',siteuser.userhome,name='userhome'),
    path('adminhome/',siteadmin.adminhome,name='adminhome'),

    path('login/',siteadmin.login,name='login'),
    path('loginAction/',siteadmin.loginAction,name='loginAction'),
    path('hobbie/',siteadmin.hobbie,name='hobbie'),
    path('hobbieAction/',siteadmin.hobbieAction,name='hobbieAction'),
    path('register/',siteuser.register,name='register'),
    path('getstate/',siteuser.getstate,name='getstate'),
    path('registerAction/',siteuser.registerAction,name='registerAction'),
    path('factor/',siteadmin.factor,name='factor'),
    path('factorAction/',siteadmin.factorAction,name='factorAction'),
    path('checkusername/',siteadmin.checkusername,name='checkusername'),
    path('season/',siteadmin.season,name='season'),
    path('seasonAction/',siteadmin.seasonAction,name='seasonAction'),
    path('seasonfactor/',siteadmin.seasonfactor,name='seasonfactor'),
    path('seasonfactorAction/',siteadmin.seasonfactorAction,name='seasonfactorAction'),
    path('seasoncountry/',siteadmin.seasoncountry,name='seasoncountry'),
    path('getstate1/',siteadmin.getstate1,name='getstate1'),
    path('getfactor',siteadmin.getfactor,name='getfactor'),
    path('seasoncountryAction/',siteadmin.seasoncountryAction,name='seasoncountryAction'),
    path('age/',siteadmin.age,name='age'),
    path('ageAction/',siteadmin.ageAction,name='ageAction'),
    path('message/',siteuser.message,name='message'),
    path('checkreceivername/',siteuser.checkreceivername,name='checkreceivername'),
    path('messageAction/',siteuser.messageAction,name='messageAction'),
    path('viewmsg/',siteuser.viewmsg,name='viewmsg'),
    path('delete/<int:id>',siteuser.delete,name='delete'),
    path('trash/',siteuser.trash,name='trash'),
    path('movetotrash/',siteuser.movetotrash,name='movetotrash'),
    path('movetrash/',siteuser.movetrash,name='movetrash'),
    path('delete1/<int:id>',siteuser.delete1,name='delete1'),
    path('forward/<int:id>',siteuser.forward,name='forward'),
    path('checkreceivername/',siteuser.checkreceivername,name='checkreceivername'),
    path('forwardAction/',siteuser.forwardAction,name='forwardAction'),
    path('reply<int:id>/',siteuser.reply,name='reply'),
    path('replyAction/',siteuser.replyAction,name='replyAction'),
    path('contact/',siteuser.contact,name='contact'),
    path('checkcontactname/',siteuser.checkcontactname,name='checkcontactname'),
    path('contactAction/',siteuser.contactAction,name='contactAction'),
    path('blacklist/',siteuser.blacklist,name='blacklist'),
    path('checkblacklist/',siteuser.checkblacklist,name='checkblacklist'),
    path('blacklistAction/',siteuser.blacklistAction,name='blacklistAction'),
    path('viewcontact/',siteuser.viewcontact,name='viewcontact'),
    path('delete3/<int:id>',siteuser.delete3,name='delete3'),
    path('viewblacklist/',siteuser.viewblacklist,name='viewblacklist'),
    path('delete4/<int:id>',siteuser.delete4,name='delete4'),
    path('movetoblacklist/<int:id>',siteuser.movetoblacklist,name='movetoblacklist'),
    path('customerhobbiefactor/',siteuser.customerhobbiefactor,name='customerhobbiefactor'),
    path('getfactor1/',siteuser.getfactor1,name='getfactor1'),
    path('costumerAction/',siteuser.costumerAction,name='costumerAction'),
    path('customeragefactor/',siteuser.customeragefactor,name='customeragefactor'),
    path('ageAction1/',siteuser.ageAction1,name='ageAction1'),
    path('customercountryfactor/',siteuser.customercountryfactor,name='customercountryfactor'),
    path('countryAction1/',siteuser.countryAction1,name='countryAction1'),
    path('viewspam/',siteuser.viewspam,name='viewspam'),
    path('delete5/<int:id>',siteuser.delete5,name='delete5'),
    path('logout/',siteuser.logout,name='logout'),
    path('logout1/',siteadmin.logout1,name='logout1'),
    path('forgot/',siteuser.forgot,name='forgot'),
    path('forgotAction/',siteuser.forgotAction,name='forgotAction'),
    path('newpasswordAction/',siteuser.newpasswordAction,name='newpasswordAction'),
    path('enternewAction/',siteuser.enternewAction,name='enternewAction'),
    path('update/',siteuser.update,name='update'),
    path('updateAction/',siteuser.updateAction,name='updateAction')
    

    
    













]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)