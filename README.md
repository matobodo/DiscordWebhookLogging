# Discord webhook logging
Simple `logging` handler and formatter for sending larger logs to discord channels.

## Usage
```python
import logging
from discord_webhook_logging import DiscordWebhookHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = DiscordWebhookHandler(webhook_url='<your webhook url>')
logger.addHandler(handler)
```