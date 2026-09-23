from django.test import SimpleTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ResumeUploadForm

class ResumeUploadTests(SimpleTestCase):
    def test_rejects_non_resume_extension(self):
        form = ResumeUploadForm(files={'file': SimpleUploadedFile('notes.txt', b'hello')})
        self.assertFalse(form.is_valid())
        self.assertIn('PDF or DOCX', str(form.errors))
