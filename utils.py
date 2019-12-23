import functools
import time


# 记录POW的工作时间
def time_log(flag=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start_time = time.time()
            func(*args, **kw)
            end_time = time.time()
            print('%s spend time: %.2f s\n' % (func.__name__, (end_time - start_time)))
            if flag:
                pass  # 可以写入日志

        return wrapper
    return decorator
