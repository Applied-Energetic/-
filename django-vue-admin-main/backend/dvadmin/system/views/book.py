# -*- coding: utf-8 -*-

"""
@author: 陈佳婧
@Remark: 预订管理
"""
from dvadmin.system.models import Book
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class BookSerializer(CustomModelSerializer):
    """
    预订-序列化器
    """

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]


class BookViewSet(CustomModelViewSet):
    """
    预订权限接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    extra_filter_backends = []