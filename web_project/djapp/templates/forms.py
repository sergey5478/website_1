from django import forms


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    email = forms.EmailField(max_length=128, label='Email', widget=forms.EmailInput, required=True)
    adr = forms.CharField(max_length=1000, label='Адрес', required=False)
    phone = forms.CharField(max_length=100, label="Телефон", widget=forms.NumberInput, required=True)
    info = forms.CharField(max_length=1024, label="Дополнительная информация", required=False, widget=forms.Textarea)

    class Meta:
        fields = ('name', 'email', 'adr', 'phone', 'info')
