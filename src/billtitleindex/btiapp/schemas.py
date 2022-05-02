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


class TitleMatchWithBill(BaseModel):
    """
    TitleMatchWithBill
    """

    bills: List[str]
    title: str


class BillMatchingTitlesResponse(BaseModel):
    """
    BillMatchingTitlesResponse
    """

    titles: List[TitleMatchWithBill]
    titlesNoYear: List[TitleMatchWithBill]  # List[str]
    hitsTotal: int


class ErrorResponse(BaseModel):
    """
    ErrorResponse
    """

    error: str
