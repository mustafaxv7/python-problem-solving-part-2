# This Programm is Ceaser Cipher method to protect conversations
def CeaserCipher(sentence , key):# code
    sentence = sentence.split(" ")
    Ciphered_sentence = " "
    for i in sentence:
        Ciphered_sentence+= " "
        for letter in i.lower():
            Ciphered_sentence += chr(ord(letter) + key)
    return Ciphered_sentence

def CeaserDecipher(codedSentence , key):#decode
    codedSentence = codedSentence.split(" ")
    Deciphered_sentence = " "
    for i in codedSentence:
        Deciphered_sentence+=" "
        for letter in i.lower():
            Deciphered_sentence+= chr(ord(letter) - key)
    return Deciphered_sentence
while True:
    print("\n\n1.Press One To Code Your Message\n")
    print("\n2.Press Two To Decode Your Message\n")
    option = int(input("\nChoose an Option>>: "))
    if option == 1:
        sentece_to_protect = input("\n\nEnter Your Sentence To Code it >>: ")
        key = int(input("\n\nEnter The Key of Protection >>: "))
        print(f"\n\nThe Protected Message is >>> \t\"\"{CeaserCipher(sentece_to_protect,key)} \"\"\n\n\n")
    elif option == 2:
        sentece_to_show = input("\n\nEnter Your Sentence To Decode it >>: ")
        key = int(input("\n\nEnter The Key >>: "))
        print(f"\n\nThe Decoded Message is >>> \t\"\"{CeaserDecipher(sentece_to_show,key)} \"\"\n\n\n")
    else:
        print("\n\nNo Option With This Number\n\n")
    kill_program = input("\n\nDo You Want To Exit ? (Y/N) >> ")
    if kill_program == "Y" or kill_program == "y":
        break

  
