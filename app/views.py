from django.shortcuts import render,HttpResponse
from .models import *
from django.shortcuts import render,redirect
import random
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import Login
from .models import Feedback
from django.contrib import messages
from django.shortcuts import render



# Create your views here.


def index(request):
    return render(request,'public/index.html')

# def login(request):
#     if 'submit' in request.POST:
#         username=request.POST['username']
#         password=request.POST['password']
        
#         if Login.objects.filter(username=username,password=password).exists():
#             q=Login.objects.get(username=username,password=password)
#             request.session['login_id']=q.pk
#             login_id=request.session['login_id']
#             if q.usertype=='admin':
#                 return HttpResponse(f"<script>alert('admin login success');window.location='/admin_home'</script>")
#             if q.usertype=='user':
#                 q1 = User.objects.get(LOGIN_id=login_id)
#                 if q1:
#                     request.session['user_id']=q1.pk
#                     return HttpResponse(f"<script>alert('user login success');window.location='/user_home'</script>")
#                 else:
#                     return HttpResponse(f"<script>alert('invalid user login');window.location='/login'</script>")
#             if q.usertype=='depots':
#                 q1 = Depot_head.objects.get(LOGIN_id=login_id)
#                 if q1:
#                     request.session['depots_id']=q1.pk
#                     return HttpResponse(f"<script>alert('depots login success');window.location='/depots_home'</script>")
#                 else:
#                     return HttpResponse(f"<script>alert('invalid depots login');window.location='/login'</script>")
#             if q.usertype=='staffs':
#                 q1 = Staffs.objects.get(LOGIN_id=login_id)
#                 if q1:
#                     request.session['staffs_id']=q1.pk
#                     return HttpResponse(f"<script>alert('staffs login success');window.location='/staffs_home'</script>")
#                 else:
#                     return HttpResponse(f"<script>alert('invalid staffs login');window.location='/login'</script>")
#         else:
#              return HttpResponse(f"<script>alert('invalid..');window.location='/login'</script>")
#     return render(request,'public/login.html')


