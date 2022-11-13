import os
import platform
from termcolor

def main():
    DOWNLOAD_PATH = f'C:\\Users\\{os.getuser()}\\Downloads\\' if 'windows' in platform.\
    platform().lower() else f'/home/{os.getser()}/Downloads/'

    downloaded_files = os.listdir(DOWNLOAD_PATH)

    if len(downloaded_files) > 0:
        for file in downloaded_files:
            os.system(f'rm -rf {file}')
        print(colored('Done deleting files.', 'green'))
    else:
        print(colored('No files to clean up!', 'green'))

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(colored('An error has occurred:\n{err}', 'red'))
