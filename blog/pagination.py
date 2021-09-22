from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PostPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1000
    page_query_param = 'page'
    

    def get_paginated_response(self, data):
        return Response({
            'results': data
        })