from abc import ABC, abstractmethod
from typing import Type
from PySide6.QtWidgets import QWidget

class MainWindowInterface(ABC) :
    @abstractmethod
    def __init__(self) -> None :
        """Init
        Create a new instance of the main window.
        Create all forms.
        Set all button events.
        Create a app and exec_().
        Create a buttons events.

        Raises:
            NotImplementedError: _description_
        """        
        raise NotImplementedError()

    @abstractmethod
    def load_ui(self, ui_file : str) -> Type[QWidget] :
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        raise NotImplementedError()
