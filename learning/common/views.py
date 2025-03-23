from django.shortcuts import render

# Create your views here.

import redis
from django.core.cache import cache

# user_id = 123
# user_data = {
#     'name': 'John Doe',
#     'email': 'johndoe@example.com',
#     'last_login': '2025-03-10'
# }

# cache.set(f"user:{user_id}:data", user_data, timeout=3600)


def index(request):
    value = cache.get('test_key')
    return render(request,"index.html")