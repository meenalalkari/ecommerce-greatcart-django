from .models import Category

def menu_links(request):
    category_items = Category.objects.all()
    return dict(category_items=category_items)
