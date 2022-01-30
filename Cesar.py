from os import system

choix = input("""
  

                                ____                     
                               / ___|___  ___  __ _ _ __ 
                              | |   / _ \/ __|/ _` | '__|
                              | |__|  __/\__ \ (_| | |   
                               \____\___||___/\__,_|_|   
                                  
              
                        #1 : cryptage          #2 : décryptage

                                    [->] Choix : """)

if choix == "1":
    system("cls")
    cryptage = input("""     
                                              _                   
                         ___ _ __ _   _ _ __ | |_ __ _  __ _  ___ 
                        / __| '__| | | | '_ \| __/ _` |/ _` |/ _ |
                       | (__| |  | |_| | |_) | || (_| | (_| |  __/
                        \___|_|   \__, | .__/ \__\__,_|\__, |\___|
                                  |___/|_|             |___/      

                            [->] Entrer votre texte : """)

    system("cls")
    clef = int(input("""
    
                                         _       __ 
                                     ___| | ___ / _|
                                    / __| |/ _ \ |_ 
                                   | (__| |  __/  _|
                                    \___|_|\___|_|  
                                
                                [->] Entrer la clef : """))
    message = [(ord(i)+clef) for i in cryptage]
    message_crypter = [chr(i) for i in message]
    final = "".join(message_crypter)
    print(final)
    fichier = open("text_crypter.txt", "a")
    fichier.write(final)
    fichier.close()

if choix =="2":
    system("cls")
    decryptage = input("""
    
                    _                            _                   
                 __| | ___  ___ _ __ _   _ _ __ | |_ __ _  __ _  ___ 
                / _` |/ _ \/ __| '__| | | | '_ \| __/ _` |/ _` |/ _ |
               | (_| |  __/ (__| |  | |_| | |_) | || (_| | (_| |  __/
                \__,_|\___|\___|_|   \__, | .__/ \__\__,_|\__, |\___|
                                     |___/|_|             |___/      
    
                    [->] Entrer le message a decrypter : """)

    clef2 = int(input("""
    
                                         _       __ 
                                     ___| | ___ / _|
                                    / __| |/ _ \ |_ 
                                   | (__| |  __/  _|
                                    \___|_|\___|_|  
                                
                                [->] Entrer la clef : """))
    message2 = [(ord(i)-clef2) for i in decryptage]
    message_decrypter2 = [chr(i) for i in message2]
    final2 = "".join(message_decrypter2)
    print(final2)
    fichier = open("text_decrypter.txt", "a")
    fichier.write(final2)
    fichier.close()