def numbers():
    try:
        file = open('numbers.txt')
        content : str = file.read()

        nb_list = content.split(',')
        for nb in nb_list:
            if nb.isdigit() == False:
                print("error: Le modele du fichier numbers.txt est incorrect")
                return
        for nb in nb_list:
            print(nb)
    except Exception as e:
        if e.errno == 2:
            print('numbers.txt is not found.\nPlease moove it in the same directory as the script number.py')

if __name__ == '__main__':
    numbers()