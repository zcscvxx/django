from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    if request.method=='POST': # 메소드의 방식이 POST 라면
        form = Form(request.POST)
        if form.is_valid(): # form의 형식이 제대로 갖추어졌다면
            form.save() # 데이터베이스에 저장
    else:
        form = Form()
    # 디스패치 작업
    return render(request,'write.html',{'form':form})

def list(request):
    articleList = Article.objects.all()
    return render(request,'list.html',{'articleList':articleList})

def view(request,num=1):
    article = Article.objects.get(id=num)
    return render(request,'view.html',{'article':article})


