from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin


class User(LogicalDeletionMixin):

    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Customer(LogicalDeletionMixin):

    name = models.CharField(max_length=200)                 # 会社正式名称
    abbreviation = models.CharField(max_length=50)          # 略称
    customer_id = models.CharField(max_length=16, blank=True)  # 顧客ID
    zip_code = models.IntegerField(null=True, blank=True)   # 所在地・郵便番号
    address = models.CharField(max_length=200, blank=True)  # 所在地
    tel = models.IntegerField(null=True, blank=True)        # 代表電話番号
    established_at = models.DateField(null=True, blank=True)  # 設立日
    capital_stock = models.FloatField(null=True, blank=True)  # 資本金（百万円）
    representative_pos = models.CharField(max_length=50, blank=True)    # 代表者役職
    representative_name = models.CharField(max_length=100, blank=True)  # 代表者氏名
    url = models.URLField(null=True, blank=True)            # 企業サイトURL
    remarks = models.TextField(blank=True)                  # 備考
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(LogicalDeletionMixin):

    customer = models.ForeignKey(Customer, to_field='id', on_delete=models.DO_NOTHING)
    project_name = models.CharField(max_length=100)  # プロジェクト名
    project_outline = models.TextField(blank=True)   # プロジェクト概要
    start_date = models.DateField(null=True, blank=True)  # 開始日
    delivered_date = models.DateField(null=True, blank=True)  # 納品日
    inspected_date = models.DateField(null=True, blank=True)  # 検収日
    man_month = models.IntegerField(null=True, blank=True)  # 工数
    amount_ex_tax = models.IntegerField(null=True, blank=True)  # 税抜き金額
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
