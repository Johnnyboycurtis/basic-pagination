from pagination import models
from django import forms

class ToDoForm(forms.ModelForm):
    class Meta:
        model = models.ToDoList
        fields = ['name', 'text', 'due_date']


class FilterListView(forms.Form):
    name = forms.ChoiceField(choices = [('user1', 'user1'), ('user2', 'user2')], label = 'Choose a user0', required=False)
    order_by = forms.ChoiceField(choices = [('id', 'id'), ('name', 'name')], label = 'Choose an order by option', required=False)
