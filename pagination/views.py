from django.shortcuts import render, redirect
from pagination import forms
from django.contrib import messages
from django.views.generic.list import ListView
from pagination import models
from pagination import forms

def form_view(request, **kwargs):
    if request.method == "POST":
        todo_form = forms.ToDoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            messages.success(request, "Submission successful")
        redirect('listview')
    todo_form = forms.ToDoForm()
    context = {'title': "To Do List", "todo_form": todo_form}
    return render(request, 'pagination/form.html', context=context)




class FormListView(ListView):
    model = models.ToDoList
    paginate_by = 5  # if pagination is desired
    template_name = 'pagination/listview.html'
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form List View'
        context['filter_form'] = forms.FilterListView(self.request.GET)
        return context

    def get_queryset(self):
        queryset = models.ToDoList.objects.all().order_by('-id')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name=name)
        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        print(queryset)
        return queryset
