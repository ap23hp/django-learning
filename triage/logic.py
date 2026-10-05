from .models import Category


def find_category(text):
    text = text.lower()
    for category in Category.objects.all():
        for keyword in category.keywords.all():
            if keyword.word in text:
                return category
    return None