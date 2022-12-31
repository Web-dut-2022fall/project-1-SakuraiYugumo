from django import forms


class articleForm(forms.Form):
    articleName = forms.CharField(label="articleName", max_length=20, )
    article_content = forms.CharField(
        label="Article content",
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 1})
    )


class EditForm(forms.Form):
    article_content = forms.CharField(
        label="Article content",
        widget=forms.Textarea()
    )
