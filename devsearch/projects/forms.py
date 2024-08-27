from django.forms import ModelForm
from projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'featured_image', 'description','demo_link','source_link', 'tags']

        