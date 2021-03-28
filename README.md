# Discord webhook logging
Simple `logging` handler and formatter for sending larger logs to discord channels.

## Installation
Package can be installed via pip.

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

## Examples
Here are some basic examples to demonstrate how this package works.

### Example of all log levels
#### Python:
```python
logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
```
#### Discord:
<pre style="background-color: #2f3136">
<span style="color:rgb(79, 84, 92)">===│This is debug message</span>
<span style="color:rgb(133, 153, 0)">+  │This is info message</span>
<span style="color:rgb(185, 187, 190)">W  │This is warning message</span>
<span style="color:rgb(220, 50, 47)">-  │This is error message</span>
<span style="color:rgb(220, 50, 47)">-!!│This is critical message</span>
</pre>

### Flushing buffered messages
DiscordWebhookHandler by default buffers messages, so it can send more lines as single messasge. Buffer can store 1989 due to Discords message length limits. It is automatically flushed when there is not enogh space for next message. You can also manualy flush the buffer by calling `logger.flush()`.

Buffer is also automatically flushed right before the app exits.

#### Python:
```python
logger.debug('This is debug message')
logger.info('This is info message')

logger.flush()  # All messages in buffer are sent

logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')

# As you can see we do not need to use flush at the end of program.
# Remaining buffered messages are automatically flushed before the app exits.
```
#### Discord:

You will see two messages in Discord insted of one like in example above.
<pre style="background-color: #2f3136">
<span style="color:rgb(79, 84, 92)">===│This is debug message</span>
<span style="color:rgb(133, 153, 0)">+  │This is info message</span>
</pre>
<pre style="background-color: #2f3136">
<span style="color:rgb(185, 187, 190)">W  │This is warning message</span>
<span style="color:rgb(220, 50, 47)">-  │This is error message</span>
<span style="color:rgb(220, 50, 47)">-!!│This is critical message</span>
</pre>

If you want, you can set to flush buffer automatically after every message. However, I do not recommend doing it, due to Discords API rate limits.
You can enable this by setting `auto_flush=True` while creating the handler.

`handler = DiscordWebhookHandler(webhook_url='<your webhook url>', auto_flush=True)`

In this case, after every message, handler sends message to discord channel.

#### Python:
```python
logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
```
#### Discord:
<pre style="background-color: #2f3136">
<span style="color:rgb(79, 84, 92)">===│This is debug message</span>
</pre>
<pre style="background-color: #2f3136">
<span style="color:rgb(133, 153, 0)">+  │This is info message</span>
</pre>
<pre style="background-color: #2f3136">
<span style="color:rgb(185, 187, 190)">W  │This is warning message</span>
</pre>


### Multi line log
If single log string contains multiple lines, it is highlighted with "├" character from 2nd line and last line is highlighted with "└"

#### Python:
```python
logger.error('1st line\nnext line\n3rd line\nlast line')
```

#### Discord:
<pre style="background-color: #2f3136">
<span style="color:rgb(220, 50, 47)">-  │1st line
-  ├next line
-  ├3rd line
-  └last line</span>
</pre>

### Long messages
Discord supports sending messages up to 2000 characters. If longer string is passed into logger, DiscordWebhookFormatter automatically splits message into shorter parts to fit discords 2000 character limt.
If the line was split, it is highlighted with "↳" character.

#### Python:
```python
logger.info('0'*2000 + '1'*50)
```

#### Discord:
<pre style="background-color: #2f3136">
<span style="color:rgb(133, 153, 0)">+  │000000000000000000000000000 ... zeroes contiues up to message length limit</span>
</pre>
And in the next message remaining text from the same log line
<pre style="background-color: #2f3136">
<span style="color:rgb(133, 153, 0)">+  ↳00000000000000011111111111111111111111111111111111111111111111111</span>
</pre>
