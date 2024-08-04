from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title','featured_image','description','demo_link','souce_link','tag']

        widgets = {
            'tag':forms.CheckboxSelectMultiple()
        }
    
    def __init__(self,*args, **kwargs):
            super(ProjectModelForm,self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


            # self.fields['title'].widget.attrs.update({'class':'input'})
