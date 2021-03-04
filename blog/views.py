from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from blog import models
from blog.models import Blog,Contact,Signup,Photo
from django.db.models import Q




# Create your views here.
def home(request):
    return render(request,"index.html")
def blog(request):
    no_of_posts=3
    #if request.GET('pageno')
    #print(request.GET('pageno'))
    page=request.GET.get('page')
    #print(page)
    if page is None:
        page=1
    else:
        page=int(page)

    blogs= Blog.objects.all()
    length=len(blogs)
    #print(length)
    #print(page)
    #print(blogs)
    blogs=blogs[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
         prev=page-1
    else:
         prev=None
    if page<abs(length/no_of_posts):
        nxt=page+1
    else:
        nxt=None 
    #print(prev,nxt)               
    context={'blogs':blogs,'prev':prev,'nxt':nxt}
    return render(request,"bloghome.html", context)
def blogpost(request,slug):
    blog= Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        instance=Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save()
    
    return render(request,"contact.html")
def gallery(request):
    ph=Photo.objects.all()
    
    return render(request,"gallery.html",{"ph":ph})               
def search(request):
    return render(request,"search.html") 
def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        instance=Signup(name=name,email=email,phone=phone,password=password)
        instance.save()

    return render(request,"signup.html")        
def login(request):
   import sqlite3
   if request.method=="POST":
       email1=request.POST['email']
       password1=request.POST['password']
       Connection=sqlite3.connect("db.sqlite3")
       crsr=Connection.cursor()
       crsr.execute("SELECT*FROM blog_signup")
       ans=crsr.fetchall()
       l1=len(ans)
       for i in range(l1):
           if ans[i][2]==email1 and ans[i][4]==password1:
               return HttpResponseRedirect("http://127.0.0.1:8000/")
           
       return HttpResponseRedirect("http://127.0.0.1:8000/signup/")
               

   return render(request,"login.html")   