import Crypto
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
# 计算签名
from Crypto.Signature import PKCS1_v1_5
# 计算加密解密
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from base64 import b64decode, b64encode
import sys
import uuid
import json


private_key = '-----BEGIN RSA PRIVATE KEY-----\n' \
              'MIIEogIBAAKCAQEAr9+RLRRi3j6yegviWzS4qDCmSzUSAb7AwQ5eU4n9CkfFBP6f\n' \
              '6gOfp7bYFDu/AfJs/HxhVJFPh/64tAXBj+raVnHFCFcKOqUgRJ9QvGDJ3qwJHotI\n' \
              'mOFUhJZ7o20rKGBFpV7W3UFrPx1TcbX9mEgsZs6+YU9JgtZtNhXrIwV2qpwjv7Q6\n' \
              'EC51x5dEZwAQMV13vuxZCvZLIujx7X5cf1kU6PahSUeEb8yPFec1Z7VlkwF0RQI6\n' \
              'rv3voRCX5+m84d9xC8MIseGfXBxAd0QFrY/CqHu4U8c18uGnQp8paw6pjvKIMdOo\n' \
              '8T6PetSZ1azvIziu51/PiULKRERsPXOw8phWwwIDAQABAoIBABhfoPSA50TKppxw\n' \
              'ajHeqBqzB1DT7YdtYrQ+pAbq0DUtBhpvmUTqtKUfG2oOb6W67ay+JhT8wGtl+z4D\n' \
              'sDQcRZ8GTFqgCWxgNw0bkSpSNZfU+ryPbAO38qkfW8ol1n3VfcFx19A5AT5xd3+C\n' \
              'S79ffTvQOiUtQlBOHDuLJReo6a2yE6LOC24sPolZVbQ9qS0G699hXp3TxWx7v++K\n' \
              'TtA79tASSOuMROlt5e9/50De6iv2G0APatiXZKL7nfJTjw7XMek5dPJcILAuVBsQ\n' \
              'g3WGTk0EGaeT5sEsHBbSMGStaTI+Ks898UMbnD/7L4/aSJ0+iRz5sO1JKJy/5h/J\n' \
              'lHmUGgkCgYEAu08ic7ut5zLHLxSjxOoFvYC7DgKdoQyEFbttYQ3WmY+PXAb4YM1x\n' \
              'mqRrcxHdVAtaDEn8bFhtGmAjrrI8qHl2dwcypVBWgia7WQn2PGcFaNl6VjzPuMGB\n' \
              'YZF62WqluaK4utCvFktYmuLZfTux6Tzxg7+0RLKN1j5AJo9nwuq1pUkCgYEA8F7S\n' \
              'OsnvPN4EA77d2osOlmVWD9mzmYVfKzic3BXQBThsRhhghFz7Cp1RO7mal+yxctPW\n' \
              '3WALKxHRwXRuppyhuOHQduQVych7Le/8Nw8pUz8MPnxWHUml6aNhE1zvq5Ez5VN6\n' \
              'x6LtoEW/9kgMSbbkmxwXVCFTum2Hm9blhNX+d6sCgYAeXqxVW37M17zX817CVLdt\n' \
              'jGvHz8DDFgZsh6EqdVXwPAiggTjQaT8cNcB+Pc1HDTgiefSFlKjL9/6RGrEfF+KP\n' \
              'VgluKGJ+Y81ImIbmMEX+RBTD2sRLToStzyq+Cb6pJKsTDzb0RG8vXcyps34bNRhr\n' \
              'pi+SW+kHbbx1BBds0SV2kQKBgDKWskY/M8OqskubgxO4yoQqpbdGST9ZS5NMIe9M\n' \
              'A/DlVBxYiw+whgFQ5MTeJkQtQ5d4MDN9QDx7TpsZhyQ3uO2xUO+Ex3UlZY9gf8OS\n' \
              'xE7J6SjJgFI/qtSGVyr9F1ATikmMjT2w87QUmfcaaMOm42wluF8zeGy3GqBY1Qtl\n' \
              'Al5rAoGAdOx70I3gaHD9MuGElwbSadwXKVVm4u94KP1xg8s6Ru+w+ZRAJ7Y9ovlz\n' \
              '1rxEmfaCOCapkkWVX1pBMnG8Og01dZNMyTcRbYgw1QF4Iz37+w1TBZA72W1cvlm7\n' \
              'nz92lce6EnzwIb1Rmbat7wKN8OGx7etUWUEaGxZSP83JKBWGuc8=\n' \
              '-----END RSA PRIVATE KEY-----'


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


# 进行解密操作
def license_decrypt(license_file_path=None, equipment_id= None):
    """
    解密许可证授权的相关信息如开始时间,结束时间,扫描总量等
    :param license_file_path:
    """
    # 初始化RsaUtil对象
    rsa = RsaUtil()
    try:
        with open(license_file_path) as f:
            encrypt_data = f.read()

        # 对加密的数据进行解密
        decrypt_data = rsa.long_decrypt_by_private_key(msg=encrypt_data, private_key=private_key)
        # 对解密后的数据进行处理
        start_time = decrypt_data.split("-?-")[1]
        end_time = decrypt_data.split("-?-")[3]
        scan_total_num = decrypt_data.split("-?-")[5]
        res_equipment_id = decrypt_data.split("-?-")[7]
        license_status = decrypt_data.split("-?-")[8]
        user_name = decrypt_data.split("-?-")[9]
        if equipment_id != res_equipment_id:
            raise ValueError("解密错误: 错误的服务器ID信息!")
        # if license_status not in ["commercial", "trial_version"]:
        #     raise ValueError("解密错误: 错误的许可证授权状态!")
        if license_status not in ["commercial", "trial_version"]:
            raise ValueError("解密错误: 错误的许可证授权状态!")
        res_dict = dict()
        res_dict["start_time"] = start_time
        res_dict["end_time"] = end_time
        res_dict["scan_total_num"] = scan_total_num
        res_dict["equipment_id"] = res_equipment_id
        res_dict["license_status"] = license_status
        res_dict["user_name"] = user_name
        print(res_dict)
        # 讲结果信息存入到json文件中
        # file_name = str(uuid.uuid4())
        json_str = json.dumps(res_dict)
        with open("result.json", "w") as f:
            f.write(json_str)

    except Exception as e:
        raise ValueError("解密错误: {}".format(e))


if __name__ == '__main__':
    # 命令行参数 第一个是许可证的路径
    license_file_path = sys.argv[1]
    # 命令行参数第二个是设备的ID
    equipment_id = sys.argv[2]
    license_decrypt(license_file_path=license_file_path, equipment_id=equipment_id)







