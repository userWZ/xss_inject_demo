from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import AnonymousUser
from .form import CustomLoginForm
from .models import Post, Comment
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.


class Index(View):
    template_name = 'home/index.html'
    context = {}

    def get(self, request):
        self.context['rows'] = []
        search_val = (request.GET.get('search') or '').strip()
        if search_val:
            self.context['rows'] = self.search(search_val)

        posts = Post.objects.all()

        self.context['posts'] = posts
        print(self.context)

        return render(request, template_name=self.template_name, context=self.context)

    def search(self, search_val):
        sql = """
                SELECT title
                FROM home_post
            """

        sql += f"WHERE title LIKE '%{search_val}%'"

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        rows = [row[0] for row in rows]

        return rows


class ReadPost(View):
    template_name = 'home/read_post.html'
    context = {}

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.all().filter(post=post)

        self.context['post'] = post
        self.context['comments'] = comments

        return render(request, template_name=self.template_name, context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class AddComment(View):
    def post(self, request):

        post = Post.objects.get(id=request.POST['post-id'])

        if request.user.is_authenticated:
            comment = Comment(
                post=post,
                author=request.user,
                content=request.POST['comment-textarea']
            )

        else:

            comment = Comment(
                post=post,
                content=request.POST['comment-textarea']
            )

        comment.save()

        return redirect('/posts/' + str(post.id))


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 登录成功后跳转到首页
    else:
        form = CustomLoginForm(request)
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
