from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment,Product,help
from django.contrib.auth.decorators import login_required 

# Create your views here.

def contact(request):
    ic_cont1=Article.objects.get(title="ic_cont1")
    ic_cont2=Article.objects.get(title="ic_cont2")
    
    return render(request,"contact.html",{"ic_cont1":ic_cont1,"ic_cont2":ic_cont2})



def articles(request):
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

def index(request):
    
    products= Product.objects.all()
    comments = Comment.objects.all()

    ic_an1=Article.objects.get(title="ic_an1")
    ic_an2=Article.objects.get(title="ic_an2")
    ic_an3=Article.objects.get(title="ic_an3")
    ic_an4=Article.objects.get(title="ic_an4")
    return render(request,"index.html",{"products":products,"comments":comments,"ic_an1":ic_an1,"ic_an2":ic_an2,"ic_an3":ic_an3,"ic_an4":ic_an4})


def about(request):
    ic_ab1=Article.objects.get(title="ic_ab1")
    ic_ab2=Article.objects.get(title="ic_ab2")
    ic_ab3=Article.objects.get(title="ic_ab3")
    return render(request,"about.html",{"ic_ab1":ic_ab1,"ic_ab2":ic_ab2,"ic_ab3":ic_ab3})

@login_required
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context={
        "articles":articles
    }
    

    return render(request,"dashboard.html",context)

@login_required
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu...")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id= id).first()
    article=get_object_or_404(Article,id = id,)

    comments = article.comments.all()


    return render(request,"detail.html",{"article":article,"comments":comments},)
  
@login_required(login_url = "user:login")
def updateArticle(request,id):

    article =get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi...")
        return redirect("article:dashboard") 

    return render(request,"update.html",{"form":form})

@login_required
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()

    messages.success(request,"Makale başarıyla silnidi...")

    return redirect("article:dashboard")

def addHelp(request):
    
    
    if request.method == "POST":
        help_name = request.POST.get("name")
        help_mail = request.POST.get("email")
        help_title=request.POST.get("subject")
        help_content=request.POST.get("message")

        
        
        newHelp = help.objects.create(help_name = help_name, help_content=help_content,help_mail=help_mail,help_title=help_title)

        
        newHelp.save()


        messages.warning(request,"Mesajınız işleme alınmıştır en kısa sürede E-Posta adresinize geri dönüş sağlayacağız..")
    
    

        
            

    return redirect("contact")


def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        comment_oy=request.POST.get("rating")
        if comment_oy is None:
           messages.warning(request,"Oylama kısmı boş bırakılamaz...") 
        elif comment_content=="" or comment_author=="":
            messages.warning(request,"İsim veya yorum kısmı boş bırakılamaz..")
        else:
            bosoy=5-int(comment_oy)
            comment_script=int(comment_oy)*"<span class='fa fa-star checked'></span>"
            comment_script+=bosoy*"<span class='fa fa-star'></span>"

            newComment = Comment(comment_author = comment_author, comment_content=comment_content,comment_oy=comment_oy,comment_script=comment_script)

            newComment.article = article

            newComment.save()
            messages.warning(request,"Yorumunuz için teşekkür ederiz...")
        
    
    return redirect("index")