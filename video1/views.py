import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from .forms import TextForm
from .dependencies import create_video


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            bg_color = form.cleaned_data['background_color']
            text_color = form.cleaned_data['text_color']
            video = create_video(text, bg_color, text_color)
            response = FileResponse(open("media/" + video + '.mp4', 'rb'))
            response['Content-Disposition'] = f'attachment; filename={video}.mp4'
            return response
    else:
        form = TextForm()
    return render(request, 'video1/index.html', {'form': form})
