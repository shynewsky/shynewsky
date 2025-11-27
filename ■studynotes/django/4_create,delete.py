# views.py - create(회원가입하면서 로그인하기)

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()        # 여기
            auth_login(request, user) # 여기
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

#---------------------------------------------------------------------

# views.py - delete(회원탈퇴하면서 로그아웃)

def signout(request):
    request.user.delete()
    auth_logout(request)   # 여기
    return redirect('articles:index')
 