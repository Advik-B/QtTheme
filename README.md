# QtTheme
> Are you tired of making custom qt stysheets, do you want add a theme system for app

[**Just use QtTheme**](https://github.com/Advik-B/QtTheme#usage)

## Installation
see [releases](https://github.com/Advik-B/QtTheme/releases)

## Usage

```py

from QtTheme import apply_theme
from PyQt5.QtWidgets import QApplication, QMainWindow

class YourExistingGui(QMainWindow):
  def __init__(self):
    ... # Your existing code
    apply_theme(self, "ubuntu")
 

```

**Or list all themes**
```py

from QtTheme import apply_theme, list_themes
from PyQt5.QtWidgets import QApplication, QMainWindow

class YourExistingGui(QMainWindow):
  def __init__(self):
    ... # Your existing code
    apply_theme(self, list_theme()[0])
 

```

**Or apply random theme**

```py

from QtTheme import apply_random_theme
from PyQt5.QtWidgets import QApplication, QMainWindow

class YourExistingGui(QMainWindow):
  def __init__(self):
    ... # Your existing code
    apply_random_theme(self)
 

```

## License
[MIT](https://github.com/Advik-B/QtTheme/blob/Master/LICENSE.txt)

## Attribution

Some themes are from [qss-stock.devsecstudio.com](https://qss-stock.devsecstudio.com)
