from django.shortcuts import render
from django.http import HttpResponse
from web1.models import Post
from django.template.loader import get_template

# Create your views here.

def home(request):
#    template=get_template('web1/post.html')
    return render(request,'web1/base.html')
#    html=template.render(locals())
#    return HttpResponse(html)


def manage_post(request):
    posts=Post.objects.all()
    return render(request,'web1/index.html',locals())


def post_detail(request):
    return 0