def login(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        if Login.objects.filter(username=username,password=password) .exists():
            obj=Login.objects.get(username=username,password=password)
            request.session['login_id']=obj.pk
            login_id=request.session['login_id']
            if obj.usertype=='admin':
                return HttpResponse(f"<script>alert('Admin login successfully');window.location='/admin_homepage'</script>")
            elif obj.usertype == 'ration_officer':
                request. session['log']="in"
                q = Ration_office.objects.get(LOGIN_id=login_id)
                if q:
                    request.session['Ration_office_id']=q.pk
                    return HttpResponse(f"<script>alert('Ration office login successfully ');window.location='/ration_homepage'</script>")
                
            elif obj.usertype == 'voter_officer':
                request. session['log']="in"
                q = Voter_office.objects.get(LOGIN_id=login_id)
                if q:
                    request.session['Voter_office_id']=q.pk
                    return HttpResponse(f"<script>alert('voter office login successfully ');window.location='/voter_homepage'</script>")     
            elif obj.usertype == 'mvd_officer':
                request. session['log']="in"
                q = Mvd_office.objects.get(LOGIN_id=login_id)
                if q:
                    request.session['mvd_office_id']=q.pk
                    return HttpResponse(f"<script>alert('Mvd office login successfully ');window.location='/mvd_homepage'</script>")
            elif obj.usertype == 'aadhaar_officer':
                request. session['log']="in"
                q = Aadhaar_office.objects.get(LOGIN_id=login_id)
                if q:
                    request.session['aadhaar_office_id']=q.pk
                    return HttpResponse(f"<script>alert('Aadhaar office login successfully ');window.location='/aadhaar_homepage'</script>")   
            elif obj.usertype == 'user':
                request. session['log']="in"
                q = User.objects.get(LOGIN_id=login_id)
                if q:
                    request.session['user_id']=q.pk
                    return HttpResponse(f"<script>alert('User login successfully ');window.location='/user_homepage'</script>")  
                 
            elif obj.usertype == 'pending':
                return HttpResponse(f"<script>alert('Please wait for admin approval');window.location='/login'</script>")
            
            elif obj.usertype == 'rejected':
                return HttpResponse(f"<script>alert('You are rejected');window.location='/'</script>")
            else:
                return HttpResponse(f"<script>alert('Invalid username or password');window.location='/login'</script>")
        else:
            return HttpResponse("""
                <html>
                <head>
                    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
                </head>
                <body>
                    <script>
                        Swal.fire({
                            title: "Login Failed!",
                            text: "Incorrect username or password. Please try again.",
                            icon: "error",
                            confirmButtonText: "OK"
                        }).then(() => {
                            window.location='/login';
                        });
                    </script>
                </body>
                </html>
            """)

        
    return render(request,'public/login.html')



def admin_homepage(request):
    return render(request,'admin/admin_homepage.html')

def manage_officer(request):
    return render(request,'admin/manage_officer.html')

def view_aadhaarofficers(request):
    data = Aadhaar_office.objects.all()
    return render(request,'admin/view_aadhaarofficers.html', {'data': data})

def admin_accept_aadharofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='aadhaar_officer'
    data.save()
    return HttpResponse(f"<script>alert('Accepted');window.location='/view_aadhaarofficers'</script>")


def admin_reject_aadharofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='aadhaar_officer'
    data.save()
    return HttpResponse(f"<script>alert('Rejected');window.location='/view_aadhaarofficers'</script>")


def view_users(request):
    data = User.objects.all()
    return render(request,'admin/view_users.html', {'data': data})

def view_voterofficers(request):
    data = Voter_office.objects.all()
    return render(request,'admin/view_voterofficers.html', {'data': data})

def admin_accept_voterofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='voter_officer'
    data.save()
    return HttpResponse(f"<script>alert('Accepted');window.location='/view_voterofficers'</script>")

def admin_reject_voterofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='voter_officer'
    data.save()
    return HttpResponse(f"<script>alert('Rejected');window.location='/view_voterofficers'</script>")


def view_mvdofficers(request):
    data = Mvd_office.objects.all()
    return render(request,'admin/view_mvdofficers.html', {'data': data})

def admin_accept_mvdofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='mvd_officer'
    data.save()
    return HttpResponse(f"<script>alert('Accepted');window.location='/view_mvdofficers'</script>")

def admin_reject_mvdofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='mvd_officer'
    data.save()
    return HttpResponse(f"<script>alert('Rejected');window.location='/view_mvdofficers'</script>")



def view_rationofficers(request):
    data = Ration_office.objects.all()
    return render(request,'admin/view_rationofficers.html', {'data': data})

def admin_accept_rationofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='ration_officer'
    data.save()
    return HttpResponse(f"<script>alert('Accepted');window.location='/view_rationofficers'</script>")

def admin_reject_rationofficer(request,id):
    data = Login.objects.get(id=id)
    data.usertype='ration_officer'
    data.save()
    return HttpResponse(f"<script>alert('Rejected');window.location='/view_rationofficers'</script>")



def update_status(request):
    return render(request,'admin/update_status.html')

def admin_view_feedback(request):
    data = Feedback.objects.all()
    return render(request,'admin/view_feedback.html', {'data': data})



def create_alphacard(request):
    return render(request,'admin/create_alphacard.html')


def admin_viewrequest(request):
    data = Applyalphacard_request.objects.all()
    return render(request,'admin/admin_viewrequest.html', {'data': data})

def generate(request, id):
    # Fetch request and user ID
    data = Applyalphacard_request.objects.get(id=id)
    user_id = data.USER.id

    # Mark request as accepted
    data.status = 'ACCEPTED'
    data.save()

    # Safely fetch cards (or None)
    rationcard = Rationcard.objects.filter(USER_id=user_id).first()
    aadhaarcard = Aadhaarcard.objects.filter(USER_id=user_id).first()
    voterid = Voterid.objects.filter(USER_id=user_id).first()
    licence = Licence.objects.filter(USER_id=user_id).first()

    # Count how many cards the user has
    card_count = sum(1 for card in [rationcard, aadhaarcard, voterid, licence] if card)

    if card_count < 2:
        return HttpResponse("<script>alert('User must have at least 2 cards to generate Alpha Card');window.location='/admin_viewrequest'</script>")

    # Generate Alpha Number with "AL" prefix
    if Alphacard.objects.count() < 1:
        numeric_part = random.randint(100000000000, 999999999999)
    else:
        last_card = Alphacard.objects.last()
        last_number = last_card.alphanumber.replace("AL", "")
        numeric_part = int(last_number) + 1

    alphanumber = f"AL{numeric_part}"

    # Create the Alpha Card with available cards only
    alphacard = Alphacard.objects.create(
        RATION=rationcard,
        LICENCE=licence,
        AADHAARCARD=aadhaarcard,
        VOTERID=voterid,
        USER_id=user_id,
        alphanumber=alphanumber
    )

    return HttpResponse("<script>alert('Alpha Card generated successfully');window.location='/admin_viewrequest'</script>")

def aadhaar_registration(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]   
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)
        obj=Login(username=username,password=password,usertype="pending")
        obj.save()
        obj1=Aadhaar_office(LOGIN_id=obj.pk,name=name,email=email,phone=phone,image=fs.url(fp))
        obj1.save()
        return HttpResponse(f"<script>alert('Aaadhaar registered Successfully');window.location='/login'</script>")
    return render(request,'public/aadhaar_registration.html')


