from abc import ABC, abstractmethod

class Scrapper(ABC):
    """
    Base class for extracting data from a page
    and putting it in a formatted, markdown comment for reddit
    """
    def __init__(self, dom):
        self.dom: object = dom

    @abstractmethod
    def get_data(self) -> None:
        """
        Extracts the available data from the page
        """
        raise NotImplementedError

    @abstractmethod
    def get_info(self) -> str:
        """
        Returns a formatted comment displaying information
        extracted from the page
        """
        raise NotImplementedError
