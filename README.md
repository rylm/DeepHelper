# DeepHelper
Here you can find different things.
He can download files on dropbox and send you notification on telegram
## How to install
```{r, engine='bash', count_lines}
pip install https://github.com/ADmitri42/DeepHelper.git
```
## How to use
```{r, engine='python', count_lines}
from deephelper import DeepHelper
dh = DeepHelper("config.json")
dh.send_messages("Hello world")
```
