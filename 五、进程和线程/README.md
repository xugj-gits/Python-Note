# 进程和线程

<div align=center><img src="进程和线程.png"/></div>

### 1、多进程

- 在Unix/Linux下，可以使用fork()调用实现多进程。

- 要实现跨平台的多进程，可以使用multiprocessing模块。

- 进程间通信是通过Queue、Pipes等实现的。

