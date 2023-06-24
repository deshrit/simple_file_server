from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'file form-control',
                'multiple': ''
            }
        ),
        error_messages={
            'required': 'File field is required.'
        }
    )