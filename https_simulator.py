
from sys import argv
from random import randint

class HttpsSimulator():
    def __init__(self):
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

    def generate_A(self, a = None):
        a = self.generate_random_a()
        a = int(a)
        p = int(self.p, 16)
        g = int(self.g, 16)
        A_dec = pow(g, a, p)
        A_hex = hex(A_dec)[2:].upper()
        return a, A_dec, A_hex
    
    def generate_random_a(self):
        a = 0
        for _ in range(1000):
            a = (a << 1) | randint(0, 1)
        return a

    def report(self, file, text):
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
            https_simulator.report(argv[1], "A (dec): %s" % (ret[1]))
            https_simulator.report(argv[1], "A (hex): %s" % (ret[2]))
            https_simulator.report(argv[1], "\n")
        else:
            pass
