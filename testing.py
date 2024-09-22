from test1 import *

def main():
    msg = 'encryption'
    print("Original Message :", msg)

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)  # Private key for receiver
    h = power(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)
    print("privatekey : ", key)

    en_msg, p, k = encrypt(msg, q, h, g)
    print("senderkey",k)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg);
    print("sender key : ", k)

if __name__ == '__main__':
    main()