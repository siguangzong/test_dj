from django.db import models


# Create your models here.

# 初始化Choice 选项
BOOK_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Publish(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=63, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    sex = models.CharField(max_length=20, verbose_name="性别")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64, verbose_name="书名")
    price = models.IntegerField(verbose_name="价格")
    color = models.CharField(max_length=64, verbose_name="颜色")
    page_num = models.IntegerField(null=True, verbose_name="页数")
    # 一对多的关系。2.0django中，当有主外键和其他对应关系时，需要设置
    publisher = models.ForeignKey("Publish", on_delete=models.CASCADE, null=True, verbose_name="发布者")
    author = models.ManyToManyField("Author", verbose_name="作者")
    book_sizes = models.CharField(max_length=1, choices=BOOK_SIZES, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
