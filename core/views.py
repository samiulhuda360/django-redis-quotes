from django.shortcuts import render
from .models import Quote
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def quote_gallery(request):
    quotes = Quote.objects.all()
    for quote in quotes:
        quote.likes = cache.get(f'likes:{quote.id}', 0)
    return render(request, 'core/quotes.html', {'quotes': quotes})

@csrf_exempt
def like_quote(request, quote_id):
    if request.method == 'POST':
        key = f'likes:{quote_id}'
        current = cache.get(key)

        if current is None:
            # Redis miss → pull from DB
            quote = Quote.objects.get(id=quote_id)
            current = quote.likes

        # Increase like count
        current += 1
        cache.set(key, current)

        # Save to DB
        Quote.objects.filter(id=quote_id).update(likes=current)

        return JsonResponse({'likes': current})


def quote_gallery(request):
    quotes = Quote.objects.all()
    for quote in quotes:
        quote.likes = cache.get(f'likes:{quote.id}', quote.likes)
    return render(request, 'core/quotes.html', {'quotes': quotes})

