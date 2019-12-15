from datetime import datetime
from django.db import models
# Create your models here.


class BookCategory(models.Model):
    """
    书籍分类
    """
    CATEGORYS = (
        (1, "图书类目"),
        (2, "图书")
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别名")
    description = models.CharField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORYS, verbose_name="类别描述", help_text="类别描述")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目录",
                                        related_name="sub_cat", on_delete=False)
    is_tab = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


class Book(models.Model):
    category = models.ForeignKey(BookCategory, null=True, blank=True, verbose_name="图书类别", on_delete=False)
    books_sn = models.CharField(max_length=50, default="", verbose_name="图书编号")
    name = models.CharField(default=0, verbose_name="书名")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    collection_num = models.IntegerField(default=0, verbose_name="收藏量")
    reference_price = models.FloatField(default=0, verbose_name="价格")
    book_brief = models.TextField(default=0, verbose_name="简单描述")
    book_description = models.TextField(default=0, verbose_name="详细描述")
    score = models.FloatField(default=0, verbose_name="评分")
    author = models.CharField(default=0, verbose_name="作者")
    Year = models.DateTimeField(verbose_name="写作时间")
    word_num = models.IntegerField(default=0, verbose_name="字数")
    book_image = models.ImageField(upload_to="", verbose_name="封面")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    add_time = models.DateTimeField(datetime.now)


    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookToSentence(models.Model):
    