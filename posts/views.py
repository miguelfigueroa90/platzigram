from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Mont Blank',
        'user': {
            'name': 'Yésica Cortez',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Vía lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
]

@login_required
def posts_list(request):
    return render(request, 'posts/feed.html', {'posts': posts})
