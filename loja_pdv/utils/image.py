from pathlib import Path
from django.conf import settings
from PIL import Image


def resize_image(image_django, new_width=800, optimize=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round(new_width * original_height / original_width)

    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS) # type: ignore

    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image


def resize_image_slide(image_django, new_width=1920, new_height=1080, optimize=True, quality=100):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width == new_width and original_height == new_height:
        image_pillow.close()
        return image_pillow

    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS) # type: ignore

    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image


def resize_image_logo(image_django, new_width=50, optimize=True, quality=100):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    new_height = round(new_width / 2)

    if original_width == new_width and original_height == new_height:
        image_pillow.close()
        return image_pillow

    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS) # type: ignore

    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image