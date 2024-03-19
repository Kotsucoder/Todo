import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive('/Users/screenbones/Documents/Screenbones/Classes/Python/Bonus/compressed.zip', 
                    '/Users/screenbones/Documents/Screenbones/Classes/Python/Bonus')