# views.py

def new(request):
    form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context)
    
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save() 
        return redirect('articles:detail', article.pk)
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context)

#---------------------------------------------------------------------

# views.py - 통합버전
    
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save() 
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html', context)
