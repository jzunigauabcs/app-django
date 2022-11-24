from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Momento
from django.core import serializers
# Create your views here.


@login_required
def index(request):
    momentos = Momento.objects.all()
    momentos_json = serializers.serialize('json', momentos)

    ctx = {
        'momentos': momentos_json
    }
    return render(request, 'momentos/index.html', ctx)


@login_required
def save_momento(request):
    if request.method == 'POST':
        user_id = request.user.id
        title = request.POST['titulo']
        content = request.POST['contenidoMomento']
        lat = request.POST['latHidden']
        lng = request.POST['lngHidden']
        m = Momento(title=title, content=content,
                    lat=lat, lng=lng, user_id_id=user_id)
        m.save()

    return redirect('home')
