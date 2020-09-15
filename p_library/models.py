from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название издательства')

    def __str__(self):
        return self.name


class Friend(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='Имя друга')
    address = models.CharField(max_length=128, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Электронный адресс')

    def __str__(self):
        return self.full_name


class Author(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='Имя автора')
    birth_year = models.PositiveSmallIntegerField(verbose_name='Год рождения')
    country = models.CharField(max_length=2, verbose_name='Страна')

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13, verbose_name='Международный стандартный книжный номер')
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Аннотация')
    year_release = models.PositiveSmallIntegerField(verbose_name='Год издания')
    copy_count = models.PositiveSmallIntegerField(default=1, verbose_name='Число копий')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')

    authors = models.ManyToManyField(
        Author, 
        through='Inspiration', 
        through_fields=('book', 'author'),
        verbose_name='Авторы',
        related_name='book_authors',
    )
    publisher = models.ForeignKey(
        Publisher,
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        verbose_name='Издательство', 
        related_name='book_publisher',
    )
    friend = models.ForeignKey(
        Friend,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Книга одолжена другу',
        related_name='book_friend',
    )
    date_issue = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Книга выдана')
    date_delivery = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Книга должна быть сдана')

    def __str__(self):
        return self.title


class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='inspired_works',
    )