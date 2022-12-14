from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('User:{}, logged in through page {}.'.format(user.username,request.META.get('HTTP_REFERER')))

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print('User:{}, failed to log in through page {}.'.format(user.username,request.META.get('HTTP_REFERER')))

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('User:{}, logged out through page {}.'.format(user.username,request.META.get('HTTP_REFERER')))