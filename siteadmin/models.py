from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
class hobbiename_tb(models.Model):
    name = models.CharField( max_length=50)

class hobbiefactor_tb(models.Model):
    factor_name = models.CharField(max_length=50)
    hobbie_id = models.ForeignKey("hobbiename_tb", on_delete=models.CASCADE)

class season_tb(models.Model):
    name = models.CharField( max_length=50)

class seasonfactor_tb(models.Model):
    factor_name = models.CharField( max_length=50)
    seasonid = models.ForeignKey('season_tb', on_delete=models.CASCADE)

class seasoncountry_tb(models.Model):
    seasonid = models.ForeignKey("season_tb", on_delete=models.CASCADE)
    countryid = models.ForeignKey("siteuser.country_tb",on_delete=models.CASCADE)
    stateid = models.ForeignKey("siteuser.state_tb", on_delete=models.CASCADE)
    factorid = models.ForeignKey("seasonfactor_tb", on_delete=models.CASCADE)
    month = models.IntegerField()
class age_tb(models.Model):
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    factor_name = models.CharField( max_length=50)
