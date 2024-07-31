from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }

    return render(request, 'form.html', context)

def create(request):


    #-----------------------------------
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장

    # GET create/ => 빈 종이를 보여주는 기능 (사용자에게 빈 form을 보여주는?)
    # POST create/ => 사용자가 입력한 데이터를 저장하는 기능

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

            # article = Article()
            # article.title = title
            # article.save()
        
    else:
        form = ArticleForm()

    context = {
    'form': form,
    }
    return render(request, 'create.html', context)

def delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
    
    return redirect('articles:index')

def update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        article = Article.objects.get(id=id)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        # article = Article.objects.get(id=id)
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        }

    return render(request, 'form.html', context)