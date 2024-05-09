import os
from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = int(os.getenv("DEFAULT_LIMIT", 10))
    max_limit = int(os.getenv("MAX_LIMIT", 100))
    min_limit = int(os.getenv("MIN_LIMIT", 1))
    min_offset = int(os.getenv("MIN_OFFSET", 0))
    max_offset = int(os.getenv("MAX_OFFSET", 50))
    limit_query_param = "limit"
    offset_query_param = "offset"
