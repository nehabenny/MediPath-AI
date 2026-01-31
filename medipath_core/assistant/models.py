from django.db import models
from django.contrib.auth.models import User

class PatientReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_content = models.TextField() # To store the text extracted from the PDF
    created_at = models.DateTimeField(auto_now_add=True)