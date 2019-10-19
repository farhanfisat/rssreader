from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
import feedparser
from .forms import UrlForm
from .models import Urllist
# Create your views here.



def index(request):
	return render_to_response('home.html')

def predictpage(request):
	form = UrlForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()

	
	context = {
		"form": form,
	}
	return render(request, "index.html", context)

def url_list(request): #list items
	queryset = Urllist.objects.all()
	context = {
		"queryset": queryset, 
		"title": "URLs"
	}

	
	return render(request, "linklist.html", context)


def parse(request):
	#link=Urllist.objects.get(id=2)
	d = feedparser.parse('http://indianexpress.com/section/cities/kochi/feed/')
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)

def parse1(request):
	#link=Urllist.objects.get(id=2)
	d = feedparser.parse('http://indianexpress.com/section/cities/kochi/feed/')
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)
def parse2(request):
	#link=Urllist.objects.get(id=2)
	d = feedparser.parse('http://indianexpress.com/section/cities/kochi/feed/')
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)
def parse3(request):
	#link=Urllist.objects.get(id=2)
	d = feedparser.parse('http://indianexpress.com/section/cities/kochi/feed/')
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)
def parse4(request):
	#link=Urllist.objects.get(id=2)
	d = feedparser.parse('http://indianexpress.com/section/cities/kochi/feed/')
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)

def parseclicked(request, id=None):
	purl=Urllist.objects.get(id=id)
	link = purl.url	
	d = feedparser.parse(link)
	context = {
		"d": d, 
	}
	return render(request, "feeds.html", context)

