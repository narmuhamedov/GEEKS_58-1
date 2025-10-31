from django.db import models

class Film(models.Model):

    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Мелодрамма', 'Мелодрамма'), 
        ('Боевик', 'Боевик')
    )

    title = models.CharField(max_length=100, verbose_name='введите название фильма')
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото')
    description = models.TextField(verbose_name='Укажите описание фильма')
    director = models.CharField(max_length=100, verbose_name='укажите режисера',
                                default='Иванов Иван')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр')
    country = models.CharField(max_length=100, default='США',  verbose_name='укажите страну')
    duration = models.PositiveIntegerField(verbose_name="укажите продолжительность фильма", 
                                           default=3)
    trailer = models.URLField(verbose_name='вставьте ссылку на трейлер')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

#python manage.py makemigrations
#python manage.py migrate