def mvd_registration(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)
        
        obj=Login(username=username,password=password,usertype="pending")
        obj.save()
        obj2=Mvd_office(LOGIN_id=obj.pk,name=name,email=email,phone=phone,image=fs.url(fp))
        obj2.save()
        return HttpResponse(f"<script>alert('Mvd registered Successfully');window.location='/login'</script>")
    return render(request,'public/mvd_registration.html')


def ration_registration(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        image=request.FILES["image"] 
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)



        obj=Login(username=username,password=password,usertype="pending")
        obj.save()
        obj3=Ration_office(LOGIN_id=obj.pk,name=name,email=email,phone=phone,image=fs.url(fp))
        obj3.save()
        return HttpResponse(f"<script>alert('Ration registered Successfully');window.location='/login'</script>")
    return render(request,'public/ration_registration.html')


def voter_registration(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)
        obj=Login(username=username,password=password,usertype="pending")
        obj.save()
        obj4=Voter_office(LOGIN_id=obj.pk,name=name,email=email,phone=phone,image=fs.url(fp))
        obj4.save()
        return HttpResponse(f"<script>alert('Voter registered Successfully');window.location='/login'</script>")

    return render(request,'public/voter_registration.html')


def user_registration(request):
    if "submit" in request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        housename=request.POST["housename"]
        state=request.POST["state"]
        district=request.POST["district"]
        pin=request.POST["pin"]
        dob=request.POST["dob"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)
        gender=request.POST["gender"]

        obj=Login(username=username,password=password,usertype="user")
        obj.save()
        obj5=User(LOGIN_id=obj.pk,name=name,email=email,phone=phone,housename=housename,pin=pin,district=district,state=state,dob=dob,image=fs.url(fp),gender=gender)
        obj5.save()
        return HttpResponse(f"<script>alert('user registered Successfully ');window.location='/login'</script>")
    
    return render(request,'public/user_registration.html')


def verify_voterid(request):
    data = Voterid.objects.all()
    return render(request,'voter/verify_voterid.html',{'data': data})


def officer_accept_voterid(request,id):
    data = Voterid.objects.get(id=id)
    data.status='ACCEPTED'
    data.save()
    return HttpResponse(f"<script>alert('Approved');window.location='/verify_voterid'</script>")


def officer_reject_voterid(request,id):
    data = Voterid.objects.get(id=id)
    data.status='REJECTED'
    data.save()
    return HttpResponse(f"<script>alert('Declined');window.location='/verify_voterid'</script>")


def voter_homepage(request):
    return render(request,'voter/voter_homepage.html')

def voter_view_feedback(request):
    data = Feedback.objects.filter(usertype='user')
    return render(request, 'voter/voter_view_feedback.html', {'data': data})



def user_view_status(request):
    data = Applyalphacard_request.objects.filter(USER_id=request.session['user_id'])
    return render(request,'user/user_view_status.html', {'data': data})



def user_homepage(request):
    return render(request,'user/user_homepage.html')


def add_voterid(request):

    uid = request.session['user_id']
    user_instance = User.objects.get(id=uid)
    if "submit" in request.POST:
        number=request.POST["number"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)

        obj=Voterid(USER=user_instance,number=number,image=fs.url(fp))
        obj.save()
        return HttpResponse(f"<script>alert('data entered Successfully');window.location='/apply_alphacard'</script>")
    return render(request,'user/add_voterid.html')



def add_licence(request):
    uid = request.session['user_id']
    user_instance = User.objects.get(id=uid)
    if "submit" in request.POST:
        number=request.POST["number"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)

        obj=Licence(USER=user_instance,number=number,image=fs.url(fp))
        obj.save()
        return HttpResponse(f"<script>alert('data entered Successfully');window.location='/apply_alphacard'</script>")
    return render(request,'user/add_licence.html')


def add_aadhaarcard(request):
    uid = request.session['user_id']
    user_instance = User.objects.get(id=uid)
    if "submit" in request.POST:
        number=request.POST["number"]
        image=request.FILES["image"]
        date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date,image)

        obj=Aadhaarcard(USER=user_instance,number=number,image=fs.url(fp))
        obj.save()
        return HttpResponse(f"<script>alert('data entered Successfully');window.location='/apply_alphacard'</script>")
    return render(request,'user/add_aadhaarcard.html')


