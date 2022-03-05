from typing import List, Dict
from pydantic import BaseModel


class BillTitlesResponse(BaseModel):
    """
        BillTitlesResponse
    """
    titles: Dict[str, List[str]]
    titlesNoYear: Dict[str, List[str]]


class BillsTitlesResponse(BaseModel):
    """
        BillsTitlesResponse
    """
    __root__: Dict[str, BillTitlesResponse]


class BillMatchingTitlesResponse(BaseModel):
    """
        BillMatchingTitlesResponse
    """
    titles: List[str]
    titlesNoYear: List[str]