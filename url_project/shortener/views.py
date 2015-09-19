from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Url


def index(request):
    if request.method == 'GET':
        context = {'form': UrlForm()}
        return render(request, 'shortener/index.html', context)
    else:
        url_form = UrlForm(request.POST)
        if url_form.is_valid():
            new_url = Url(url=request.POST['url'])
            new_url.path = new_url.create_path()
            new_url.save()
            return redirect(shortener, new_url.path)
        else:
            existing_url = Url(url=request.POST['url'])
            path = Url.objects.get(url=existing_url.url)
            return redirect(shortener, path.path)

def shortener(request, path):
    url = get_url(path)
    if url:
        context = {"url": url}
        return render(request, 'shortener/shortener.html', context)
    else:
        return redirect(index)

def shortener_redirect(request, path):
    url = get_url(path)
    if url:
        url.counter += 1
        url.save()
        return redirect(url.url)
    else:
        return redirect(index)

def get_url(path):
    try:
        return Url.objects.get(path=path)
    except Exception:
        return None
