from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.
def blog(request):
	blog_list = Blog.objects.all()
	paginator = Paginator(blog_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request,'blog_index.html',{"Blogs":contacts})

def personal(request):
	personal_list = Blog.objects.filter(flag='P')
	paginator = Paginator(personal_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request, "personal_manage.html", {"Blogs": contacts})

def search(request):
	sreach_blog = request.GET.get("name", "")
	sreach_blog_bytes = sreach_blog.encode(encoding="utf-8")
	blog_list = Blog.objects.filter(blog_title__contains=sreach_blog)
	return render(request, "blog_index.html", {"Blogs": blog_list})

def live(request):
	live_list = Blog.objects.filter(flag='L')
	paginator = Paginator(live_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request, "live_manage.html", {"Blogs": contacts})

def work(request):
	work_list = Blog.objects.filter(flag='W')
	paginator = Paginator(work_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request, "work_manage.html", {"Blogs": contacts})

def habit(request):
	habit_list = Blog.objects.filter(id='H')
	paginator = Paginator(habit_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request, "habit_manage.html", {"Blogs": contacts})

def blog_detail(request, blog_id):
	blog = Blog.objects.filter(id=blog_id)
	return render(request, 'blog_detail.html',{'Blogs':blog})
