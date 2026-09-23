from django import forms
from .models import ResumeAnalysis

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = ResumeAnalysis
        fields = ('file',)
        widgets = {'file': forms.FileInput(attrs={'accept': '.pdf,.docx', 'class': 'form-control form-control-lg'})}

    def clean_file(self):
        uploaded = self.cleaned_data['file']
        if uploaded.size > 10 * 1024 * 1024:
            raise forms.ValidationError('Resume files must be 10MB or smaller.')
        if not uploaded.name.lower().endswith(('.pdf', '.docx')):
            raise forms.ValidationError('Upload a PDF or DOCX resume.')
        return uploaded
