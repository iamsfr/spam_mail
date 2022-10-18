from django.db import models

# Create your models here.
class country_tb(models.Model):
    name = models.CharField(max_length=50)

class state_tb(models.Model):
    state = models.CharField(max_length=100)
    countryid = models.ForeignKey(country_tb, on_delete=models.CASCADE)




class register_tb(models.Model):
    name = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    dob = models.CharField( max_length=50)
    gender = models.CharField( max_length=50,default='abc')
    country = models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state = models.ForeignKey(state_tb, on_delete=models.CASCADE)
    phone = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    security_question = models.CharField( max_length=50)
    answer = models.CharField( max_length=50,default='abc')

class hobbie_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE)
    hobbieid = models.ForeignKey('siteadmin.hobbiename_tb', on_delete=models.CASCADE)

class message_tb(models.Model):
    senderid = models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='sender')
    subject = models.CharField( max_length=50)
    message = models.CharField( max_length=50)
    date = models.CharField( max_length=50)
    time = models.CharField( max_length=50)
    receiverid = models.ForeignKey(register_tb, on_delete=models.CASCADE,related_name='receiver')
    status = models.CharField( max_length=50,default='pending')
    filterstatus = models.CharField( max_length=50,default='pending')

class trash_tb(models.Model):
    message = models.ForeignKey(message_tb, on_delete=models.CASCADE)
    receiver = models.ForeignKey(register_tb, on_delete=models.CASCADE)
    date = models.CharField( max_length=50)
    time = models.CharField( max_length=50)

class contact_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE,related_name='userid')
    contactid = models.ForeignKey(register_tb, on_delete=models.CASCADE,related_name='contactid')
    name = models.CharField( max_length=50)
    date = models.CharField( max_length=50)
    time =  models.CharField( max_length=50)
    remarks = models.CharField( max_length=50)

class blacklist_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE,related_name='userid1')
    contactid = models.ForeignKey(register_tb, on_delete=models.CASCADE,related_name='contactid1')
    name = models.CharField( max_length=50)
    date = models.CharField( max_length=50)
    time = models.CharField( max_length=50)
    remarks = models.CharField( max_length=50)

class customerhobbiefactor_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE)
    hobbieid = models.ForeignKey('siteadmin.hobbiename_tb', on_delete=models.CASCADE)
    factorid = models.ForeignKey("siteadmin.hobbiefactor_tb", on_delete=models.CASCADE)

class customeragefactor_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE)
    factorid = models.ForeignKey('siteadmin.age_tb', on_delete=models.CASCADE)

class customercountryfactor_tb(models.Model):
    userid = models.ForeignKey(register_tb, on_delete=models.CASCADE)
    factorid = models.ForeignKey('siteadmin.seasoncountry_tb', on_delete=models.CASCADE)
