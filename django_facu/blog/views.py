from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, PostDetail, Presentation, Presentation_ImageOnline
from django.urls import reverse

#Todas las Investigaciones
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #Ordenados de más reciente a menos reciente
    ordering = ['-date_posted']
    paginate_by = 3

#Investigaciones x Usuario
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #Ordenados de más reciente a menos reciente
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#Investigaciones x Categoria
class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #Ordenados de más reciente a menos reciente
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        category_reverse = dict((v,k) for k, v in Post.CATEGORIAS)
        return Post.objects.filter(category=category_reverse[self.kwargs.get('get_category_display')]).order_by('-date_posted')

#Poyectos de una Investigación
class PostDetailListView(ListView):
    model = PostDetail
    template_name = "blog/post_detail.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    # Ordenados de más reciente a menos reciente
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        print("aloh",self.kwargs.get('pk'))
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        print("adioh", post)
        x=PostDetail.objects.all()
        for i in x:
            print(i.post.title)
        return PostDetail.objects.filter(post=post)

#Dashboards de un proyecto
class PresentationListView(ListView):
    model = Presentation
    template_name = "blog/presentation.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'postDetail'
    # Ordenados de más reciente a menos reciente
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        postDetail = get_object_or_404(PostDetail, pk=self.kwargs.get('pk'))
        return Presentation.objects.filter(postDetail=postDetail)

#Instancia de un dashboard
class PresentationDetail(DetailView):
    model = Presentation_ImageOnline
    template_name = "blog/presentation_detail.html"  # <app>/<model>_<viewtype>.html

#La creacion de un post necesitara de un loggeado
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #Los campos del objeto Post que quieres que se creen manualmente
    fields = ['title', 'content']
    #Definimos al autor como el usuario loggeado
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#La modifiación de un post necesitara de un loggeado que sea igual al author del post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #Los campos del objeto Post que quieres que se modifiquen manualmente
    fields = ['title', 'content']
    #Definimos al autor como el usuario loggeado
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostDetail
    #Los campos del objeto Post que quieres que se modifiquen manualmente
    fields = ['postDetail_title', 'postDetail_content']
    #Definimos al autor como el usuario loggeado
    def get_success_url(self):
        return reverse('presentation', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        form.instance.post.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        postDetail = self.get_object()
        if self.request.user == postDetail.post.author:
            return True
        return False

class PresentationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Presentation
    #Los campos del objeto Post que quieres que se modifiquen manualmente
    fields = ['presentation_title', 'presentation_content']
    #Definimos al autor como el usuario loggeado
    def get_success_url(self):
        return reverse('presentation-detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        form.instance.postDetail.post.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        presentation = self.get_object()
        if self.request.user == presentation.postDetail.post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostDetail
    success_url = '/'

    def test_func(self):
        postDetail = self.get_object()
        if self.request.user == postDetail.post.author:
            return True
        return False

class PresentationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Presentation
    success_url = '/'

    def test_func(self):
        presentation = self.get_object()
        if self.request.user == presentation.postDetail.post.author:
            return True
        return False
    def get_success_url(self):
        return reverse('presentation', kwargs={'pk': self.object.pk})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
