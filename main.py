import os
from heic2png import HEIC2PNG

# FOLDER WITH .HEIC PICS
dir_path = r'C:\Users\jakub\Desktop\Alfa zdjecia\HEIC\Alfa'

# LIST TO STORE FILE NAMES
res = []

if __name__ == "__main__":

    for path in os.listdir(dir_path):
        # CHECK IF CURRENT PATH IS FILE
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    print('Work in progress...')
    for resx in res:
        heic_img = HEIC2PNG(dir_path+'/'+resx)
        heic_img.save()
        # print(resx + ' przekonwertowano! Pozostało: ' + str(len(res)-res.index(resx)-1))

    print('Converted all .HEIC to .PNG!')