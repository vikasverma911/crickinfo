from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from .forms import SearchForm
import requests
from django.http import HttpResponse,HttpResponseRedirect


class FindTeamView(FormView):
  template_name = 'app/myapp.html'
  form_class = SearchForm
  success_url = ''
  def form_valid(self, form):
      data = form.cleaned_data['data']
      URL = 'http://127.0.0.1:8000/api/teams/'
      r = requests.get(URL)
      context = r.json()
      for rw in context:
          if(rw['name']==data):
               context=rw['members']
               return HttpResponse(context)
      return HttpResponse("not valid")
