import Crypto
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
# 计算签名
from Crypto.Signature import PKCS1_v1_5
# 计算加密解密
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from base64 import b64decode, b64encode
import random
import uuid

# 公钥
public_key = '-----BEGIN PUBLIC KEY-----\n' \
             'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr9+RLRRi3j6yegviWzS4\n' \
             'qDCmSzUSAb7AwQ5eU4n9CkfFBP6f6gOfp7bYFDu/AfJs/HxhVJFPh/64tAXBj+ra\n' \
             'VnHFCFcKOqUgRJ9QvGDJ3qwJHotImOFUhJZ7o20rKGBFpV7W3UFrPx1TcbX9mEgs\n' \
             'Zs6+YU9JgtZtNhXrIwV2qpwjv7Q6EC51x5dEZwAQMV13vuxZCvZLIujx7X5cf1kU\n' \
             '6PahSUeEb8yPFec1Z7VlkwF0RQI6rv3voRCX5+m84d9xC8MIseGfXBxAd0QFrY/C\n' \
             'qHu4U8c18uGnQp8paw6pjvKIMdOo8T6PetSZ1azvIziu51/PiULKRERsPXOw8phW\n' \
             'wwIDAQAB\n-----END PUBLIC KEY-----'


# RSA分段加解密工具类
class RsaUtil(object):

    def sign_encrypt(self, message, private_key):
        """ RSA私钥加密 MD5withRSA """
        # digest = SHA.new()
        digest = MD5.new()
        digest.update(message.encode(encoding='utf8'))
        private_key = RSA.importKey(b64decode(private_key))
        signer = PKCS1_v1_5.new(private_key)
        sig = b64encode(signer.sign(digest))
        return sig.decode('utf8')

    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = Crypto.Util.number.size(rsa_key.n) / 8
        reserve_size = 11  # 预留位为11
        if not encrypt:  # 解密时不需要考虑预留位
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    def long_rsa_public_encrypt(self, msg, public_key):
        """ 分段使用公钥加密
        单次加密串的长度最大为(key_size / 8 - 11)
        加密的 plaintext 最大长度是 证书key位数 / 8 - 11, 例如1024 bit的证书，被加密的串最长 1024 / 8 - 11=117,
        解决办法是分块加密，然后分块解密就行了，
        因为 证书key固定的情况下，加密出来的串长度是固定的。
        """
        # base64加密后 再进行RSA加密，也可以选择直接进行RSA加密，这个看业务要求
        msg = b64encode(msg.encode('utf-8'))

        length = len(msg)
        public_key = RSA.importKey(public_key)
        max_length = int(self.get_max_length(public_key))
        pub_obj = Cipher_pkcs1_v1_5.new(public_key)
        # 长度不用分段
        if length < max_length:
            return b64encode(pub_obj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > max_length:
                res.append(pub_obj.encrypt(msg[offset:offset + max_length]))
            else:
                res.append(pub_obj.encrypt(msg[offset:]))
            offset += max_length
        byte_data = b''.join(res)
        fin_data = b64encode(byte_data)
        # 编码返回值修改
        fin_data = fin_data.decode('utf-8')
        return fin_data

    def long_decrypt_by_private_key(self, msg, private_key):
        """ 使用私钥分段解密 """
        msg = b64decode(msg)
        length = len(msg)
        private_key = RSA.importKey(private_key)
        max_length = int(self.get_max_length(private_key, False))
        # 私钥解密
        private_obj = Cipher_pkcs1_v1_5.new(private_key)
        # 长度不用分段
        if length < max_length:
            return b''.join(private_obj.decrypt(msg, b'xyz'))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > max_length:
                res.append(private_obj.decrypt(msg[offset:offset + max_length], b'xyz'))
            else:
                res.append(private_obj.decrypt(msg[offset:], b'xyz'))
            offset += max_length
        # RSA解密后再进行一次base64解密，也可以直接返回，这个看加密的数据有没有base64加密
        de_base_res = b64decode(b''.join(res))
        # 编码修改
        de_base_res = de_base_res.decode('utf-8')
        return de_base_res


# 生成英文随机字符
def generate_random_english_str():
    init_str = ""
    for i in range(300):
        for j in range(100):
            ij = random.randint(65, 90) + random.randint(0, 1) * 32
            init_str += str(chr(ij))
    return init_str


# 生成数字随机字符串
def generate_random_num_str():
    init_str = ""
    for i in range(300):
        for j in range(100):
            ij = random.randint(65, 90) + random.randint(0, 1) * 32
            init_str += str(ij)
    return init_str


# 生成License 文件
def generate_license_file(start_time="", end_time="", scan_total_num=None, equipment_id=None, license_status=None,
                          user_name=None, machine_node_num=None, engine_node_num=None, total_num=None):
    """
    根据相关参数生成License文件
    :param start_time: 开始时间 形如 2022-02-22
    :param end_time: 结束时间  形如 2023-02-22
    :param scan_total_num: 扫描代码总量(G为单位)
    :param equipment_id: 设备id
    :param license_status: 授权许可证状态 有 试用(probation)和 正式(official) 两种
    :param user_name: 客户用户名(和登录账号一致)
    :param machine_node_num: 节点数
    """
    # 参数校验
    if not (scan_total_num >= 1 and type(scan_total_num) == int):
        raise ValueError("扫描总量错误,请检查后重试!")

    if not (scan_total_num and equipment_id):
        raise ValueError("请填写正确的扫描总量或者设备ID信息!")

    if license_status not in ["commercial", "trial_version"]:
        raise ValueError("请填写正确的许可证授权状态!")

    if not user_name:
        raise ValueError("请填写正确的客户用户名!")
    if type(machine_node_num) != str:
        raise ValueError("请填写正确的web节点数!")

    if type(engine_node_num) != str:
        raise ValueError("请填写正确的引擎机器节点数!")

    # 初始化字符串
    first_str = generate_random_english_str()
    second_str = generate_random_num_str()
    third_str = generate_random_num_str()
    four_str = generate_random_english_str()
    five_str = generate_random_english_str()
    six_str = generate_random_num_str()
    seven_str = generate_random_english_str()

    original_str = first_str + "-?-" + str(start_time) + "-?-" + second_str + "-?-" + str(end_time) + "-?-" + \
                   third_str + "-?-" + str(scan_total_num) + "-?-" + four_str + "-?-" + equipment_id + "-?-" + \
                   license_status + "-?-" + user_name + "-?-" + five_str + "-?-" + machine_node_num + "-?-" + six_str \
                   + "-?-" + engine_node_num + "-?-" + seven_str + "-?-" + total_num
    rsa = RsaUtil()
    # 进行加密
    res_data = rsa.long_rsa_public_encrypt(msg=original_str, public_key=public_key)
    return res_data


res = generate_license_file("2022-07-13", "2022-07-31", 500, "FDDC152D-FCF7-48DD-914F-1C46AF2411F4", "commercial",
                            "admin", "9449", "7812", "6430")

# 将加密后的数据生成一个License文件
with open("dist/authorization.license", "w") as f:
    f.write(res)
print("License已生成, 文件名名为: authorization.license")
