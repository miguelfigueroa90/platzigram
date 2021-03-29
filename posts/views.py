from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Mont Blank',
        'user': 'Yésica Cortez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Vía lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Uriel',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
]

def posts_list(request):
    content = []

    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"></figure>
            """.format(**post))

    return HttpResponse('<br>'.join(content))
