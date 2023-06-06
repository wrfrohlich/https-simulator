from sys import argv
from random import randint
from hashlib import sha256
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from utils import dec_to_hex, hex_to_bytes, byte_to_hex

class HttpsSimulator():
    def __init__(self):
        self.iv_size = 128 #bits
        self.key_size = 128 #bits
        self.p = "%s%s%s%s%s%s%s%s" % ( "B10B8F96A080E01DDE92DE5EAE5D54EC",
                                        "52C99FBCFB06A3C69A6A9DCA52D23B61",
                                        "6073E28675A23D189838EF1E2EE652C0",
                                        "13ECB4AEA906112324975C3CD49B83BF",
                                        "ACCBDD7D90C4BD7098488E9C219A7372",
                                        "4EFFD6FAE5644738FAA31A4FF55BCCC0",
                                        "A151AF5F0DC8B4BD45BF37DF365C1A65",
                                        "E68CFDA76D4DA708DF1FB2BC2E4A4371")

        self.g = "%s%s%s%s%s%s%s%s" % ( "A4D1CBD5C3FD34126765A442EFB99905",
                                        "F8104DD258AC507FD6406CFF14266D31",
                                        "266FEA1E5C41564B777E690F5504F213",
                                        "160217B4B01B886A5E91547F9E2749F4",
                                        "D7FBD7D3B9A92EE1909D0D2263F80A76",
                                        "A6A24C087A091F531DBF0A0169B6A28A",
                                        "D662A4D18E73AFA32D779D5918D08BC8",
                                        "858F4DCEF97C2A24855E6EEB22B3B2E5")

    def custom_values(self):
        self.a = "%s%s%s%s%s%s%s%s" % ( "d7ea9337c772e836e5113f8bb89f6629",
                                        "822ba3efb5bef3dcf4727b0f964bcbbc",
                                        "6b503fbeceab1aa545a7f64d2af406db",
                                        "b36923486aff1304d4f69d294d04f8cf",
                                        "cafdf1d9725aa735e633c28b84e62935",
                                        "a3be3993a4c987467a64be39372892b5",
                                        "977c89c83fe11b22f882e2175d17dc6b",
                                        "86fbb91e7873c0d132c8757675")

        self.Aa = "%s%s%s%s%s%s%s%s" % ("7020D292C8173E88F90EB6656133CA33",
                                        "DB931DBDE43AFE844D8CFFCC50947363",
                                        "AA8530FD429C3F29ED38C91DDDBFC1FB",
                                        "7D239573EBC372331AA89292B2E12AB6",
                                        "8FECA44D720CC5CFB2CEA495AF2A23C9",
                                        "D598862ABA9E33EE4AA88F6922B46ED9",
                                        "6899DFDDD76D41B7117E84250AD37770",
                                        "1BF82351FBFFE6021D461B095C4A4496")

        self.Bb = "%s%s%s%s%s%s%s%s" % ("6465FF74501E724583AE76A9E0DCCBDF",
                                        "BE4A646DF0193A42031B3F958EEE4FF7",
                                        "A9AA6A1C8A90F52F5C3FC76D0670C71D",
                                        "ABA32849FE89DD2DDCE11B15CD790C97",
                                        "8ADD7340CDD9CFBB738580BD01204C60",
                                        "4FDFFA220DC25515D461E7CAC5A7DF20",
                                        "1B9F358D7EA2DDAE2B8FCA64FB242F1C",
                                        "D89DDA853F89D9CFE45B9CDA285C6952")

        self.MSG = "%s%s%s%s%s%s%s" %(  "ABBDE81FFF5F4FC4740A5BD391B441CB",
                                        "2BC4A45FDCFFF4EA73C19C5E5804C5F9",
                                        "8DF745F74AC71E366B695932A88DF44F",
                                        "B7A95DB96BE4989A37FE68D12AF2EB84",
                                        "730A5A183EFD4F59622F6909C64E8043",
                                        "4C1D93DC79FEB7D8CFB309CED2A4FF23",
                                        "F090952BBC9CC28DCAF1677FBB3291DF")

        self.MSG2 =  "%s%s%s%s%s%s%s%s%s%s" % ( "0D058E92ECED6AA2DBB52769055A71F3",
                                                "25569FEFDACA754AAAE4B25AF8E4691A",
                                                "CAD7233F877334201086C3511009E4EA",
                                                "B0D5F70A997EDDAD118C434B6EA83745",
                                                "403F85589F98A9AA7D4D5856D81FCB46",
                                                "D560E90E5A611B3BFE2F8B46904CE142",
                                                "1199D0BA3915272F2DFE1E66696CF04B",
                                                "20B45795EFD0B6DFDFF80BECF4CC521A",
                                                "B28ADD643CB2597F4992725D00AA7CE8",
                                                "0B0E039A516BDEDDB05D5FD58943B222")

        self.MSG3 =  "%s%s%s%s%s" % (   "581112A2A049AE3CE079C01E21BBB905",
                                        "E46A295F8803737261F8989E575DF4E7",
                                        "DCB427FD1FFAFF1569D006FBAE6E63CC",
                                        "FAFB0E9FC14FC6ABF7AF57E1D3BAD52A",
                                        "C34E41CC8C722DC36E5F222231268871")

    def mount_dict(self, value: int)-> dict:
        value_hex = dec_to_hex(value)
        value_bytes = hex_to_bytes(value_hex)
        value_dict = {'dec': value, 'hex': value_hex, 'bytes': value_bytes}
        return value_dict

    def generate_random_a(self, size: int = 1024)-> int:
        a = 0
        for _ in range(size):
            a = (a << 1) | randint(0, 1)
        return a

    def generate_A(self, a: str = None)-> tuple:
        a = self.generate_random_a()
        a = int(a)
        g = int(self.g, 16)
        p = int(self.p, 16)
        Aa = pow(g, a, p)
        Aa = hex(Aa)[2:].upper()
        return a, Aa

    def generate_V(self, a: str = None)-> str:
        a = int(self.a, 16)
        Bb = int(self.Bb, 16)
        p = int(self.p, 16)
        Vv = pow(Bb, a, p)
        Vv = hex(Vv)[2:].upper()
        return Vv

    def calculate_sha256(self, Vv: str)-> str:
        Vv = hex_to_bytes(Vv)
        Ss = sha256(Vv)
        Ss = Ss.hexdigest()
        return Ss

    def get_n_bits(self, Ss: str, bits: int)-> bytes:
        size = int(bits/8)
        Ss = hex_to_bytes(Ss)
        Ss = Ss[:size]
        return Ss

    def generate_key(self)-> str:
        Vv = self.generate_V()
        Ss = self.calculate_sha256(Vv)
        Ss = self.get_n_bits(Ss, self.key_size)
        return byte_to_hex(Ss)

    def decrypt(self, key, ciphertext: str, iv_size: int)-> str:
        iv_size = int(iv_size/8)
        msg = hex_to_bytes(ciphertext)
        key = hex_to_bytes(key)
        iv = msg[:iv_size]
        msg = msg[iv_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher = cipher.decrypt(msg)
        cipher = unpad(cipher, iv_size).decode('utf-8')
        return cipher

    def encrypt(self, key, plaintext: str, iv_size: int)-> str:
        iv_size = int(iv_size/8)
        plaintext = plaintext.encode('utf-8')
        plaintext = pad(plaintext, iv_size)
        iv = Random.new().read(iv_size)
        key = hex_to_bytes(key)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(plaintext)
        ciphertext = byte_to_hex(ciphertext)
        iv = byte_to_hex(iv)
        ciphertext = "%s%s" % (iv, ciphertext)
        return ciphertext.upper()

    def custom_plaintext(self, plaintext: str)-> str:
        return plaintext[::-1]

    def report(self, file: str, text: str)-> None:
        if file == "stage1":
            with open("./results/stage1.txt", "a+") as f:
                f.write("%s\n" % text)
                print(text)
        else:
            with open("./results/stage2.txt", "a+") as f:
                f.write("%s\n" % text)
                print(text)

if __name__ == '__main__':
    https_simulator = HttpsSimulator()
    args = None
    if len(argv) > 1:
        if argv[1] == "stage1":
            ret = https_simulator.generate_A(args)
            https_simulator.report(argv[1], "a : %s" % (ret[0]))
            https_simulator.report(argv[1], "A (hex): %s" % (ret[1]))
            https_simulator.report(argv[1], "\n")
        else:
            pass
    else:
        https_simulator.custom_values()
        key = https_simulator.generate_key()
        https_simulator.report("stage2", "Key: %s" % (key.upper()))
        plaintext = https_simulator.decrypt(key, https_simulator.MSG, https_simulator.iv_size)
        https_simulator.report("stage2", "Received plaintext: %s" % (plaintext))
        plaintext = https_simulator.custom_plaintext(plaintext)
        msg = https_simulator.encrypt(key, plaintext, https_simulator.iv_size)
        https_simulator.report("stage2", "Delivered ciphertext : %s" % (msg))
        plaintext = https_simulator.decrypt(key, msg, https_simulator.iv_size)
        https_simulator.report("stage2", "Delivered plaintext : %s" % (plaintext))
        https_simulator.report("stage2", "\n")




        plaintext = https_simulator.decrypt(key, msg, https_simulator.iv_size)
        print(plaintext)

