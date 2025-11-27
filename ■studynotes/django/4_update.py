# views.py - update(회원정보 수정)

from .forms import CustomUserChangeForm

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

#---------------------------------------------------------------------

# views.py - update(비밀번호 수정 & 세션 무효화 방지)

from django.contrib.auth.forms import PasswordChangeForm # 내장 모듈

def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 여기
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password.html', context)

#---------------------------------------------------------------------

# (참고) 비밀번호 초기화

# urls.py
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# settings.py
EMAIL_BACKED = 'django.core.mail.backends.console.EmailBackend'