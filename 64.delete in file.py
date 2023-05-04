#64.delete in file.py
"""
current path la erunthu file erukkunu pakka
    if os.path.exists(filename)
=>Total file lum delete aakuirum
"""
import os
if os.path.exists("test.text"):
    os.remove("test.text")
    #os.rmdir("floder delete meanse(folder name)")
else:
    print("file not found")
