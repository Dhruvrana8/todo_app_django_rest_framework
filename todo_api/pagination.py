from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# This is the custom pagination class, we need to define this in the setting.py
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None
        return Response({
            'count': self.page.paginator.count,
            'next': next_page,
            'previous': previous_page,
            'results': data
        })
