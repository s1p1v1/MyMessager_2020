from django import forms

class Contact_add_Form(forms.Form):
    contact_name = forms.CharField(label='Ведите login добавляемого контакта', max_length=10)


class Talk(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}), required=False,
                           label='Введите текст сообщения', error_messages={'required': ''})

    def clean_text(self):
        data = self.data.copy()
        data['text'] = ''
        self.data = data







