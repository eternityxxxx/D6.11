from django import forms
from p_library.models import Book, Author, Friend, Publisher, Inspiration


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'


class InspirationForm(forms.ModelForm):
    class Meta:
        model = Inspiration
        fields = '__all__'