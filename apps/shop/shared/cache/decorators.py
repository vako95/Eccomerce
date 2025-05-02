# import hashlib, json
# from django.core.cache import cache
# from functools import wraps

# def cache_model(timeout=30):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             cache_key = f"{func.__name__}:{hashlib.md5(json.dumps(kwargs, sort_keys=True).encode()).hexdigest()}"
#             cached_data = cache.get(cache_key) or cache.set(cache_key, func(*args, **kwargs), timeout=timeout) or cache.get(cache_key)
#             return cached_data
#         return wrapper
#     return decorator
