from django.shortcuts import render
from .models import contactlist, contactform
from django.core.mail import send_mail
# Create your views here.
def contactus(request):
    # contactlistdata = contactlist.objects.all()[0]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            email ,
            message,
            name,
            ['info@indicanfc.com']
            )

        contactformdata = contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()


    # context = {
    #     'contactlist':contactlistdata,
    # }
    return render(request,'contact.html', )