def user_add_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        login_id = request.session.get('login_id')  # your custom session key

        try:
            login_instance = Login.objects.get(id=login_id)

            if feedback_text:
                Feedback.objects.create(
                    LOGIN=login_instance,
                    feedback=feedback_text,
                    usertype='user',
                    date=timezone.now().date()
                )
                return render(request, 'user/user_add_feedback.html', {'message': 'Feedback submitted successfully'})
        except Login.DoesNotExist:
            return render(request, 'user/user_add_feedback.html', {'error': 'Login not found'})

    return render(request, 'user/user_add_feedback.html')
from .models import Rationcard, FamilyMember
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def add_rationcard(request):
    uid = request.session['user_id']
    user_instance = User.objects.get(id=uid)

    if "submit" in request.POST:
        number = request.POST["number"]
        image = request.FILES["image"]
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fp = fs.save(date, image)

        # Save Ration Card
        ration = Rationcard(USER=user_instance, number=number, image=fs.url(fp))
        ration.save()

        # Get family members data
        names = request.POST.getlist("names[]")
        ages = request.POST.getlist("ages[]")

        # Save family members
        for name, age in zip(names, ages):
            FamilyMember.objects.create(rationcard=ration, name=name, age=int(age))

        return HttpResponse("<script>alert('Data entered successfully');window.location='/apply_alphacard'</script>")

    return render(request, 'user/add_rationcard.html')

# def apply_alphacard(request):
#     # Check if the user has already applied for an Alpha Card
#     existing_application = Applyalphacard_request.objects.filter(USER_id=request.session['user_id']).exists()
    
#     if existing_application:
#         # If an application already exists, show an alert and redirect to the homepage
#         return HttpResponse(f"<script>alert('You have already applied for an Alpha Card');window.location='/user_homepage'</script>")
        
#     if "submit" in request.POST:
#         description = request.POST["description"]
        
#         # Save the new application
#         obj = Applyalphacard_request(USER_id=request.session['user_id'], description=description)
#         obj.save()
#         return HttpResponse(f"<script>alert('Applied successfully');window.location='/apply_alphacard'</script>")
    
#     return render(request, 'user/apply_alphacard.html')


# def apply_alphacard(request):
#     user_id = request.session.get('user_id')

#     if not user_id:
#         return HttpResponse("<script>alert('User not logged in');window.location='/login'</script>")

#     # Check if the user has added all cards
#     has_licence = Licence.objects.filter(USER_id=user_id).exists()
#     has_aadhaar = Aadhaarcard.objects.filter(USER_id=user_id).exists()
#     has_voterid = Voterid.objects.filter(USER_id=user_id).exists()
#     has_rationcard = Rationcard.objects.filter(USER_id=user_id).exists()

#     has_all_cards = has_licence and has_aadhaar and has_voterid and has_rationcard

#     # Check if the user has applied for an Alpha Card
#     existing_application = Applyalphacard_request.objects.filter(USER_id=user_id).exists()

#     if existing_application:
#         return HttpResponse("""
#             <html>
#             <head>
#                 <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
#             </head>
#             <body>
#                 <script>
#                     Swal.fire({
#                         title: "Already Applied!",
#                         text: "You have already applied for an Alpha Card. Do you want to delete it and create a new one?",
#                         icon: "warning",
#                         showCancelButton: true,
#                         confirmButtonText: "Delete & Reapply",
#                         cancelButtonText: "Keep Existing",
#                     }).then((result) => {
#                         if (result.isConfirmed) {
#                             window.location = '/delete_alphacard';
#                         } else {
#                             window.location = '/user_homepage';
#                         }
#                     });
#                 </script>
#             </body>
#             </html>
#         """)

#     if "submit" in request.POST:
#         description = request.POST["description"]
        
#         # Save the new application
#         obj = Applyalphacard_request(USER_id=request.session['user_id'], description=description)
#         obj.save()
#         return HttpResponse(f"<script>alert('Applied successfully');window.location='/apply_alphacard'</script>")
    
