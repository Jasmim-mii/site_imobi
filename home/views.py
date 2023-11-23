from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import City, Real_estate, Visit


@login_required(login_url='/auth/login/')
def home(request):
    minimum_price = request.GET.get('minimum_price')
    maximum_price = request.GET.get('maximum_price')
    local_name = request.GET.get('local_name')
    tipo = request.GET.getlist('tipo')
    cities = City.objects.all()

    if minimum_price or maximum_price or local_name or tipo:
        if not minimum_price:
            minimum_price = 0
        if not maximum_price:
            maximum_price = 999999999
        if not tipo:
            tipo = ['A', 'C']

        realEstate_home = Real_estate.objects.filter(price__gte=minimum_price).filter(price__lte=maximum_price).filter(
            type_imovel__in=tipo).filter(city=local_name)
    else:
        realEstate_home = Real_estate.objects.all()

    return render(request, 'home.html', {'realEstate_home': realEstate_home, 'cities': cities})


def real_estate(request, id):
    real_estate = get_object_or_404(Real_estate, id=id)
    suggestion = Real_estate.objects.filter(city=real_estate.city).exclude(id=id)[:2]
    return render(request, 'imobi.html', {'real_estate': real_estate, 'suggestion': suggestion, 'id': id})


def schendule_visit(request):
    username = request.user
    weekday = request.POST.get('weekday')
    time_visit = request.POST.get('time_visit')
    id_real_estate = request.POST.get('id_real_estate')

    visitations = Visit(
        imovel_id=id_real_estate,
        user_visualization=username,
        time_select=weekday,
        time_visualization=time_visit)
    visitations.save()

    return redirect('/agendamentos')


def schenduling(request):
    visitations = Visit.objects.filter(user_visualization=request.user)
    return render(request, "schenduling.html", {'visitations': visitations})


def removed_scheduling(request,id):
    visits_removed = get_object_or_404(Visit, id=id)
    visits_removed.status = "C"
    visits_removed.save()
    return redirect('/agendamentos')
