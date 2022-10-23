from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.db.models import Count

from .models import Site, Category, State, Region, Iso


# Create your views here.

class IndexView(View):
    def get(self,request):
        heritage_sites_grouped_by_category = Site.objects.values('category__name').annotate(total=Count('category')).order_by('-total')
        heritage_sites_grouped_by_region = Site.objects.values('region__name').annotate(total=Count('region')).order_by('-total')
        heritage_sites_grouped_by_year = Site.objects.values('year').annotate(total=Count('year')).order_by('-total')
        heritage_sites_grouped_by_state = Site.objects.values('state__name').annotate(total=Count('state')).order_by('-total')
        context = { 
                'heritage_sites_grouped_by_category' : heritage_sites_grouped_by_category,
                'heritage_sites_grouped_by_region' : heritage_sites_grouped_by_region,
                'heritage_sites_grouped_by_year' : heritage_sites_grouped_by_year,
                'heritage_sites_grouped_by_state' : heritage_sites_grouped_by_state
                }
        return render(request, 'unesco/index.html', context)

class ListView(generic.ListView):
    #paginate_by = 25
    template_name = 'unesco/listview.html'
    context_object_name = 'heritage_site_list'

    def get_queryset(self):
        groupby = self.request.GET.get('groupby','').lower()
        value = self.request.GET.get('value','')

        if groupby == 'category':
            return Site.objects.filter(category__name=value)
        elif groupby == 'region':
            return Site.objects.filter(region__name=value)
        elif groupby == 'state':
            return Site.objects.filter(state__name=value)
        elif groupby == 'year':
            return Site.objects.filter(year=value)
        else:
            return Site.objects.order_by('id')

class DetailView(generic.DetailView):
    template_name = 'unesco/detail.html'
    model = Site

# Candidate for deletion
"""
class IndexView(generic.ListView):
    paginate_by = 25
    template_name = 'unesco/sitelist.html'
    context_object_name = 'heritage_site_list'

    def get_queryset(self):
        return Site.objects.order_by('id')
"""
# Candidate for deletion
"""
class NewSitesView(View):
    def get(self, request):

        groupby = request.GET.get('groupby','').lower()
        value = request.GET.get('value','')

        if groupby == 'category':
            heritage_site_list = Site.objects.filter(category__name=value)
        elif groupby == 'region':
            heritage_site_list = Site.objects.filter(region__name=value)
        elif groupby == 'state':
            heritage_site_list = Site.objects.filter(state__name=value)
        elif groupby == 'year':
            heritage_site_list = Site.objects.filter(year=value)

        context = { 'heritage_site_list' : heritage_site_list }
        return render(request, 'unesco/sitesview.html', context)
"""