#     return render(request, 'user/apply_alphacard.html', {
#         'has_licence': has_licence,
#         'has_aadhaar': has_aadhaar,
#         'has_voterid': has_voterid,
#         'has_rationcard': has_rationcard,
#         'has_all_cards': has_all_cards,
#     })  
def apply_alphacard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return HttpResponse("<script>alert('User not logged in');window.location='/login'</script>")

    # Check card presence
    has_licence = Licence.objects.filter(USER_id=user_id).exists()
    has_aadhaar = Aadhaarcard.objects.filter(USER_id=user_id).exists()
    has_voterid = Voterid.objects.filter(USER_id=user_id).exists()
    has_rationcard = Rationcard.objects.filter(USER_id=user_id).exists()
    has_request = Applyalphacard_request.objects.filter(USER_id=user_id).exists()

    card_count = sum([has_licence, has_aadhaar, has_voterid, has_rationcard])
    can_apply = card_count >= 2 and not has_request

    # Handle re-application
    if has_request:
        return HttpResponse("""
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
            </head>
            <body>
                <script>
                    Swal.fire({
                        title: "Already Applied!",
                        text: "You have already applied for an Alpha Card. Do you want to delete it and create a new one?",
                        icon: "warning",
                        showCancelButton: true,
                        confirmButtonText: "Delete & Reapply",
                        cancelButtonText: "Keep Existing",
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location = '/delete_alphacard';
                        } else {
                            window.location = '/user_homepage';
                        }
                    });
                </script>
            </body>
            </html>
        """)

    # Handle form submission
    if "submit" in request.POST:
        description = request.POST["description"]
        Applyalphacard_request.objects.create(USER_id=user_id, description=description)
        return HttpResponse("""
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
            </head>
            <body>
                <script>
                    Swal.fire({
                        title: "Success!",
                        text: "Your Alpha Card application was submitted successfully.",
                        icon: "success",
                        confirmButtonText: "OK",
                    }).then(() => {
                        window.location='/apply_alphacard';
                    });
                </script>
            </body>
            </html>
        """)

    return render(request, 'user/apply_alphacard.html', {
        'has_licence': has_licence,
        'has_aadhaar': has_aadhaar,
        'has_voterid': has_voterid,
        'has_rationcard': has_rationcard,
        'card_count': card_count,
        'can_apply': can_apply,
    })
def delete_alphacard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return HttpResponse("<script>alert('User not logged in');window.location='/login'</script>")

    # Delete the Alpha Card application
    alpha_card_deleted, _ = Applyalphacard_request.objects.filter(USER_id=user_id).delete()

    # Delete linked records
    licence_deleted, _ = Licence.objects.filter(USER_id=user_id).delete()
    aadhaar_deleted, _ = Aadhaarcard.objects.filter(USER_id=user_id).delete()
    voterid_deleted, _ = Voterid.objects.filter(USER_id=user_id).delete()
    rationcard_deleted, _ = Rationcard.objects.filter(USER_id=user_id).delete()

    # Check if at least one record was deleted
    if alpha_card_deleted or licence_deleted or aadhaar_deleted or voterid_deleted or rationcard_deleted:
        return HttpResponse("""
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
            </head>
            <body>
                <script>
                    Swal.fire({
                        title: "Deleted!",
                        text: "Your Alpha Card application and all related cards have been deleted.",
                        icon: "success",
                        confirmButtonText: "OK"
                    }).then(() => {
                        window.location='/apply_alphacard';
                    });
                </script>
            </body>
            </html>
        """)

    return HttpResponse("<script>alert('No records found to delete.');window.location='/apply_alphacard'</script>")


def verify_rationcard(request):
    data = Rationcard.objects.all()
    return render(request,'ration/verify_rationcard.html', {'data': data})


def officer_accept_rationcard(request,id):
    data = Rationcard.objects.get(id=id)
    data.status='ACCEPTED'    
    data.save()
    return HttpResponse(f"<script>alert('Approved');window.location='/verify_rationcard'</script>")


def officer_reject_rationcard(request,id):
    data = Rationcard.objects.get(id=id)
    data.status='REJECTED'
    data.save()
    return HttpResponse(f"<script>alert('Declined');window.location='/verify_rationcard'</script>")


def ration_view_feedback(request):
    data = Feedback.objects.filter(usertype='user')
    return render(request,'ration/ration_view_feedback.html', {'data': data})


def ration_homepage(request):
    return render(request,'ration/ration_homepage.html')


def check_rationcard_details(request):
    context = {'searched': False}

    if request.method == "POST" and "submit" in request.POST:
        number = request.POST.get("number")
        context['searched'] = True

        try:
            data = Alphacard.objects.get(alphanumber=number)
            context['data'] = data

            ration = data.RATION

            if ration:
                try:
                    # Use related_name if set
                    family_members = ration.family_members.all()
                except:
                    family_members = ration.familymember_set.all()

                context['family_members'] = family_members
            else:
                context['no_ration'] = True

        except Alphacard.DoesNotExist:
            context['error'] = "Alpha Card not found."

    return render(request, 'ration/check_rationcard_details.html', context)

# def check_rationcard_details(request):
#     if "submit" in request.POST:
#         try:
#             number=request.POST["number"]
#             data = Alphacard.objects.get(alphanumber=number)
#             return render(request,'ration/check_rationcard_details.html', {'data': data})
#         except:
#             return HttpResponse(f"<script>alert('Not found');window.location='/check_rationcard_details'</script>") 
    
