from django.contrib.auth.forms import UserCreationForm

# extends UserCreationForm
class UserCreateForm(UserCreationForm): 

    def __init__(self, *args, **kwargs) -> None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname  in ['username', 'password1', 'password2']: 
            # remove help_text 
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control'
            })


