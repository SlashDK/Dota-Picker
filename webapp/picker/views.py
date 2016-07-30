from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .utils.algorithm import get_best_heroes
from django.contrib import messages

# Create your views here.
@csrf_protect
def pick(request):
    if request.method == 'POST':
        home_team = []
        for i in range(1,6):
            if request.POST.get('Home'+str(i)) is not '':
                home_team.append(request.POST.get('Home'+str(i)))
        enemy_team = []
        for i in range(1,6):
            if request.POST.get('Enemy'+str(i)) is not '':
                enemy_team.append(request.POST.get('Enemy'+str(i)))
        results = get_best_heroes(enemy_team, home_team)
        if not results:
            messages.warning(request, 'Please enter valid data')
        return render(request, 'picker/header.html', {'results':results})
    return render(request, 'picker/header.html')
