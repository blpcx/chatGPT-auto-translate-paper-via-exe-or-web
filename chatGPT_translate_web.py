
import time
import pyautogui
import pyperclip
import webbrowser

# 需添加的文本
new_text = """
需要翻译的内容
"""

# 填入原始文本，包含占位符 {}
original_text = """
论文翻译任务：英译汉

翻译要求
把xxx领域的期刊文章从英文翻译成中文。确保准确翻译专业术语和表达方式，坚持文章的逻辑结构和语言风格，清晰地传达作者的观点。使用权威的生物医学翻译材料作为专业术语，并考虑翻译的可读性和通用性。回答将包括译文、专业术语释义、关键句解读以及主要观点概括。

原文如下：
{}

回答模板如下（用markdown语法编写)

### 译文：

### 专业术语释义（表格）
| 英文专业术语 | 中文释义 |

### 关键句解读
1. 关键句1原文（引入话题）：
- 解释：
- 上下文作用：

2. 关键句2原文（展开话题）：
- 解释：
- 上下文作用：

3. 关键句3原文（转入主题）：
- 解释：
- 上下文作用：

4. 关键句4原文（展开论述）：
- 解释：
- 上下文作用：

5. 关键句5原文（结果&结论）：
- 解释：
- 上下文作用：

### 主要观点概括（语言精炼）
……
"""

# 将新文本填入原始文本，复制到剪贴板，其实复制到剪切板就已经决定成功了，后面最多就是手动粘贴，当然最好是能自动控制
filled_text = original_text.format(new_text)
pyperclip.copy(filled_text)

# 打开网页,好处是一直在同一个对话里，同一文章的内容方便集中讨论（保证浏览器全屏，截图才有用）
url = 'https://chat4.aichatos.com/#/chat/1681674791485'
webbrowser.open(url)
time.sleep(5)   # 等待页面加载完成
input_pos = pyautogui.locateOnScreen('question_box_web.png')  # 是指输入框的截图图片
input_x, input_y = pyautogui.center(input_pos)
pyautogui.click(input_x, input_y)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter') # 用enter键代替发送键，gui点击操作直观但是有时无法识别
