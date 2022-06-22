from os.path import exists, join
from os import mkdir, listdir
from shutil import move
from pathlib import Path
from typing import Tuple

def verify_virtual_env(path : str) -> bool:
    if exists(path):
        return True
    raise FileNotFoundError("VIRTUAL ENV NOT FOUND!")

def move_external_modules(absolute_path : str, directories : Tuple[str]) -> bool:
    external_modules_directory = join(absolute_path, 'source_api', 'external_modules')

    if not exists(external_modules_directory):
        print(f"Mkdir : {external_modules_directory}")
        mkdir(external_modules_directory)
    
    path_to_directory_packages = join(
        absolute_path,
        'lib',
        listdir(f'{absolute_path}lib')[0],
        'site-packages',
        ''
    )

    print(f'Python packages : {path_to_directory_packages}')

    for directory in directories:

        path = join(path_to_directory_packages, directory, '')

        try :
            move(path, join(absolute_path, 'source_api', 'external_modules'))
            print(f'Package {directory} moved with success')
        except FileNotFoundError:
            print(f'Package not found : {directory}')
        except :
            print(f'Exists : {directory}')

if __name__ == '__main__':
    absolute_path = join(Path().absolute(), '')
    verify_virtual_env(join(absolute_path, 'bin', 'pip'))
    move_external_modules(
        absolute_path=absolute_path,
        directories=(
        'certifi', 'charset_normalizer', 'idna', 'requests', 'urllib3'
        )
    )