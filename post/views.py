from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from post.models import Post, Comment
from post.forms import PostForm, CommentForm


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('add_post')
    template_name = 'post/add_post.html'


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add.html'
    success_url = reverse_lazy('posts')


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add.html'
    success_url = reverse_lazy('posts')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/comment_form.html'
    success_url = reverse_lazy('add_post')

    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        instance = Comment(post=post)
        form_kwargs['instance'] = instance
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        context['comments'] = Comment.objects.filter(
            post=context['post'])

        return context

    def get_success_url(self):
        return reverse_lazy(
            'add_comment',
            kwargs={'post_pk': self.kwargs['post_pk']}
        )