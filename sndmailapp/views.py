from django.shortcuts import HttpResponse
import smtplib
from decouple import config
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sendMailApp(request, **kwargs):
    EMAIL_ADDRESS = config('EMAIL_ADDRESS')
    EMAIL_PASSWORD = config('EMAIL_PASSWORD')

    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('subject')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            subject = subject
            body = body
            msg = f'Subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, "akhatri@devopsinternational.nl", msg)

    return HttpResponse("Message send")
