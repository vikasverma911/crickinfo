from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup

from .serializers import TeamSerializer
from .models import Team, TeamMember
from .forms import URLForm
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

# Create your views here.

@csrf_exempt
def get_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            URL = form.cleaned_data['url']
            URLsqs = URL + '/squads'
            page = requests.get(URLsqs)
            soup = BeautifulSoup(page.content, 'html.parser')
            heading = soup.findAll('a', attrs={'class': 'black-link benton-bold font-sm'})
            for row in heading:
                print(row.text)
                team = Team.objects.create(name=row.text)
                Team.save()
                print(":->")
                URLsq = 'https://www.espncricinfo.com' + row['href']
                innerpage = requests.get(URLsq)
                innersoup = BeautifulSoup(innerpage.content, 'html.parser')
                plytable = innersoup.findAll('div', attrs={'class': 'player-page-name'})
                for rw in plytable:
                    nm = rw.get_text()
                    print(nm)
                    TeamMember.objects.create(team_name=team, name=nm)
                    TeamMember.save()
                print("-------------------")
            # return HttpResponseRedirect('/thanks/')
            return HttpResponse("Okay")
    else:
        form = URLForm()

    return render(request, 'api/urlform.html', {'form': form})


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# def get_name(request):
#     if request.method == 'POST':
#         form = URLForm(request.POST)
#         if form.is_valid():
#             URL = form.cleaned_data['url']
#             URLsqs = URL + '/squads'
#             page = requests.get(URLsqs)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             heading = soup.findAll(
#                 'a', attrs={'class': 'black-link benton-bold font-sm'})
#             for row in heading:
#                 print(row.text)
#                 team = Team.objects.create(name=row.text)
#                 Team.save()
#                 print(":->")
#                 URLsq = 'https://www.espncricinfo.com' + row['href']
#                 innerpage = requests.get(URLsq)
#                 innersoup = BeautifulSoup(innerpage.content, 'html.parser')
#                 plytable = innersoup.findAll(
#                     'div', attrs={'class': 'player-page-name'})
#                 for rw in plytable:
#                     nm = rw.get_text()
#                     print(nm)
#                     TeamMember.objects.create(team_name=team, name=nm)
#                     TeamMember.save()
#                 print("-------------------")
#             # return HttpResponseRedirect('/thanks/')
#             return HttpResponse("Okay")
#     else:
#         form = URLForm()
