from django.forms import ModelForm
from .models import Project
class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title','featured_image','description','demo_link','souce_link','tag']