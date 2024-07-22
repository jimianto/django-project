from django import forms
from .models import Item

CLASS_INPUT = "w-full py-4 px-6 rounded-xl border"

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category","name","description","price","image")
        widgets ={
            "category": forms.Select(attrs={
                 "class":CLASS_INPUT
            }),
             "name": forms.Textarea(attrs={
                 "class":CLASS_INPUT
            }),
             "description": forms.TextInput(attrs={
                 "class":CLASS_INPUT
            }),
            "price": forms.TextInput(attrs={
                 "class":CLASS_INPUT
            }),
            "image": forms.FileInput(attrs={
                 "class":CLASS_INPUT
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category","name","description","price","image","is_sold")
        widgets ={
             "name": forms.Textarea(attrs={
                 "class":CLASS_INPUT
            }),
             "description": forms.TextInput(attrs={
                 "class":CLASS_INPUT
            }),
            "price": forms.TextInput(attrs={
                 "class":CLASS_INPUT
            }),
            "image": forms.FileInput(attrs={
                 "class":CLASS_INPUT
            }),

        }