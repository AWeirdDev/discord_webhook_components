from .all import button, URLbutton, checkWebhook, checkWebhookToken, send, embed
from .exceptions import IncorrectLinkError, WebhookNotFound, NoTokenError

"""
discord_webhook_components is a module that displays components in a webhook message.
"""


__version__ = "0.0.5a"
__author__ = "AWeirdScratcher"
__email__ = "aweirdscratcher@gmail.com"
__copyright__ = "Copyright 2021, AWeirdScratcher"

__all__ = [
    "button",
    "URLbutton",
    "checkWebhook",
    "checkWebhookToken",
    "send",
    "embed",
    "IncorrectLinkError",
    "WebhookNotFound",
    "NoTokenError"
]
