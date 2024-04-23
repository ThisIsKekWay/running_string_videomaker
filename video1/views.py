import os

from django.http import HttpResponse
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

            with open(video, 'rb') as video_file:
                response = HttpResponse(video_file, content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video)}"'
                return response
    else:
        form = TextForm()
    return render(request, 'video1/index.html', {'form': form})
