from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)

def help(request):
    view_dict = {'help_page': 'Help Page'}
    return render(request, 'first_app/help.html', context=view_dict)
