from zipfile import ZipFile, ZIP_DEFLATED
import pathlib
import os


# Change folder to fit needs
mainFolder = './manga'
#Todo Change this to recognise file location automatically without entering it manually 

for subfolder in pathlib.Path(mainFolder).iterdir():
    if subfolder.is_dir():
        cbz_path = f'{subfolder}.cbz'
        folderToZip = subfolder

        folder = pathlib.Path(folderToZip)

    

        with ZipFile(cbz_path, 'w', ZIP_DEFLATED) as cbz:
            for file in folder.iterdir():
             if file.is_file():   
                   cbz.write(file, arcname=file.name)

# Add section to delete the rest and leave only the chapter number for example = c001