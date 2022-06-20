from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required
class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'photo/list.html'

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/detail.html'

class Profile(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/profile.html'

