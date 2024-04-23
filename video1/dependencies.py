import datetime
import movis as mv
from .models import add


def create_video(
        text: str,
        bg_color,
        text_color,
):
    if len(text) > 20:
        name = text[:20]
    else:
        name = text

    scene_size = (100, 100)
    text_layer = mv.layer.Text(text, font_size=50, font_family='Arial', color=text_color)

    scene = mv.layer.Composition(size=scene_size, duration=3)
    scene.add_layer(mv.layer.Rectangle(scene.size, color=bg_color))  # Set background

    start_pos = scene.size[0] + text_layer.get_size()[0] // 2, scene.size[1] // 2

    scene.add_layer(
        text_layer,
        name='text',  # The layer item can be accessed by name
        position=start_pos,  # The layer is centered by default, but it can also be specified explicitly
        anchor_point=(0.0, 0.0),
        opacity=1.0, scale=1.0, rotation=0.0,  # anchor point, opacity, scale, and rotation are also supported
        blending_mode='normal')  # Blending mode can be specified for each layer.
    end_pos = - text_layer.get_size()[0] // 2, scene.size[1] // 2
    scene['text'].position.enable_motion().extend(
        keyframes=[0.0, 3.0], values=[start_pos, end_pos], easings=['ease_in_out']
    )

    time = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    full_name = f"{name}_{time}"
    add(full_name, bg_color=bg_color, font_color=text_color)
    file_path = f'media/{full_name}.mp4'
    scene.write_video(file_path)
    return file_path
