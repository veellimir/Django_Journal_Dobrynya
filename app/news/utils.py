import os.path
from datetime import datetime

from django.conf import settings
from .models import News



def add_news(event_date: str, title: str, description: str) -> News:
    try:
        image_name = "assets/cancelled_lesson.jpg"
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)

        date_obj = datetime.strptime(event_date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d.%m.%Y")

        cancelled_training_title = f"☢️ Внимание ! {formatted_date} тренировка по направлению {title} отменяется"
        cancelled_training_description = f"Причина: {description}"

        if os.path.exists(image_path):
            news = News(
                title=cancelled_training_title,
                description=cancelled_training_description,
                image_news=image_name
            )
            news.save()
            return news
        else:
            raise FileNotFoundError(f"Image {image_name} not found in {image_path}")
    except Exception as e:
        print(f"Error occurred while adding news: {str(e)}")
        raise