#     return render(request,'ration/check_rationcard_details.html')


def mvd_homepage(request):
    return render(request,'mvd/mvd_homepage.html')


def verify_licence(request):
    data = Licence.objects.all()
    return render(request,'mvd/verify_licence.html', {'data': data})


def officer_accept_licence(request,id):
    data = Licence.objects.get(id=id)
    data.status='ACCEPTED'
    data.save()
    return HttpResponse(f"<script>alert('Approved');window.location='/verify_licence'</script>")


def officer_reject_licence(request,id):
    data = Licence.objects.get(id=id)
    data.status='REJECTED'
    data.save()
    return HttpResponse(f"<script>alert('Declined');window.location='/verify_licence'</script>")



def mvd_view_feedback(request):
    data = Feedback.objects.filter(usertype='user')
    return render(request,'mvd/mvd_view_feedback.html', {'data': data})


def aadhaar_homepage(request):
    return render(request,'aadhaar/aadhaar_homepage.html')


def verify_aadhaarcard(request):
    data = Aadhaarcard.objects.all()
    return render(request,'aadhaar/verify_aadhaarcard.html', {'data': data})


def officer_accept_aadhaarcard(request,id):
    data = Aadhaarcard.objects.get(id=id)
    data.status='ACCEPTED'
    data.save()
    return HttpResponse(f"<script>alert('Accepted');window.location='/verify_aadhaarcard'</script>")


def officer_reject_aadhaarcard(request,id):
    data = Aadhaarcard.objects.get(id=id)
    data.status='REJECTED'
    data.save()
    return HttpResponse(f"<script>alert('Rejected');window.location='/verify_aadhaarcard'</script>")




def aadhaar_view_feedback(request):
    data = Feedback.objects.filter(usertype='user')
    return render(request,'aadhaar/aadhaar_view_feedback.html', {'data': data})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from app.models import Feedback, Login  # change 'app' to your app name

def aadhaar_add_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        login_id = request.session.get('login_id')  # ✅ use session
        if feedback_text and login_id:
            try:
                login_instance = Login.objects.get(id=login_id)
                Feedback.objects.create(
                    LOGIN=login_instance,
                    feedback=feedback_text,
                    usertype=login_instance.usertype,
                    date=timezone.now().date()
                )
                messages.success(request, "Feedback submitted successfully.")
                return redirect('/aadhaar_add_feedback')
            except Login.DoesNotExist:
                messages.error(request, "Login session is invalid.")
        else:
            messages.error(request, "Missing feedback or login session.")
    return render(request, 'aadhaar/aadhaar_add_feedback.html')



def voter_add_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        login_id = request.session.get('login_id')  # get login id from session
        if feedback_text and login_id:
            try:
                login_instance = Login.objects.get(id=login_id)
                Feedback.objects.create(
                    LOGIN=login_instance,
                    feedback=feedback_text,
                    usertype=login_instance.usertype,
                    date=timezone.now().date()
                )
                messages.success(request, "Feedback submitted successfully.")
                return redirect('/voter_add_feedback')
            except Login.DoesNotExist:
                messages.error(request, "Login session is invalid.")
        else:
            messages.error(request, "Missing feedback or login session.")
    return render(request, 'voter/voter_add_feedback.html')

def mvd_add_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        login_id = request.session.get('login_id')
        if feedback_text and login_id:
            try:
                login_instance = Login.objects.get(id=login_id)
                Feedback.objects.create(
                    LOGIN=login_instance,
                    feedback=feedback_text,
                    usertype=login_instance.usertype,
                    date=timezone.now().date()
                )
                request.session['feedback_success'] = True
                return redirect('/mvd_add_feedback')
            except Login.DoesNotExist:
                messages.error(request, "Login session is invalid.")
        else:
            messages.error(request, "Missing feedback or login session.")
    return render(request, 'mvd/mvd_add_feedback.html')

def ration_add_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        login_id = request.session.get('login_id')
        if feedback_text and login_id:
            try:
                login_instance = Login.objects.get(id=login_id)
                Feedback.objects.create(
                    LOGIN=login_instance,
                    feedback=feedback_text,
                    usertype=login_instance.usertype,
                    date=timezone.now().date()
                )
                request.session['feedback_success'] = True
                return redirect('/ration_add_feedback')
            except Login.DoesNotExist:
                messages.error(request, "Login session is invalid.")
        else:
            messages.error(request, "Missing feedback or login session.")
    return render(request, 'ration/ration_add_feedback.html')

