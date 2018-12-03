from django.shortcuts import render, redirect
from apps.Usuario.models import Usuario
from django.contrib.auth.models import User
from apps.Usuario.forms import UsuarioForm, UserForm
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.


class UsuarioVer(ListView):
	model = Usuario
	template_name = 'Usuario/ver.html'

	def dispatch(self, *args, **kwargs):
		return super(UsuarioVer,  self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(UsuarioVer, self).get_context_data(**kwargs)
		Usuarios = Usuario.objects.filter(estado=True).exclude(usuario__username = "admin")
		context['Usuarios']= Usuarios
		return context


class UsuarioCrear(CreateView):
	model = User
	template_name = 'Usuario/crear.html'
	form_class = UsuarioForm
	second_form_class = UserForm
	success_url = '/Usuario/'

	def dispatch(self, *args, **kwargs):
		return super(UsuarioCrear,  self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(UsuarioCrear, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid():
			if form2.is_valid():
				Usuario = form.save(commit=False)
				Usuario.usuario=form2.save()
				Usuario.save()
				return HttpResponseRedirect(self.get_success_url())
			else:
				return self.render_to_response(self.get_context_data(form=form, form2=form2))
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


class UsuarioActualizar(UpdateView):
	model = Usuario
	second_model = User
	template_name = "Usuario/actualizar.html"
	form_class = UsuarioForm
	second_form_class = UserForm
	success_url = '/Usuario/'

	def get_context_data(self, **kwargs):
		context = super(UsuarioActualizar, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		UsuarioForm = self.model.objects.get(id=pk)
		userForm = self.second_model.objects.get(id=UsuarioForm.usuario.id)
		if 'form' not in context:
			context['form'] = self.form_class(instance=UsuarioForm)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=userForm)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pk = self.kwargs.get('pk', 0)
		UsuarioForm = self.model.objects.get(id=pk)
		userForm = self.second_model.objects.get(id=UsuarioForm.usuario.id)
		form = self.form_class(request.POST, instance=UsuarioForm)
		form2 = self.second_form_class(request.POST, instance=userForm)
		if form.is_valid():
			if form2.is_valid():
				form.save()
				form2.save()
				return HttpResponseRedirect(self.get_success_url())
			else:
				return self.render_to_response(self.get_context_data(form=form, form2=form2))
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

def UsuarioEliminar(request, pk):
	Usuario = Usuario.objects.get(id = pk)
	Usuario.soft_delete()
	return redirect("/Usuario/")