from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from .forms import Fullset

# Create your views here.

def loadfile():
	file=open("question.html", "w")
	file.close()

def send_otl_email():
	text_content="Your one time link Email"
	subject="Request for your comment"
	template_name="email/otl.html"
	from_email=settings.EMAIL_HOST_USER
	users=User.objects.all()
	for user in users:
		recipients=[user.email]

		kwargs = {
			"uidb64":urlsafe_base64_encode(force_bytes(user.pk)),
			"token":default_token_generator.make_token(user)
		}

		the_url=reverse('user_comments', kwargs=kwargs)
		otl_url="{0}://{1}{2}".format("http", "127.0.0.1:8000", the_url)

		context = {
			'user' : user,
			'otl_url': otl_url,
		}
		html_content = render_to_string(template_name, context)
		email=EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		email.send()
		print("Mail has been sent to {0}\n".format(user.email))


def comments(request, uidb64=None, token=None):
	try:
		uid=force_text(urlsafe_base64_decode(uidb64))
		user=User.objects.get(pk=uid)
	except User.DoesNotExist:
		user = None
	if user and default_token_generator.check_token(user, token):
		if request.method=="POST":
			form=Fullset(request.POST)
			if form.is_valid():
				answer=form.save(commit=False)
				answer.submitby=user
				answer.save()
				return HttpResponseRedirect('/success/')
		else:
			form=Fullset()
		return render(request, 'question.html', {'form':form})
	else:
		return HttpResponse("Your time has expired")
