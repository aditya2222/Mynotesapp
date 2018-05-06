from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import DocumentForm,UserCreateForm
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Document
# Create your views here

class NotesListView(LoginRequiredMixin,ListView):
	login_url = '/login/'
	template_name = 'notes/index.html'

	def get_queryset(self):
		return Document.objects.all()


class NotesDetailView(LoginRequiredMixin,DetailView):
	login_url = '/login/'
	template_name = 'notes/details.html'
	model = Document


class ThanksView(TemplateView):
	template_name = 'thanks.html'


class SignUpCreateView(CreateView):
    form_class=UserCreateForm
    success_url=reverse_lazy('login')
    template_name='notes/signup.html'