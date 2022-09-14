import requests

from app.config import config


class TelegramBotAdapter:
    """Адаптер взаимодействия с ботом через Telegram Api."""

    def __init__(self, token: str = config.TG_BOT_TOKEN):
        self.api_url = 'https://api.telegram.org/bot' + token + '/{method}'

    def send_message(self, chat_id: str, message: str, is_quite: bool = False):
        """Отправить сообщение в чат."""
        requests.post(
            self.api_url.format(method='sendMessage'),
            params={
                'chat_id': chat_id,
                'text': message,
                'disable_notification': is_quite
            }, verify=False
        )

