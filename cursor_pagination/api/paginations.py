from rest_framework.pagination import CursorPagination

class MYCP(CursorPagination):
    page_size = 3
    ordering = 'name'