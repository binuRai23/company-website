# signals.py

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enroll
from .utils import generate_random_username, generate_random_password

@receiver(post_save, sender=Enroll)
def create_user_and_send_email(sender, instance, created, **kwargs):
    if created:
        username = generate_random_username()
        password = generate_random_password()

        user = User.objects.create_user(username=username, password=password, email=instance.email)
        
        # Email subject and message
        subject = 'Your Course Enrollment Login Information'
        message = f'Hello {instance.firstname},\n\nYou have been successfully enrolled in the course {instance.selected_course}.\n\nHere are your login details:\nUsername: {username}\nPassword: {password}\n\nPlease log in to the student dashboard and change your password immediately.\n\nThank you!'
        
        # Send email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email])
