from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='제목'
    )
    # TextField 길이 제한이 없다.
    contents = models.TextField(
        verbose_name='내용'
    )

    writer = models.ForeignKey(
        'myuser.Myuser',
        # user 가 탈퇴하면 게시글들 같이 전부 삭제하겠다.
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )

    tags = models.ManyToManyField(
        'tag.Tag',
        verbose_name='태그'
    )

    registered_dttm = models.DateTimeField(
        auto_now_add=True,
        verbose_name='등록시간'
    )

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = 'board'
    #     verbose_name = '게시글'
    #     verbose_name_plural = '게시글'
