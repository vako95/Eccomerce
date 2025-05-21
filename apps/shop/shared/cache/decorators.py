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


from django.core.cache import cache
from django.shortcuts import redirect, render
from ...models import Category



def add_category(request):
    # Логика добавления новой категории
    if request.method == 'POST':
        new_category_name = request.POST.get("category_name")
        new_category = Category.objects.create(name=new_category_name)

        # Очистка кэша, чтобы обновить данные
        cache.delete("categories")

        # Редирект на главную страницу (или куда-то ещё)
        return redirect("index")
    return render(request, "shop/add_category.html")
