"""
共识机制在以前一般被称为证明方式（Proof），因为比特币采用工作量证明（即Proof-Of-Work，简写为POW）
POW系统构建区块的过程一般称为“挖矿”（mine）
即算力越大，挖到块的可能性越大，维护区块链安全的权重越大
"""

import hashlib
import time


# sha256哈希值
def sha256(data):
    sha = hashlib.sha256()
    sha.update(data.encode('utf-8'))
    return sha.hexdigest()


# 记录POW的工作时间
def time_log(flag=0):
    def showtime(func):
        def wrapper(a):
            start_time = time.time()
            func(a)
            end_time = time.time()
            print('%s dot %s spend time: %.2f\n' % (func.__name__, a, (end_time - start_time)))
            if flag:
                pass  # 可以写入日志

        return wrapper

    return showtime


@time_log(flag=0)
def proof_of_word(prefix: str):
    data = 'luolin'
    x = 1
    while True:
        if sha256(data + str(x))[:len(prefix)] == prefix:  # 匹配区块的前nw位hash值
            print(sha256(data + str(x)))
            break
        else:
            x += 1


if __name__ == '__main__':
    proof_of_word("100")  # 0.01s
    proof_of_word("1000")  # 0.15s
    proof_of_word("10000")  # 7.32s
