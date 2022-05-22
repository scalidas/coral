from django import forms

class InputForm(forms.Form):
    distance_from_shore = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 68408.84375}))
    distance_from_port = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 106505.6016}))
    speed = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 1.899999976}))
    course = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 242.8999939}))
    lat = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 29.42815971}))
    lon = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': -12.7421236}))

    class Meta:
        fields = ("distance_from_shore", "distance_from_port", "speed", "course", "lat", "lon")