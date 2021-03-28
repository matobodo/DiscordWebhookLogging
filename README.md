# Discord webhook logging
Simple `logging` handler and formatter for sending larger logs to discord channels.

## Installation
Package can be installed via pip

`pip install discord-webhook-logging`

## Usage
```python
import logging
from discord_webhook_logging import DiscordWebhookHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = DiscordWebhookHandler(webhook_url='<your webhook url>')
logger.addHandler(handler)
```