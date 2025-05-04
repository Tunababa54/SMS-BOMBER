from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

# Servisleri belirleme
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print("""{}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&~:^B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@&^.~7:#@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#G@@@@@@@@@@&@@@@@@~.~^P!^&@@@@&&@@@@@@@@@#G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&!:Y&@@@@@@@!?&@@@7 !~.PB^!@@@G!P@@@@@@@G~:G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@! .5&@@@@@P.?@@J :J7:5#G:?@#^~&@@@@@B~ :#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y..Y#&@@@@!.GG..!J^.5B#5.Y7:G@@@&#G~.!&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G^:7PG#@@B::. ^?~. !BB#Y..7@@&GGY^:Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&7:~5GP#@7  .!^   !B###?.P&PPG?^~Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G?5B&@@@@@&!:7PBBG:  :7.   ^5PBBB7:PBB5J?!..!@@@&BYJ&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY~.:?B&@5.::?B#^   ~:    .^:PGGB~^B#BJ:.^~.YP77JG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J:?..~~.!P?.^^   :?:    :GPPY?#G^^5!.^7:J?.^^7&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J.~!7.:.~J.^:    .!!     :B##G~~PG: .~^. J#!  ^!5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG! .: .. ^7.       :?^     .JYYY^  ^:      .~?. ^?:!B#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@~:~~~~~~~!~~5&&&&&&&&&!          .          .     .........               .   !&@@@@&&&&&&&@@&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&.^&&&&&&&&&P:.:~~:.^~~.    :::. :::::::. :::.     P&&&&&&&&? .::::::.  .:::::::^!GJ^~~~~~~^~::~~~~~~^.?@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&.~@@@5~~5@@@! Y&@5 :B&&J .Y&&5..B@&&&&&!.B@@?     #@@B~~~~~:~#&&&&&&&? !@@&&&&&&? ^#&&&&&&&? !&&&&&&B.~@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@.~@@@!  !@@&! 5@@5  .G@@5G@@Y  .#@&7... .B@@?     #@@G...   ?@@#:.G@@5 7@@#:.5@@P 7@@#^.^PG7 7@@&:....J@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@.~@@@GJJG@@@! 5@@5   .P@@@&?   .#@&#GG^ .B@@?     #@@&&&&G. ?@@#  P@@Y !@@&!^P@@P !@@#..777: 7@@@BB5.7@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@.~&@&&#BBBG?. 5@@5   :B@&@&Y.  .#&&PJ?. .B@&7    .#&&B!!!~  ?@@B  P@@Y 7&@&&&&&P^ !@@#.^&@@Y 7&&&YJ7 7@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@.~&&#^.777?YJ Y&&Y  ^#@#!P&&5. .#&&7:.:..B&&J:::. #&&5      ?@&B^:G&&Y 7&&B:Y&&5. !&&#^:P&&Y 7&&#^..:.J@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@.^&&#:^@@@@@G Y&&Y !#&G:..Y#&P..B&&####!.G&#####7 B&&5      ~B&&###&B~ !&&P. J#&5 :G&###&&&? !&&####B.!@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@~:~!~:7@@@@@B:^~~^:!!~^7&P^~!!^:~~~~~~~::^~^~^^^..:::.       .:^!!!!~J!^!!~^7^~~!^::~~!!~!~~^^!777777~Y@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GGGBBGP55Y5YYYYJJ??7~~:::..        ~GB#BB#BGB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&!^???:.~??7. ^~ .!.  ^?77~.  :?.  .!!7!.  :??7::&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.Y&P5^ .YB^. JB :G~  ?G:~B^  7&.  JB:^G!  J&5Y^.B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# ^JY&?  ?P   ?&!?G^  ?G^!G^  7&.  JB~!G!  ^JJBJ G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&~^!!!^J~::.?Y~!77~ . .^^^:   :~^YY^!77~.~~~7!!^?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@P^J&@@@&#&&7.7.     .!::&@@&&&&&P7J#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&??#@@@@@@@@@@~^P7. .~5!.#@@@&@@@@@&5!B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#@@@@@@@&@@@@#.!G5?YGJ.5@@@@@&@@@@@@&#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@P.?GGG5.7@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@?.YGP^:&@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&^^P!.B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:^.5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G.7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))

    try:
        menu = input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: ")
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: " + Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: " + Fore.LIGHTGREEN_EX, end="")
            kere = input()
            kere = int(kere) if kere else None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        if kere is None:
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value) and not attribute.startswith('__'):
                        exec("sms." + attribute + "()")
                        sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value) and not attribute.startswith('__'):
                            if sms.adet == kere:
                                break
                            exec("sms." + attribute + "()")
                            sleep(aralik)

        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                threads = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    threads.append(t)
                    t.start()
                for t in threads:
                    t.join()

        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
