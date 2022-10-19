from rest_framework.pagination import LimitOffsetPagination

class MYLOSP(LimitOffsetPagination):
    default_limit = 2