import telepot

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest

from journal_dobrynya.env_config import TELE_BOT_TOKEN, CHAT_ID

BOT = telepot.Bot(token=TELE_BOT_TOKEN)


@csrf_exempt
def send_message_to_telegram(request: HttpRequest, send_msg: str) -> None:
    BOT.sendMessage(chat_id=CHAT_ID, text=send_msg)
