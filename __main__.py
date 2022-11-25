from ctypes import windll

from source.manager.SceneManager import SceneManager

# Avoid the blurry font in Windows 10 - Reference: https://stackoverflow.com/a/43046744
windll.shcore.SetProcessDpiAwareness(1)

if __name__ == '__main__':
    root = SceneManager()
    root.mainloop()
