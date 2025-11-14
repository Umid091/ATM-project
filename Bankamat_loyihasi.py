import json
import sys


s = {
    "1234567890123456": {
        "owner": "Ali Valiyev",
        "balance": 200000,
        "password": "1234",
        "phone": "+998901234567",
        "blocked":False
    },
    "9876543210987654": {
        "owner": "Vali Aliyev",
        "balance": 500000,
        "password": "4321",
        "phone": None,
        "blocked":True
    },
    "9876541110987654": {
        "owner": "jorayev Umid",
        "balance": 200000,
        "password": "8091",
        "phone": None,
        "blocked":False
    }
}


def w_karta(d: dict):
    with open("kartalar.json", 'w') as f:
        json.dump(d, f, indent=4)


# w_karta(s)

def r_karta():
    with open("kartalar.json", "r") as f2:
        try:
            data=json.load(f2)
            return dict(data)
        except:
            return False
# print(r_karta())

def karta_login():
    data=r_karta()
    karta_number=input(">>>16 xonali karta raqamini kiriting:-->")
    # if data[karta_number]["blocked"]==True:
    #     print("  Bu karta bloklangan!!!!!")
    #     return sys.exit()

    if karta_number in data:
        if data[karta_number]["blocked"]==True:
            print("  Bu karta bloklangan!!!!!")
            return sys.exit()

        count=0
        for i in range(3):
            count+=1
            password=input("passvordni kiriting:-->")
            if password==data[karta_number]["password"]:
                print(f"Xush kelibsiz--> {data[karta_number]['owner']}")


                return {karta_number: data[karta_number]}

            else:
                print(f"parol xato! qolgan urunishlar={3-count} ta")
        print("❌❌Karta bloklandi!!! urnishlr limiti tugadi ")

        data[karta_number]["blocked"]=True
        w_karta(data)
        return sys.exit(None)
    else:
        print("❌Bunday karta topilmadi")
        return sys.exit()


karta=karta_login()
# print(karta)


def show_balance(karta):
    for k in karta:
        # print(k)
        return print(f"Karta balance:{karta[k]['balance']} ")
# show_balance(karta)



def add_balance(karta):
    summa=int(input("Qo‘shiladigan summa: "))
    data=r_karta()
    for i in karta:
        # print(i)
        data[i]['balance'] += summa
        karta[i]['balance']=data[i]['balance']
    w_karta(data)
    print(f"✅ {summa} so'm qo‘shildi! Yangi balans: {karta[i]['balance']} so'm")
# add_balance(karta)



def withdraw_balance(karta):
    summa=int(input("Yechiladigan summani kiriting:-->"))
    for k in karta:
        balance=karta[k]['balance']
        komissiya=int(summa*0.01)
        jami=summa+komissiya
        if jami<balance:
            data=r_karta()
            data[k]['balance']-=jami
            w_karta(data)
            print(f"✅ {summa} so‘m yechildi (komissiya {komissiya}). Yangi balans: {data[k]['balance']} so‘m")
        else:
            print("❌Kartada pul yetarli emas")
# withdraw_balance(karta)



def change_password(karta):
    yangi_password=input("Yangi parolni kiriting -->>")
    for k in karta:
        if yangi_password!=karta[k]['password']:
            data=r_karta()
            data[k]['password']=yangi_password
            w_karta(data)
            return print("✅Parol  yangilandi.")
        else:
            print("❌ Eski parolinggiz kiritib qoydingiz.")
# change_password(karta)


def enable_sms(karta):
    for k in karta:
        if karta[k]['phone']==None:
            tel_raqam=input("Telifon raqamni kiriting:-->>")
            data=r_karta()
            data[k]['phone']=tel_raqam
            w_karta(data)
            return print("✅sms xabarnoma ulandi")
        else:
            print(" Ushbu raqamga sms xabarnomayiz ulangan")

# enable_sms(karta)


def Menu(karta):
    if karta is None:
        print("Dastur to‘xtadi. Login muvaffaqiyatsiz!")
        return


    print('''=====> BOSH MENU <=====
        1.show_balance
        2.add_balance
        3.withdraw_balance
        4.change_password
        5.enable_sms
        6.exit
        ''')


    t=input("Tanlovni tanlang (1-6) -->>")

    if t=="1":
        show_balance(karta)
    elif t=="2":
        add_balance(karta)
    elif t=="3":
        withdraw_balance(karta)
    elif t=="4":
        change_password(karta)
    elif t=="5":
        enable_sms(karta)
    elif t=="6":
        print("=====Xayr=====")


    else:
        print("❌Noto‘g‘ri tanlov")

Menu(karta)
