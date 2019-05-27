from . import send_email
from django.shortcuts import render
def contact(request):
    if request.method=='POST':
        message=request.POST['query']
        subject=request.POST['subject']
        message+=f"\n\n Sent by : {request.POST['email']}"
        send_email.send_email_to('goldenhourrescue@gmail.com',message,subject)
        return render(request,'contact_form.html',{'message':'Message Successfully Send \n Our Team will be \n touch with you soon.'})
    else:
        return render(request,'contact_form.html')
def login(request):
    return render(request,'account/profile.html')
