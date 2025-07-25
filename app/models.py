from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    usertype=models.CharField(max_length=500)


class Ration_office(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    image=models.CharField(max_length=2000)


class Voter_office(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    image=models.CharField(max_length=2000)


class Mvd_office(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    image=models.CharField(max_length=1000)
    

class Aadhaar_office(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    image=models.CharField(max_length=1000)


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    image=models.CharField(max_length=1000)
    gender=models.CharField(max_length=500)
    housename=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    pin=models.CharField(max_length=500)
    dob=models.CharField(max_length=500)


class Feedback(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    feedback=models.CharField(max_length=500)
    usertype=models.CharField(max_length=500)

class Aadhaarcard(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=500, default='pending')
    image=models.CharField(max_length=2000)
    number=models.CharField(max_length=500)

class Licence(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=500, default='pending')
    image=models.CharField(max_length=2000)
    number=models.CharField(max_length=500)

class Rationcard(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=500, default='pending')
    image = models.CharField(max_length=2000)
    number = models.CharField(max_length=500)

class FamilyMember(models.Model):
    rationcard = models.ForeignKey(Rationcard, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Voterid(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=500, default='pending')
    image=models.CharField(max_length=2000)
    number=models.CharField(max_length=500)

    
class Alphacard(models.Model):
    RATION=models.ForeignKey(Rationcard,on_delete=models.CASCADE, null=True)
    AADHAARCARD=models.ForeignKey(Aadhaarcard,on_delete=models.CASCADE, null=True)
    VOTERID=models.ForeignKey(Voterid,on_delete=models.CASCADE, null=True)
    LICENCE=models.ForeignKey(Licence,on_delete=models.CASCADE, null=True)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    alphanumber=models.CharField(max_length=500)

class Applyalphacard_request(models.Model):
    USER=models.ForeignKey(User ,on_delete=models.CASCADE)
    description=models.CharField(max_length=2000)
    date=models.DateField(auto_now=True)
    status=models.CharField(max_length=100)

    



