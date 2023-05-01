from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from django import forms
# from main.models import Score, Bookinfo, Course_arrang
import datetime


class ScoreForm(forms.ModelForm):
    term_choice = (
        ('1', "第一学期"),
        ('2', "第二学期"),
    )
    select_term = forms.ChoiceField(choices=term_choice)

    class Meta:
        model = models.Score
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.item():
                field.widgets.attrs = {
                    "class": "from-control",
                    "placeholder": field,
                }


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Bookinfo
        fields = ["book_name", "read_type", "borrow_date", "return_date"]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = models.Course_arrang
        fields = "__all__"

        # widgets = {
        #     "course_name": forms.TextInput(attrs={"class": "form-control"})
        #     "addr": forms.TextInput(attrs={"class": "form-control"})
        # }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.item():
                field.widgets.attrs = {"class": "form-control", "placeholder": field.labels}