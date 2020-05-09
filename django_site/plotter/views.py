import sys
import os
ROOT_DIR = '/'.join((os.path.dirname(os.path.abspath(__file__)).split('/'))[:-2])
sys.path.insert(0, ROOT_DIR + '/asthma/')
# print(sys.path)
from django.shortcuts import render
from django.http import HttpResponse
from plot_asthma import get_html

html_source = get_html()

html_source = '<div>' + '<div>'.join(html_source.split('<div>')[1:])
html_source = '</div>'.join(html_source.split('</div>')[:-1]) + '</div>'

# Create your views here.
def home(request):
    context = {
        'html': html_source
    }
    return render(request, 'plotter/home.html', context)