def check_licence(request):
    context = {'searched': False}

    if request.method == "POST" and "submit" in request.POST:
        context['searched'] = True
        number = request.POST.get("number")

        try:
            data = Alphacard.objects.get(alphanumber=number)
            context['data'] = data

            # Check if licence is linked
            if hasattr(data, 'LICENCE'):
                context['licence'] = data.LICENCE
            else:
                context['no_licence'] = True

        except Alphacard.DoesNotExist:
            context['error'] = "Alpha Card not found."

    return render(request, 'mvd/check_licence.html', context)

def check_aadhaarcard(request):
    context = {'searched': False}

    if request.method == "POST" and "submit" in request.POST:
        context['searched'] = True
        number = request.POST.get("number")

        try:
            data = Alphacard.objects.get(alphanumber=number)
            context['data'] = data

            # Check if Aadhaar is linked
            if hasattr(data, 'AADHAARCARD'):
                context['aadhaar'] = data.AADHAARCARD
            else:
                context['no_aadhaar'] = True

        except Alphacard.DoesNotExist:
            context['error'] = "Alpha Card not found."

    return render(request, 'aadhaar/check_aadhaarcard.html', context)

def check_voterid(request):
    context = {'searched': False}

    if request.method == "POST" and "submit" in request.POST:
        context['searched'] = True
        number = request.POST.get("number")

        try:
            data = Alphacard.objects.get(alphanumber=number)
            context['data'] = data

            # Check if VOTERID is linked
            if hasattr(data, 'VOTERID') and data.VOTERID:
                context['voterid'] = data.VOTERID
            else:
                context['no_voterid'] = True

        except Alphacard.DoesNotExist:
            context['error'] = "Alpha Card not found."

    return render(request, 'voter/check_voterid.html', context)



def view_alphacard(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return HttpResponse("<script>alert('User not logged in');window.location='/login'</script>")

    try:
        data = Alphacard.objects.get(USER_id=user_id)
    except Alphacard.DoesNotExist:
        return HttpResponse("""
            <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
            </head>
            <body>
                <script>
                    Swal.fire({
                        title: "Apply First!",
                        text: "No Alpha Card Found.",
                        icon: "warning",
                        showCancelButton: true,
                        confirmButtonText: "Apply",
                        cancelButtonText: "Cancel",
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location = '/apply_alphacard';
                        } else {
                            window.location = '/user_homepage';
                        }
                    });
                </script>
            </body>
            </html>
        """)

    return render(request, 'user/view_alphacard.html', {'data': data})

def user_profile(request): 
    data = User.objects.get(id=request.session['user_id'])
    return render(request, 'user/user_profile.html', {'data': data})


def edit_profile(request):
    if request.method == "POST":
        s = User.objects.get(id=request.session['user_id'])
        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.phone = request.POST["phone"]
        s.housename = request.POST["housename"]
        s.state = request.POST["state"]
        s.district = request.POST["district"]
        s.pin = request.POST["pin"]
        s.dob = request.POST["dob"]
        s.gender = request.POST["gender"]

        # Handle new image upload
        if 'image' in request.FILES:
            image = request.FILES["image"]
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, image)
            s.image = fs.url(fp)  # Save new image path

        s.save()
        return redirect('/user_profile')  # Redirect after successful update

    data = User.objects.get(id=request.session['user_id'])
    return render(request, 'user/edit_profile.html', {'data': data})

def aadhaar_profile(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        obj = Aadhaar_office(name=name, email=email, phone=phone)
        obj.save()

    data = Aadhaar_office.objects.get(id=request.session['aadhaar_office_id'])
    return render(request, 'aadhaar/aadhaar_profile.html', {'data': data})


def aadhaar_edit_profile(request, id):
    s = Aadhaar_office.objects.get(id=request.session['aadhaar_office_id'])

    if request.method == "POST":
        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.phone = request.POST["phone"]

        # Handle image upload
        if 'image' in request.FILES:
            image = request.FILES["image"]
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, image)
            s.image = fs.url(fp)  # Save new image URL

        s.save()
        return HttpResponse("<script>alert('Profile Edited');window.location='/aadhaar_profile'</script>")

    return render(request, 'aadhaar/aadhaar_edit_profile.html', {'data': s})


def mvd_profile(request):
    uid=request.session['mvd_office_id']
    data = Mvd_office.objects.get(id=uid)    
    return render(request,'mvd/mvd_profile.html', {'data': data})


def mvd_edit_profile(request):  # Removed 'id' parameter
    s = Mvd_office.objects.get(id=request.session['mvd_office_id'])

    if request.method == "POST":
        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.phone = request.POST["phone"]

        # Handle image upload
        if 'image' in request.FILES:
            image = request.FILES["image"]
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, image)
            s.image = fs.url(fp)  # Save new image URL

        s.save()
        return HttpResponse("<script>alert('Profile Edited');window.location='/mvd_profile'</script>")

    return render(request, 'mvd/mvd_edit_profile.html', {'data': s})

