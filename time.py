from datetime import datetime
import pyperclip
import os
from datetime import datetime
time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')
# 保存到剪切板中
pyperclip.copy(time)


# 将文本显示在在记事本中 
'''
with open('time.txt', 'w+') as f:
    print('现在的时间是：\n' + time, file = f)

os.system('notepad time.txt')
os.system('del /q time.txt')   
'''

