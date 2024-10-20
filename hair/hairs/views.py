from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import TemplateView

def main_page_view(request):
    return HttpResponse('che to')

def html_view(request):
    return render(request, '../static/../templates/html/hair.html')


def css_view(request):
    return render(request, '../static/css/styles.css')
#
# class Home (TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, request):
#         ctx = {}
#         return render(request, self.template_name, ctx)
