import sys

def console_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline()

name = console_input('請輸入名稱：')
print('哈囉, ', name)
