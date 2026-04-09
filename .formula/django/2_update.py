# views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

#---------------------------------------------------------------------

# views.py - 통합버전

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST": # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # edit
        form = ArticleForm(instance=article) # 필수 키워드 인자
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
