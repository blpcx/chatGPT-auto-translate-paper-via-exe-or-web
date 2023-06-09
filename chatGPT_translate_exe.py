import os
import time
import pyautogui
import pyperclip

# 需添加的文本
new_text = """
填入需要翻译的文本
"""

# 填入原始文本，包含占位符 {}
# 基本的翻译任务模板
original_text = """
论文翻译任务：英译汉

翻译要求
把xxx领域的期刊论文从英文翻译成中文。确保准确翻译专业术语和表达方式，坚持文章的逻辑结构和语言风格，清晰地传达作者的观点。使用权威的xxx领域的翻译材料作为专业术语，并考虑翻译的可读性和通用性。回答将包括译文、专业术语释义、关键句解读以及主要观点概括。

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

# 将新文本填入原始文本，复制到剪贴板
filled_text = original_text.format(new_text)
pyperclip.copy(filled_text)

# 双击快捷键或者程序exe，启动应用程序（示例使用binjie09提供的桌面程序，或者自己熟悉的客户端；网页版可能出现无法自动控制打开网页的问题，本人编程小白暂时舍弃)
os.system('快捷键路径或者程序exe路径')

# 等待应用程序启动并加载完成
time.sleep(5)

# 定位程序的提问框并粘贴文本
# 打开软件将输入框截图，命名为'question_box.png'，截图保存在python脚本所在文件夹例如c/用户/你的名字
question_box_loc = pyautogui.locateCenterOnScreen("question_box.png") 
pyautogui.click(question_box_loc)
pyautogui.hotkey('ctrl', 'v')

# 自动点击发送按钮
send_button_loc = pyautogui.locateCenterOnScreen("send_box.png") # 同上需截图保存'send_box.png'
pyautogui.click(send_button_loc)

# 运行本代码，即可在客户端看到自动输入问题并生成解答，祝顺利！
