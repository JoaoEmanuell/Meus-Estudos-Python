from abc import ABC, abstractmethod
from typing import Type
from PySide2.QtWidgets import QWidget

class WindowInterface(ABC) :
    @abstractmethod
    def __init__(self) -> None :
        """Init
        Create a new instance of the window.
        Create a form.
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

    @abstractmethod
    def show_form(self) -> None :
        """Show the main form of the window

        Raises:
            NotImplementedError: _description_
        """        
        raise NotImplementedError()

    @abstractmethod
    def close_form(self) -> None :
        """Close the main form of the window

        Raises:
            NotImplementedError: _description_
        """        
        raise NotImplementedError()