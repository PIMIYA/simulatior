# Document

程式會讀取 `.yaml` 檔案(目前預設使用 `actions.yaml` )來當作腳本執行，

每個動作都有固定的參數以及該動作特有的參數，所有的動作會以固定參數 `time` 來做排序後依序執行；

以下會介紹所有參數。

## Action type

固定參數:

```text
id: str, browser id, 若操作對象非 browser 則可以不必有
type: int, Action type 的表示值
args: { }, 各動作特有參數
```

### OPEN_BROWSER = 100

開啟瀏覽器

參數說明:

```text
x: int, 起始位置 X，預設 10
y: int, 起始位置 Y，預設 10
```

### OPEN_URL = 101

訪問網址

參數說明:

```text
url: string, 網址。
```

### TRIGGER_ELEMENT_INDEX = 102

依照 Index 訪問網頁上的元素

參數說明:

```text
element: string, HTML element tag。
index: int, 第 x 個元素，若無該元素則不會作用；若 index 超過元素數量則會選擇最後一個。
```

### TRIGGER_ELEMENT_RANDOM = 103

隨機訪問網頁上的元素

參數說明:

```text
element: string, HTML element tag。
```

### DRAG_BROWSER_WIN = 104

拖曳瀏覽器視窗

參數說明:

```text
offset_x: int = 0 移動 X 距離(-往右 +往左)
offset_y: int = 0 移動 Y 距離(-往上 +往下)
duration: float = 0.3 拖曳的時間
```

### RESIZE_BROWSER_WIN = 105

改變瀏覽器大小

參數說明:

```text
target_width: int 目標寬
target_height: int 目標高
move_duration: float = 0.3 移動到視窗右下的時間
drag_duration: float = 0.3 拖曳大小的時間
```

### CLOSE_BROWSER_WIN = 106

關閉瀏覽器

參數說明:

```text
無
```

### MOUSE_MOVE = 200

移動滑鼠。

參數說明:

```text
x: int, 螢幕上的座標 X，有左至右。
y: int, 螢幕上的座標 Y，由上至下。
duration: float, 花 x 秒數來到達目的。
```

### MOUSE_CLICK = 201

點擊滑鼠左鍵

參數說明:

```text
x: int, 座標 X
y: int, 座標 Y
```

### MOUSE_DOUBLECLICK = 202

雙擊滑鼠左鍵

參數說明:

```text
無
```

### MOUSE_CLICK_RIGHT = 203

點擊滑鼠右鍵

參數說明:

```text
x: int, 座標 X
y: int, 座標 Y
```

### KEY_PRESS = 300

按下鍵盤按鍵，可用的按鍵請參考下方[合法的按鍵字串](#合法的按鍵字串)

參數說明:

```text
key: string or list, 鍵盤按鍵
presses: int, 按下幾次，預設為 1
interval: float, 間隔幾秒按下一次，預設為 0.0
```

### KEY_TYPEWRITE = 301

輸入一串文字，只能英數。
若有中文需求可能需要使用 [pyperclip](https://github.com/asweigart/pyperclip)
透過 copy/paste 的方式製造出輸入中文的樣子

參數說明:

```text
text: string, 輸入的文字。
interval: float, 每個字的間隔
```

### KEY_HOTKEY = 302

組合按鍵，例如 `CTRL + v`，可用的按鍵請參考下方[合法的按鍵字串](#合法的按鍵字串)

參數說明:

```text
key1: string, 組合按鍵 1。
key2: string, 組合按鍵 2。
```

## 合法的按鍵字串

```python
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

Reference: [KEYBOARD_KEYS](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)