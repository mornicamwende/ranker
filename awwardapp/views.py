from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from geelweb.django.ratings.views import RateView
from .models import post 
from django.urls import reverse
from django.shortcuts import get_object_or_404
import random



def home(request):
    try:
        posts= post.objects.all()
        posts = posts[::-1]
        one_post = random.randint(0, len(posts)-1)
        random_post= posts[one_post]
        print(random_post)
    except post.DoesNotExist:
        posts = None
    
    return render(request, 'awwardapp/home.html', locals())

class PostListView(ListView):
    model = post
    template_name = 'awwardapp/home.html' #<app>/<model> <viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'caption', 'image', 'owner', 'url']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'caption']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        else:
            return False


def about(request):
    return render(request, 'awwardapp/about.html', {'title': 'About'})


# class PostRateView(LoginRequiredMixin, RateView):
#     model = Rating
#     fields = ['usability', 'design', 'content']
    
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super().form_valid(form)

