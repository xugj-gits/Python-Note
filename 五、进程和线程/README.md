# 进程和线程

<div align=center><img src="进程和线程.png"/></div>

### 1、多进程

- 在Unix/Linux下，可以使用fork()调用实现多进程。

- 要实现跨平台的多进程，可以使用multiprocessing模块。

- 进程间通信是通过Queue、Pipes等实现的。

- 如果要启动大量的子进程，可以用进程池(Pool)的方式批量创建子进程

### 2、 多线程

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

- 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

- Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

### 3、 ThreadLocal

- 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
- ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

[use_threadlocal.py](use_threadlocal.py)

### 4、分布式进程
在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
- Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

- 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。