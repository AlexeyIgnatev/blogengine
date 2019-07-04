from django.shortcuts import redirect


def redirect_url(request):
    return redirect('posts_list_url', permanent=True)