# def mvd_profile(request): 
#     if "submit" in request.POST:
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         obj=Mvd_office(name=name,email=email,phone=phone)
#         obj.save()
               
#     data = Mvd_office.objects.get(id=request.session['mvd_office_id'])
#     return render(request,'mvd/mvd_profile.html', {'data': data})


# def mvd_edit_profile(request):
#     if "submit" in request.POST:
#         s = Mvd_office.objects.get(id=request.session['mvd_office_id'])
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         if 'image' in request.FILES:
#             image=request.FILES["image"]
#             date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
#             fs = FileSystemStorage()
#             fp = fs.save(date,image)
#             s.image=fs.url(fp)
#             s.name=name
#             s.email=email
#             s.phone=phone
#         s.save()
#     data = Mvd_office.objects.get(id=request.session['mvd_office_id'])
#     return render(request,'mvd/mvd_edit_profile.html', {'data': data})



def ration_profile(request): 
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        obj = Ration_office(name=name, email=email, phone=phone)
        obj.save()

    data = Ration_office.objects.get(id=request.session['Ration_office_id'])
    return render(request, 'ration/ration_profile.html', {'data': data})

def ration_edit_profile(request):
    s = Ration_office.objects.get(id=request.session['Ration_office_id'])

    if request.method == "POST":
        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.phone = request.POST["phone"]

        # Handle image upload
        if 'image' in request.FILES:
            image = request.FILES["image"]
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, image)
            s.image = fs.url(fp)  # Save new image URL

        s.save()
        return HttpResponse("<script>alert('Profile Edited');window.location='/ration_profile'</script>")

    return render(request, 'ration/ration_edit_profile.html', {'data': s})


# def ration_profile(request): 
#     if "submit" in request.POST:
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         obj=Ration_office(name=name,email=email,phone=phone)
#         obj.save()
               
#     data = Ration_office.objects.get(id=request.session['Ration_office_id'])
#     return render(request,'ration/ration_profile.html', {'data': data})


# def ration_edit_profile(request):
#     if "submit" in request.POST:
#         s = Ration_office.objects.get(id=request.session['Ration_office_id'])
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         if 'image' in request.FILES:
#             image=request.FILES["image"]
#             date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
#             fs = FileSystemStorage()
#             fp = fs.save(date,image)
#             s.image=fs.url(fp)
#             s.name=name
#             s.email=email
#             s.phone=phone
#         s.save()
#     data = Ration_office.objects.get(id=request.session['Ration_office_id'])
#     return render(request,'ration/ration_edit_profile.html', {'data': data})


def voter_profile(request): 
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        obj = Voter_office(name=name, email=email, phone=phone)
        obj.save()

    data = Voter_office.objects.get(id=request.session['Voter_office_id'])
    return render(request, 'voter/voter_profile.html', {'data': data})

def voter_edit_profile(request):
    s = Voter_office.objects.get(id=request.session['Voter_office_id'])

    if request.method == "POST":
        s.name = request.POST["name"]
        s.email = request.POST["email"]
        s.phone = request.POST["phone"]

        # Handle image upload
        if 'image' in request.FILES:
            image = request.FILES["image"]
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fp = fs.save(date, image)
            s.image = fs.url(fp)  # Save new image URL

        s.save()
        return HttpResponse("<script>alert('Profile Edited');window.location='/voter_profile'</script>")

    return render(request, 'voter/voter_edit_profile.html', {'data': s})

# def voter_profile(request): 
#     if "submit" in request.POST:
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         obj=Voter_office(name=name,email=email,phone=phone)
#         obj.save()
               
#     data = Voter_office.objects.get(id=request.session['Voter_office_id'])
#     return render(request,'voter/voter_profile.html', {'data': data})


# def voter_edit_profile(request):
#     if "submit" in request.POST:
#         s = Voter_office.objects.get(id=request.session['Voter_office_id'])
#         name=request.POST["name"]
#         email=request.POST["email"]
#         phone=request.POST["phone"]
#         if 'image' in request.FILES:
#             image=request.FILES["image"]
#             date=datetime.now().time().strftime("%Y%m%d-%H%M%S")+".jpg"
#             fs = FileSystemStorage()
#             fp = fs.save(date,image)
#             s.image=fs.url(fp)
#             s.name=name
#             s.email=email
#             s.phone=phone
#         s.save()
#     data = Voter_office.objects.get(id=request.session['Voter_office_id'])
#     return render(request,'voter/voter_edit_profile.html', {'data': data})

def logout(request):
    return redirect(login)