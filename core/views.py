from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from .models import Theme, Tube
from .forms import UserForm, ThemeForm, TubeForm

class IndexTubeListView(LoginRequiredMixin, ListView):
	model = Tube
	paginate_by = 12
	template_name = 'tube/index_tube_list.html'
	ordering = ['-thumbs_up']
	

class ThemeListView(LoginRequiredMixin, ListView):
	model = Theme
	paginate_by = 10
	template_name = 'theme/theme_list.html'
	ordering = ['-media_thumbs']

class ThemeCreateView(LoginRequiredMixin, CreateView):
	template_name = "theme/theme_form.html"
	model = Theme
	form_class = ThemeForm
	success_url = reverse_lazy("index")
	
	def form_valid(self, form):
		theme = form.save(commit=False)
		theme.save()
		messages.add_message(self.request, messages.SUCCESS, 'Theme {} Salved!'.format(theme.name))
		return HttpResponseRedirect(self.success_url)

class TubeCreateView(LoginRequiredMixin, CreateView):
	template_name = "theme/theme_form.html"
	model = Tube
	form_class = TubeForm
	success_url = reverse_lazy("index")
	
	def form_valid(self, form):
		tube = form.save(commit=False)
		tube.user = self.request.user
		tube.save()
		messages.add_message(self.request, messages.SUCCESS, 'Tube {} Salved!'.format(tube.name))
		return HttpResponseRedirect(self.success_url)

class UserCreateView(View):
	def get(self, request, *args, **kwargs):
		form = UserForm()
		context = {'form':form}
		return render(request, 'registration/registration.html',context)
	
	def post(self, request, *args, **kwargs):
		form = UserForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			user_count = User.objects.filter(username=name).count()
			if user_count > 0:
				messages.add_message(self.request, messages.ERROR, 'Name already register, try another!')
				return HttpResponseRedirect(reverse_lazy("register"))
            
			if not password == password2:
				messages.add_message(self.request, messages.ERROR, 'Diferent passwords!')
				return redirect('register')

			try:
				user = User.objects.create_user(name, password=password)
				user.save()
				messages.add_message(self.request, messages.SUCCESS, 'Register Success!')
				return redirect('index')
			except:
				messages.add_message(self.request, messages.ERROR, 'Error!')

		else:
			messages.add_message(self.request, messages.ERROR, 'Check the fields!')
		return redirect('index')


class UpTubeAjaxView(LoginRequiredMixin, View):
	def post(self, request):
		pk = request.POST.get('id')
		print('---- up ---- ',pk)
		tube = Tube.objects.get(id=pk)
		tube.thumbs_up += 1	
		tube.save()
		tube.theme.update_thumbs()
		return HttpResponse(json.dumps({'ok':'true'}), content_type="application/json")

class DownTubeAjaxView(LoginRequiredMixin, View):
	def post(self, request):
		pk = request.POST.get('id')
		print('---- dow ----')
		# #VERIFICAR SE EXISTE PREDIOS OU CURSOS/SETORES ATIVOS QUE PERTENCAM AO CAMPUS
		tube = Tube.objects.get(id=pk)
		tube.thumbs_down += 1	
		tube.save()
		tube.theme.update_thumbs()
		return HttpResponse(json.dumps({'ok':'true'}), content_type="application/json")