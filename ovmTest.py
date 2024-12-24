import random
import string
import subprocess

from ovm import bridge


def generate_random_string(length=20):
    """
    生成指定长度的随机字符串。

    参数：
        length (int): 字符串长度，默认为20。

    返回：
        str: 随机生成的字符串。
    """
    # 定义可选字符集（大小写字母和数字）
    characters = string.ascii_letters + string.digits
    # 使用 random.choices 从字符集中随机选择字符
    random_str = ''.join(random.choices(characters, k=length))
    return random_str



if __name__ == "__main__":

    workerName = "Worker" + generate_random_string()

    output = subprocess.run(['/app/ovminiminer-linux-x64', '--pool', f'stratum+tcp://0x44938313d3b8a3d1e29b571ec92eb34cd1b8cbfa.{workerName}@pool-core-testnet.inichain.com:32672./iniminer-linux-x64',
                                      '--pool', f'stratum+tcp://0x44938313d3b8a3d1e29b571ec92eb34cd1b8cbfa.{workerName}@pool-core-testnet.inichain.com:32672iniminer-linux-x64',
                                      '--pool', f'stratum+tcp://0x44938313d3b8a3d1e29b571ec92eb34cd1b8cbfa.{workerName}@pool-core-testnet.inichain.com:32672'], timeout=10800)

    bridge.submit(["bool", "string"], [True, "success"])