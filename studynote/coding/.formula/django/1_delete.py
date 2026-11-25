# urls.py

app_name = 'articles'
urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete'),
]

#---------------------------------------------------------------------

# views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
