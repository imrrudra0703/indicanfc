from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from App_Login.models import *
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        types = request.POST.get('types')
        content = request.POST.get('content')
        link = request.POST.get('link')
        open_obj = Open_Mic.objects.create(fullname = fullname, contact=contact, email=email, types=types, content=content, link=link)
        open_obj.save()
        messages.success(request, 'Open Mic Registration Completed!')
    return render(request, 'index.html')


def demo(request):
    return render(request, 'demo.html')

def demo1(request):

    return render(request, 'demo1.html')

@login_required(login_url='/account/login')
def launch(request):
    return render(request, 'launch.html')

def aboutus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        newsletter_obj = Newsletter.objects.create(email=email)
        newsletter_obj.save()
        messages.success(request, 'Thankyou for subscribing us!')
        return HttpResponseRedirect("/")
    return render(request, 'aboutus.html')

def newsletter(request):
    return render(request, 'newsletter.html')

def upcoming_event(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        types = request.POST.get('types')
        content = request.POST.get('content')
        link = request.POST.get('link')
        open_obj = Open_Mic.objects.create(fullname = fullname, contact=contact, email=email, types=types, content=content, link=link)
        open_obj.save()
        messages.success(request, 'Open Mic Registration Completed!')
    return render(request, 'upcoming_event.html')

def previous_events(request):
    return render(request, 'previous_events.html')

def membership(request):
    return render(request, 'membership.html')


def payment_status(request):
    response = request.POST
    print(response)

    params_dict = {
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    client = razorpay.Client(auth=('rzp_test_uxpXt2M6OCK6fN','UgT5LV4PMBIS6JBV5nLcLBcu'))
    try:
        status = client.utility.verify_payment_signature(params_dict)
        print(status)
        subscriber = Subscriber.objects.get(order_id=response['razorpay_order_id'])
        subscriber.razorpay_payment_id = response['razorpay_payment_id']
        subscriber.paid = True
        subscriber.save()
        return render(request, "payment_status.html", {'status': True})
    except:
        return render(request, "payment_status.html", {'status': False})



@login_required(login_url='/account/login')
def auditorium(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        comment = request.POST.get('comment')
        comment_obj = Comment.objects.create(fullname = fullname, comment = comment)
        comment_obj.save()
        return HttpResponseRedirect(reverse('auditorium'))
    return render(request, "auditorium.html")

@login_required(login_url='/account/login')
def lobby(request):
    return render(request, 'lobby.html')


@login_required(login_url='/account/login')
def add_exhibition(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        logo1 = request.FILES.get('logo1')
        logo2 = request.FILES.get('logo2')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        video = request.POST.get('video')

        exhibition_obj = Exhibition(name=name, logo1=logo1, logo2=logo2, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, video=video)
        exhibition_obj.save()
        messages.success(request, 'We have send your stall for authorization')
        return HttpResponseRedirect(reverse('view_exhibition'))



    form = ExhibitionForm()
    img = Details.objects.all()
    return render(request, 'add_exhibition.html', {'img':img, 'form':form})

class View_Exhibition(LoginRequiredMixin, ListView):
    login_url = '/account/login'
    model = Exhibition
    template_name = 'view_exhibition.html'

class Exhibition_Details(LoginRequiredMixin, DetailView):
    login_url = '/account/login'
    model = Exhibition
    # queryset = Exhibition.objects.filter(is_verified=True)
    template_name = 'exhibition_details.html'

@login_required(login_url='/account/login')
def exhibition1(request):
    return render(request, 'exhibition1.html')

@login_required(login_url='/account/login')
def exhibition2(request):
    return render(request, 'exhibition2.html')

@login_required(login_url='/account/login')
def exhibition3(request):
    return render(request, 'exhibition3.html')

@login_required(login_url='/account/login')
def exhibition4(request):
    return render(request, 'exhibition4.html')

@login_required(login_url='/account/login')
def exhibition5(request):
    return render(request, 'exhibition5.html')

@login_required(login_url='/account/login')
def exhibition6(request):
    return render(request, 'exhibition6.html')

@login_required(login_url='/account/login')
def virtual(request):
    return render(request, 'virtual.html')

@login_required(login_url='/account/login')
def sponsors(request):
    return render(request, 'sponsors.html')

@login_required(login_url='/account/login')
def archive(request):
    return render(request, 'archive.html')

@login_required(login_url='/account/login')
def clubhouse(request):
    return render(request, 'clubhouse.html')

@login_required(login_url='/account/login')
def ninja(request):
    return render(request, 'ninja.html')

@login_required(login_url='/account/login')
def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')

@login_required(login_url='/account/login')
def planet_defense(request):
    return render(request, 'planet_defense.html')

@login_required(login_url='/account/login')
def snake(request):
    return render(request, 'snake.html')

@login_required(login_url='/account/login')
def selfie(request):
    return render(request, 'selfie.html')
    
@login_required(login_url='/account/login')
def visa_support(request):
    return render(request, 'visa_support.html')

@login_required(login_url='/account/login')
def ielts_trainer(request):
    return render(request, 'ielts_trainer.html')

@login_required(login_url='/account/login')
def digital_marketing(request):
    return render(request, 'digital_marketing.html')

@login_required(login_url='/account/login')
def immigration_consultant(request):
    return render(request, 'immigration_consultant.html')

@login_required(login_url='/account/login')
def corporate_trainer(request):
    return render(request, 'corporate_trainer.html')

@login_required(login_url='/account/login')
def diamond_jeweller(request):
    return render(request, 'diamond_jeweller.html')

@login_required(login_url='/account/login')
def investment_banker(request):
    return render(request, 'investment_banker.html')

@login_required(login_url='/account/login')
def event_management(request):
    return render(request, 'event_management.html')

@login_required(login_url='/account/login')
def residency_support(request):
    return render(request, 'residency_support.html')

@login_required(login_url='/account/login')
def business_investment(request):
    return render(request, 'business_investment.html')

@login_required(login_url='/account/login')
def personal_branding(request):
    return render(request, 'personal_branding.html')

@login_required(login_url='/account/login')
def travel_and_tourism(request):
    return render(request, 'travel_and_tourism.html')

@login_required(login_url='/account/login')
def matrimony(request):
    return render(request, 'matrimony.html')

@login_required(login_url='/account/login')
def career_counselling(request):
    return render(request, 'career_counselling.html')

@login_required(login_url='/account/login')
def medical_consultancy(request):
    return render(request, 'medical_consultancy.html')

@login_required(login_url='/account/login')
def banking_support(request):
    return render(request, 'banking_support.html')

@login_required(login_url='/account/login')
def chartered_accountant(request):
    return render(request, 'chartered_accountant.html')

@login_required(login_url='/account/login')
def real_estate_guidance(request):
    return render(request, 'real_estate_guidance.html')

@login_required(login_url='/account/login')
def numerology(request):
    return render(request, 'numerology.html')
    
def services(request):
    return render(request, 'services.html')

@login_required(login_url='/account/login')
def icfc_radio(request):
    return render(request, 'icfc_radio.html')
    
@login_required(login_url='/account/login')
def previous_radio_icfc(request):
    return render(request, 'previous_radio_icfc.html')

@login_required(login_url='/account/login')
def details(request):
    if request.method == "POST":
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = DetailsForm()
    img = Details.objects.all()
    return render(request, 'details.html', {'img':img, 'form':form})
