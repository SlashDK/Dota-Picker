from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .utils.algorithm import main

# Create your views here.
@csrf_protect
def pick(request):
    if request.method == 'POST':
        home_team = []
        for i in range(1,6):
            home_team.append(request.POST.get('Home'+str(i), None))
        enemy_team = []
        for i in range(1,6):
            enemy_team.append(request.POST.get('Enemy'+str(i), None))
        print('Home', home_team)
        print('Enemy', enemy_team)
        print(main(enemy_team, home_team))
    return render(request, 'picker/header.html')
