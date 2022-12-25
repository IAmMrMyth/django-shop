from .models import Category
def category_context(request):
    return {
        'category_menu':Category.objects.all()
    }