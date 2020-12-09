from django.db import models


# 文本对象
class Text(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    text = models.TextField(verbose_name='文本内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    to_top = models.BooleanField(default=False, verbose_name='置顶')
    is_deleted = models.BooleanField(default=False, verbose_name='已删除标记')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文本对象'
        verbose_name = '文本对象'
