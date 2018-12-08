# coding=utf8
from django.db import models


class LogsDB(models.Model):
    app_name = models.CharField(max_length=100,
                                blank=True, null=True,
                                verbose_name="组件名")
    deploy_version = models.CharField(max_length=100,
                                      blank=True, null=True,
                                      verbose_name="发布单号")
    env_name = models.CharField(max_length=24,
                                blank=True, null=True,
                                verbose_name="环境")
    ip_address = models.CharField(max_length=255,
                                  blank=True, null=True,
                                  verbose_name="IP地址")
    log_content = models.CharField(max_length=4096,
                                   blank=True, null=True,
                                   verbose_name="日志内容")
    operation_no = models.IntegerField(blank=True, null=True,
                                       default=0,
                                       verbose_name="操作批次")
    operation_type = models.CharField(max_length=24,
                                      blank=True, null=True,
                                      verbose_name="操作类型")
    user_name = models.CharField(max_length=64,
                                 blank=True, null=True,
                                 verbose_name="用户名")
    change_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.add_date

    class Meta:
        ordering = ('-change_date',)
