from proofOfWork import sha256, time_log

"""
实现简易区块链
连接区块链，区块链的验证
"""


class Block:
    def __init__(self, pre_hash: str, data: str, nonce=1):
        self.pre_hash = pre_hash
        self.data = data
        self.nonce = nonce  # 演示用 To Do: 确保足够随机
        self.hash = self.compute_hash()

    def compute_hash(self):
        return sha256(self.data + self.pre_hash + str(self.nonce))

    @time_log(flag=0)
    def mine(self, difficulty):
        head = '0' * difficulty
        while True:
            if self.compute_hash()[:difficulty] != head:
                self.nonce += 1  # simple display
            else:
                self.hash = self.compute_hash()
                break
        print("挖矿结束, Hash:%s" % self.hash)


# 区块的链
class Chain:
    def __init__(self):
        self.chain = [self.__genesis()]
        self.difficulty = 5

    @staticmethod
    def __genesis():
        return Block("_", "genesis block")

    @property
    def last_block(self):
        return self.chain[-1]

    # 添加区块到区块链上
    def add_block(self, new_block: Block):
        new_block.pre_hash = self.last_block.hash
        # new_block.hash = new_block.compute_hash()
        new_block.mine(self.difficulty)
        self.chain.append(new_block)

    def validate_chain(self):
        if len(self.chain) == 1:
            if self.chain[0].hash != self.chain[0].compute_hash():
                print("genesis区块被篡改")
                return False
            return True

        # 从第一个区块开始验证
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            if block.hash != block.compute_hash():
                print("第%d个区块被篡改" % i)
                return False
            pre_block = self.chain[i-1]
            if block.pre_hash != pre_block.hash:
                print("第%d个和前一个区块断裂" % i)
                return False
        return True

    def __str__(self):
        result = ""
        for i in range(0, len(self.chain)):
            result += (self.chain[i].data + " : " + self.chain[i].pre_hash + " : " + self.chain[i].hash + "\n")
        return result


if __name__ == '__main__':
    c = Chain()
    block1 = Block("", "支付10元")
    block2 = Block("", "支付20元")
    block3 = Block("", "支付20元")
    c.add_block(block1)
    c.add_block(block2)
    c.add_block(block3)
    print(c)

    # 尝试篡改数据
    c.chain[2].data = "支付0元"
    print(c.validate_chain())

    # 尝试篡改区块
    c.chain[2].data = "支付0元"
    c.chain[2].hash = c.chain[2].compute_hash()
    print(c.validate_chain())
