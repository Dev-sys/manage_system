
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            return response
        else :
            return render(request,'index.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user','')
    paginator = Paginator(event_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,"event_manage.html",{"user":username,
                                              "events":contacts})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    sreach_name = request.GET.get("name", "")
    sreach_name_bytes = sreach_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=sreach_name)
    return render(request, "event_manage.html", {"user": username,
                                                "events": event_list})

@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page','')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
                                                "guests": contacts})

@login_required
def search_realname(request):
    username = request.session.get('user', '')
    sreach_realname = request.GET.get("name", "")
    sreach_realname_bytes = sreach_realname.encode(encoding="utf-8")
    guest_list = Guest.objects.filter(realname__contains=sreach_realname)
    return render(request, "guest_manage.html", {"user": username,
                                                "guests": guest_list})

@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})

@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': '手机号为空或不存在'})
    result = Guest.objects.filter(phone = phone,event_id = event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': '该用户未参加此次发布会'})
    result = Guest.objects.get(phone = phone)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,'hint': "已签到"})
    else:
        Guest.objects.filter(phone = phone).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,'hint':'sign success!','guest':result})

# 退出登录
@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/')
    return response

        
