from typing import Dict
from typing import List

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
    hitsTotal: int


class ErrorResponse(BaseModel):
    """
    ErrorResponse
    """

    error: str
