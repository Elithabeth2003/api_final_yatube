from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

SHORT_DESCRIPTION_LENGTH = 20
POST_TEXT_LENGTH = 50


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title[:SHORT_DESCRIPTION_LENGTH]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['pub_date']
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:POST_TEXT_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f'''
            {self.author.username}:
            {self.text[:POST_TEXT_LENGTH]} to
            {self.post}
        '''


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow'
            ),)

    def __str__(self):
        return f'{self.user} follows {self.following}'
