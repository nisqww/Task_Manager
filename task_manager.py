import datetime


def signup():
    print("Lütfen Kullacıcı Adınzı giriniz")
    username = input("Kullanıcı Adı")
    password = input("Şifre")

def user_information(ussnm,pssd):
    name = input("Lürfen Adınızı Giriniz: ")
    address = input("Adresiniz")
    age = input("Yaşınız Lütfen")
    ussnm_ = ussnm+ " task.txt"

    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Adress : ")

    f.write(address)
    f.write('\n')
    f.write("Age : ")
    f.write(age)
    f.write('\n')
    f.close()


def signup():
    print("Lütfen Girmek istediğiniz Hesabın Kullanıcı Adını Giriniz")
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")
    user_information(username, password)


def login():
    print("Lütfen Kullanıcı Adını girinz")
    user_nm = input("Kullanıcı Adı: ")

    pssd_wr = (input("Şifreyi giriniz: "))+ '\n'
    
    try:
        usernm = user_nm+ "task.txt"
        f_ = open(usernm, 'r')
        k = f_.readlines(0)[0]
        f_.close()

        if pssd_wr == k:
            print("1--Verilerinizi görmek için \n2-- Görev eklemek için \n3-- Güncellemek için \n4 -- Görevlerin durumunu görmek için")
        else:
            print("Kullanıcı Adı ya da Şifreniz Yanlış, Lütfen tekrar deneyiniz")
    except Exception as e:
        print(e)
        login()


def signup():
    print("Lütfen Kullıcı Adını Giriniz")       
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")
    user_information(username, password)
    print("Lütfen Giriş İşlemini Tamamlayınız")
    login()


def login():
    print("Lütfen Kullanıcı Adınızı Giriniz")
    user_nm = input("Kullanıcı Adı: ")

    pssd_wr = (input("Şifreniz: "))+'\n'

    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')

        k = f_.readlines(0)[0]
        f_.close()

        while pssd_wr == k:
            print("1--Verilerinizi Görmek İçin \n2--Görev Eklemek İçin \n3--Güncellemek İçin \n4--Görevlerin durumunu görmek için")
            a = input()

            if a == '1':
                view_data(usernm)
            elif a == '2':
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Yalnış Giriş ! ")
        else:
            print("Kullanıcı Adı ya da Şifre Yanlış")
            login()

    except Exception as e:
        print(e)
        login()

def view_data(username):
    pass
def task_information(username):
    pass
def task_update(username):
    pass
def task_update_viewer(username):
    pass


def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close

def task_information(username):
    print("Eklemek İstediğiniz Görevin Numarasını Giriniz")
    j = int(input())
    f1 = open(username,'a')

    for i in range(1,j+1):
        task = input("Görevi giriniz")
        target = input("Hedefi Giriniz")
        pp = "TASK "+str(i)+ ' :'
        qq = "TARGET "+str(i)+" :"

        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')

        print("Ekleme İşlemini Bitirdiyseniz Boşluk Tuşuna Basınız. ")
        s = input()
        if s == ' ':
            break
    f1.close

def task_update(username):
	username = username+" TASK.txt"
	print("Lütfen Tamamladığınız Görev Sayısını Giriniz: ")
	
	task_completed = input()
	print("Lütfen Daha Başlamadığınız Görevlerin Sayısını Giriniz: ")
	
	task_not_started = input()
	print("Lütfen Şuanda Yapmak Olduğunuz Görevleri Giriniz: ")
	
	task_ongoing = input()
	fw = open(username, 'a')
	DT = str(datetime.datetime.now())
	
	fw.write(DT)
	fw.write("\n")
	fw.write("TAMAMLANMIŞ GÖREVLER \n")
	fw.write(task_completed)
	fw.write("\n")
	fw.write("YAPILAN GÖREVLER \n")
	fw.write(task_ongoing)
	fw.write("\n")
	fw.write("BAŞLANMAMIŞ GÖREVLER\n")
	fw.write(task_not_started)
	fw.write("\n")


def task_update_viewer(username):
	ussnm = username+" TASK.txt"
	o = open(ussnm, 'r')
	print(o.read())
	o.close()




if __name__ == '__main__':
	print("GÖREV YÖNETİCİSİNE HOŞGELDİNİZ")
	print("BU PROGRAMDA YENİ MİSİNİZ")
	a = int(input("YENİYSENİZ 1'E BASINIZ. HALİHAZIRDA KULLANICIYSANIZ 0'A BASINIZ ::"))
	
	if a == 1:
		signup()
	elif a == 0:
		login()
	else:
		print("YANLIŞ TUŞLAMA YAPTINIZ !")
