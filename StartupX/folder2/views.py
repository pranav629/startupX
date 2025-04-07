from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import uuid
import json
# Create your views here.
from firebase_admin import firestore
db=firestore.client()
def firstpage(request):
     
     return render(request, 'firstpage.html')

def mentor(request):
     if request.method=='POST':
          db.collection("AvailableMentors").document(request.POST.get('mentorEmail')).set({
               'Name':request.POST.get('mentorName'),
               'Email':request.POST.get('mentorEmail'),
               'Bio':request.POST.get('mentorBio'),
               'Availability':request.POST.get('availableTime'),
               'Phone':request.POST.get('mentorPhone'),
               'Password':request.POST.get('password')
          })
          return HttpResponse("welcome "+request.POST.get('mentorName'))
     return HttpResponse("not received any data")
def redirectments(request):
   return redirect('mlogin')
def redirectents(request):
     return redirect('entlogin')
def entrepreneur(request):
     if (request.method=='POST'):
          db.collection("AvailableEntrepreneurs").document(request.POST.get('Email')).set({
               'Name':request.POST.get('Name'),
               'Email':request.POST.get('Email'),
               'Bio':request.POST.get('Bio'),
               'Qualification':request.POST.get('Qualification'),
               'Phone':request.POST.get('Phone'),
               'Password':request.POST.get('Password')
          })
          return HttpResponse("welcome "+request.POST.get('Name'))
    
          
def home(request):
     return render(request, 'home.html')
def entrepreneur_signup(request):
     if (request.method=='POST'):
          name=request.POST.get('name')
          newemail=request.POST.get('email')
          password=request.POST.get('password')
          exist=False
          accounts=db.collection('AvailableEntrepreneurs').get()
          for i in accounts:
               if i.to_dict()['Email']==newemail:
                    exist=True
                    break

          if exist:
               return render(request,'entrepreneur_signup.html',{'message':'The email already exists '})
          else:
               token=str(uuid.uuid4())
               registration_link=f'"http://127.0.0.1:8000/home/verify-entrepreneur-email/{token}/'
               db.collection('EntrepreneurVerifications').document(newemail).set({
                'name':name,
                'email': newemail,
                'password':password,
                'token': token,
                'verified': False
            })
               send_mail(
                'Confirm Your Entrepreneur Account',
                f'Click the link to confirm your email and complete your registration: {registration_link}',
                'startupconnect8@gmail.com', 
                [newemail],
                fail_silently=False,
               )

               return render(request,'entrepreneur_signup.html',{'message':'check your email for the confirmation link if not received check the spam list'})
     return render(request, 'entrepreneur_signup.html')
def verify_entrepreneur_email(request,token):
     collect=db.collection('EntrepreneurVerifications').get()
     verification_docs=None
     for i in collect :
          if i.to_dict()['token']==token:
               verification_docs=i
               break
     if not verification_docs:
        return render(request, 'email_verification.html', {'message': 'Invalid or expired verification link.'})
     else:
         db.collection('EntrepreneurVerifications').document(verification_docs.id).delete()
         return render(request,'index.html',{'name':verification_docs.to_dict()['name'],'email':verification_docs.to_dict()['email'],'password':verification_docs.to_dict()['password']})
def mentor_login(request):
     if request.method=='POST':
      mentors=db.collection('AvailableMentors').get()
      email=request.POST.get('email')
      password=request.POST.get('password')
      visited=False
      
      for i in mentors :
          
          if i.to_dict()['Email']==email:
               
               if (i.to_dict()['Password']==password):
                    visited=True
                    return HttpResponse('welcome back '+i.to_dict()['Name'])
               else :
                    return render(request,'mentor_login.html',{'message':'The password is incorrect'})
      if visited==False:
          return render(request, 'mentor_login.html',{'message':'The email or password is incorrect'})

     return render(request , 'mentor_login.html')
def mentor_signup(request):
     if (request.method=='POST'):
          name=request.POST.get('name')
          newemail=request.POST.get('email')
          password1=request.POST.get('password')
          exist=False
          accounts=db.collection('AvailableMentors').get()
          
          for i in accounts:
               one=i.to_dict()
               
               if one['Email']==newemail:
                    exist=True
                    break
          if exist==True:
          
          
               return render(request,'mentor_signup.html', {'message':'The email already exist','mail':newemail,'password1':password1})
          else :
                token = str(uuid.uuid4())
                confirmation_link = f"http://127.0.0.1:8000/home/verify-mentor-email/{token}/"
                db.collection('MentorVerifications').document(newemail).set({
                'name':name,
                'email': newemail,
                'password':password1,
                'token': token,
                'verified': False
            })
                
                send_mail(
                'Confirm Your Mentor Account',
                f'Click the link to confirm your email and complete your registration: {confirmation_link}',
                'startupconnect8@gmail.com', 
                [newemail],
                fail_silently=False,
               )
                return render(request,'mentor_signup.html',{'message':'Check your email for the confirmation link if not received check the spam list'})

     return render(request, 'mentor_signup.html')
def entrepreneur_login(request):
     if request.method=='POST':
          ents=db.collection('AvailableEntrepreneurs').get()
          email=request.POST.get('email')
          password=request.POST.get('password')
          visited=False
          for i in ents:
               if (i.to_dict()['Email']==email):
                    if (i.to_dict()['Password']==password):
                         visited=True
                         return HttpResponse('welcome back '+i.to_dict()['Name'])
                    else:
                         return render(request,'entrepreneur_login.html',{'message':'The password is incorrect'})
          if visited==False:
               return render(request,'entrepreneur_login.html',{'message':'email or password inc'} )  
     return render(request, 'entrepreneur_login.html')

def verify_email(request, token):
    
    verification = db.collection('MentorVerifications').get()
    verification_docs=None
    for i in verification:
         if i.to_dict()['token']==token:
              verification_docs=i
              break

          
    if not verification_docs:
        return render(request, 'email_verification.html', {'message': 'Invalid or expired verification link.'})

    else:
         db.collection('MentorVerifications').document(verification_docs.id).delete()
         return render(request,'mentor.html',{'name':verification_docs.to_dict()['name'],'email':verification_docs.to_dict()['email'],'password':verification_docs.to_dict()['password']})

    return render(request, 'email_verification.html', {'message': 'Something went wrong. Please try again.'})

