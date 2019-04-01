# coding = utf-8
import os
pid = os.fork()
if pid == 0:
    print('子进程', os.getpid(), os.getppid())
else:
    print('父进程', os.getpid(), os.getppid())

