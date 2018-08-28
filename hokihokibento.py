def printMainMenu() :
    inputUser = input("Main Menu : \n 1. Lihat Menu\n 2. Lihat Cart\n 3. Checkout\n 4. Keluar\n\n Pilih Menu : ");
    return inputUser;

def printMenu(menuList) :
    print("Pilihan Menu : ");
    for i in range(0, len(menuList)) :
        print(str(i + 1) + ". " + menuList[i]);
    inputUser = input("Mau yang mana? : ");
    return [int(inputUser)-1, menuList[int(inputUser)-1]];

def printCart(cartList) :
    print("Isi Cart : ");
    for i in range(0, len(cartList)) :
        print(str(i + 1) + ". " + cartList[i][1]);

def checkout(cartList, hargaList) :
    # while True :
        totalHarga = 0;
        print("Item yang dipilih : ");
        for i in range(0, len(cartList)) :
            print(str(i + 1) + ". " + cartList[i][1]);
            totalHarga += hargaList[cartList[i][0]];
        inputDuit = input("Total Harga Rp. " + str(totalHarga) + "\n\n Duit Anda Berapa? : ");
        if(int(inputDuit) < totalHarga):
            print("Uang Anda Kurang!");
            checkout(cartList, hargaList);
        else :
            print("Kembaliannya : Rp. " + str(int(inputDuit) - totalHarga));
            # break;


listMenu = ["Paket Bento A Rp. 20.000", "Paket Bento B Rp. 25.000", "Paket Bento C Rp. 30.000"];
listHarga = [20000, 25000, 30000];
listCart = [];

while True :
    pilihanUser = printMainMenu();
    if(pilihanUser == "1") :
        listCart.append(printMenu(listMenu));
    elif(pilihanUser == "2") :
        printCart(listCart);
    elif(pilihanUser == "3") :
        checkout(listCart, listHarga);
        listCart = [];
    elif(pilihanUser == "4") :
        print("Terima Kasih, dan sampai jumpa lagi!!");
        break;
    