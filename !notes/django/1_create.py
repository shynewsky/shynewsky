# urls.py

app_name = 'articles'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]

#---------------------------------------------------------------------

# views.py

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:detail', article.pk)
