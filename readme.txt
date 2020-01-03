Models:
1) class Post
Presenta la clase de la investigación

class PostDetail
Presenta la clase de un capitulo de la investigación

class Presentation(models.Model):
Presenta la clase de una vizualización, un dashboard.

class Presentation_ImageOnline
Es una clase hijo de Presentación. Viene a ser una visualización que acepta div's para presentar los dashboards

Views
1)class PostListView(ListView):
Muestra todas las investigaciones publicadas

2)class UserPostListView(ListView):
Muestra todas las investigaciones publicadas por usuario

3)class CategoryPostListView(ListView):
Muestra todas las investigaciones publicadas por categoria

4)class PostDetailListView(ListView):
Muestra todos los capitulos de una investigación

5)class PresentationListView(ListView):
Muestra toda las visualizaciones de un capitulo de investigación

class PresentationDetail(DetailView):
Muestra una visualización completa

class PostCreateView(LoginRequiredMixin, CreateView):
Creación de una investigación por parte del usuario

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
Actualización de una investigación por parte del usuario

class PostDetailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
Actualización de un capitulo por parte del usuarioActualización de una investigación por parte del usuario

class PresentationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
Actualización de una visualización por parte del usuario

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
Eliminación de una investigación

class PostDetailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
Eliminación de un capitulo

class PresentationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
Eliminación de una visualización

© 2019 GitHub, Inc.
