while True:
    language=input('''Select language :
    for ENG input \'ENG\'
    Türkçe için \'TR\'
    Çıkış için / to exit \'E\'
    : ''')
    if language == 'TR':
        kdvratio=float(input('KDV oranını giriniz : '))
        totrust=input('Yapmak istediğiniz işlem KDV\'siz fiyatı bulmak ve KDV\'yi bulmak için \'KDVSİZ\' yazın, eğer işlem KDV\'li fiyatı bulmak ise \'KDVLİ\' yazınız : ')
        if totrust == 'KDVSİZ':
            fee=float(input('KDV\'li fiyatı giriniz : '))
            withoutKDV=fee/((kdvratio+100)/100)
            KDVfee=fee*kdvratio/100
            print('KDV bedeli :', KDVfee, 'KDV\'siz fiyatı :', withoutKDV )
        elif totrust == 'KDVLİ' :
            fee = float(input('KDV\'li fiyatı giriniz : '))
            withKDV= fee * ((kdvratio+100)/100)
            print('KDV\'li tutar :', withKDV)

    elif language == 'ENG' :
        kdvratio = float(input('Input KDV ratio : '))
        totrust = input('Input \'WITHOUTKDV\' for KDV fee and fee without KDV. Input \'WITHKDV\' for fee wtih KDV: ')
        if totrust == 'WITHOUTKDV' or 'withoutkdv':
            fee = float(input('Input fee : '))
            withoutKDV = fee / ((kdvratio + 100) / 100)
            KDVfee = fee * kdvratio/100
            print('KDV bedeli :', KDVfee, 'KDV\'siz fiyatı :', withoutKDV)
        elif totrust == 'WITHKDV' :
            fee = float(input('Input base fee: '))
            withKDV = fee * ((kdvratio+100)/100)
            print('Fee with KDV :', withKDV)
    elif language == 'E':
        break