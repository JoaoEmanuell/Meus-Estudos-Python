from os.path import join
from os import listdir, remove
from pathlib import Path

from source import MainWindow

def create_tmp() :
    """Create a temporary directory"""    
    path = Path().absolute()
    path = join(path, '.tmp')
    if not Path(path).exists() :
        Path(path).mkdir()

def clear_tmp() :
    """Clear the temporary directory"""
    path = Path().absolute()
    path = join(path, '.tmp', '')
    if Path(path).exists() :
        for file in listdir(path) :
            remove(f'{path}{file}')

if __name__ == '__main__' :
    create_tmp()
    window = MainWindow()
    clear_tmp()