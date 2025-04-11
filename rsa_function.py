alphabet = {'a':1,"b":2,"c":3,"d":4,"e":5,"f":6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,
            'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':27,'0':28,'1':29,
            '2':30,'3':31,'4':32,'5':33,'6':34,'7':35,'8':36,'9':37,':':38,';':39,"'":40,'"':41,'[':42,']':43,'{':44,
            '}':45,'.':46,',':47,'!':48,'$':49,'%':50,'&':51,'?':52,'|':53,'#':54,'^':55}
ralphabet = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',
             17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:' ',28:'0',29:'1',30:'2',31:'3',
             32:'4',33:'5',34:'6',35:'7',36:'8',37:'9',38:':',39:';',40:"'",41:'"',42:'[',43:']',44:'{',45:'}',46:'.',
             47:',',48:'!',49:'$',50:'%',51:'&',52:'?',53:'|',54:'#',55:'^'}
# this is kind of upsetting to look at, but I promise that it cleans up the dictionary referencing later?
def rsa_encryption(message,key):
    '''
    :param message: an alphanumeric string which contains a-z, 0-9, and spaces
    :param key: a key in the form of (e,d,n)
    :return: the encrypted message using the rsa algorithm for each character
    '''
    message = message.strip().lower()
    encrypted = ''
    for char in message:
        c = 0
        for ch in alphabet.keys():
            if char == ch:
                c = alphabet[char]
                break
            else:
                continue
        e = c**key[0]
        e = e%key[2]
        for ch in ralphabet.keys():
            if e == ch:
                encrypted += ralphabet[ch]
                break
    return encrypted

def rsa_decryption(ctext,key):
    '''
    :param ctext: an alphanumeric string that has been encoded using the rsa encryption function
    :param key: key in the form of (e,d,n)
    :return: the decrypted message using the rsa algorithm for each character
    '''
    decrypted = ''
    for char in ctext:
        c = 0
        for ch in alphabet.keys():
            if char == ch:
                c = alphabet[char]
                break
            else:
                continue
        e = c ** key[1]
        e = e % key[2]
        for ch in ralphabet.keys():
            if e == ch:
                decrypted += ralphabet[ch]
                break
    return decrypted

key = (27,3,55)
c = ''
print("Welcome to the basic RSA encryption program.")
while True:
    print("Options:")
    print("    Decrypt: press 'D'")
    print("    Encrypt: press 'E'")
    print("    Quit program: press 'X'")
    choice = input("Enter your choice: ")
    if choice == 'D' or choice == 'd':
        message = input("Enter message to be decrypted: ")
        print("Below is the decrypted message:")
        print(rsa_decryption(message,key))
    elif choice == 'E' or choice == 'e':
        message = input("Enter message to be encrypted: ")
        print("Below is the encrypted message:")
        print(rsa_encryption(message,key))
    elif choice == 'X' or choice == 'x':
        break
    elif choice == 'debug':
        message = input("Enter message: ")
        encrypted_message = rsa_encryption(message,key)
        print(encrypted_message)
        print(rsa_decryption(encrypted_message,key))
print("Goodbye!")