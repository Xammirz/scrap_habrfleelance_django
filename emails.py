import os
import sys
from datetime import datetime

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django
django.setup()

from django.core.mail import EmailMultiAlternatives
from core.settings import EMAIL_HOST_USER
from pars.models import Follower
from ff import habr_parsing

jobs = habr_parsing()
emails = Follower.objects.all()
subject = f'Новости для Вас на сегодня {datetime.today()}'
from_email = EMAIL_HOST_USER
text_content = 'Рассылка новстей!'
html_content = ''
for email in emails: 
    for job in jobs:
        html_content += f'''<div class="card text-center">
        <div class="card-header">
          { job.get('title') }
        </div>
        <div class="card-body">
          <h5 class="card-title">{ job.get('vote') } Голосов</h5>
          <p class="card-text">{ job.get('bookmarks') } Избранных</p>
          <a href="{ job.get('url') }" class="btn btn-primary">Перейти на новость</a>
        </div>
        <div class="card-footer text-muted">
          { job.get('time') }
        </div>
      </div> </br>'''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()