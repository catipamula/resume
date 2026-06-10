from django import forms

class ResumeForm(forms.Form):
    resume_text = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Paste your resume here...",
            "rows": 12
        })
    )