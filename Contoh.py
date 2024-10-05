while True :
    try:
        umur = int (input ('masukan umur:'))
        print(f'umur saya adalah(umur)')
        break
    except ValueError:
        print('salah format,masukan angka')

