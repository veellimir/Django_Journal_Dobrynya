from django import forms


class BaseFormUsers(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].required = True

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

