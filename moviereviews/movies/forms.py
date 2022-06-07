

from django.forms import ModelForm, Textarea
from .models import Review


# we need to inherit from ModelForm
class ReviewForm(ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super(ModelForm, self).__init__(*args, **kwargs)

        # set some Bootstrap classes
        self.fields['text'].widget.attrs.update(
            {'class': 'form-control'}
        )

        self.fields['watch_again'].widget.attrs.update(
            {"class": 'form-check-input'}
        )

    class Meta:

        model = Review
        # we specify which model the form us for and the fields we want in the form
        fields = ['text', 'watch_again']
        labels = {
            'watch_again': ('Watch Again')
        }

        # by default a CharField is displayed as an input text, we override this default field(with the use of widgets)
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }
