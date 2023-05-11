import hashlib

class ScOpreater(object):

    def __init__(self) -> None:
        pass

    def encode(self, content:str=''):
        """
        分别对传入字符串进行 sha256，sha1，md5 进行加密，并返回元祖
        ("sha256_encode_str", "sha1_encode_str", "md5_encode_str")
        """

        ret_empty = ('', '', '')
        if not content:
            print('content is emptry')
            return ret_empty

        en_sha256 = ''
        en_sha1 = ''
        en_md5 = ''
        content_b = ''
        try:
            # 使用UTF-8编码将字符串转换为字节串
            content_b = content.encode('utf-8')
        except Exception as e:
            print(e)
            return ret_empty

        try:
            en_sha256 = hashlib.sha256(content_b).hexdigest()
        except Exception as e:
            print(e)

        try:
            en_sha1 = hashlib.sha1(content_b).hexdigest()
        except Exception as e:
            print(e)

        try:
            en_md5 = hashlib.md5(content_b).hexdigest()
        except Exception as e:
            print(e)
        return (en_sha256, en_sha1, en_md5)

    def decode(self, content=None, type=None):
        pass