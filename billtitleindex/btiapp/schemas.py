from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from typing import List, Dict, Optional
from pydantic import BaseModel


class BillTitlesResponse(BaseModel):
    """
    {
        titles: {
            "CLEAR Act of 2011": [--list of bills that have this title--],
            "Clear Law Enforcement for Criminal Alien Removal Act of 2011": [--list of bills that have this title--],
            "To provide for enhanced Federal, State, and local assistance in the enforcement of the immigration laws, to amend the Immigration and Nationality Act, to authorize appropriations to carry out the State Criminal Alien Assistance Program, and for other purposes.": [--list of bills that have this title--]
        },
        titlesNoYear: {
            "CLEAR Act": [--list of bills that have this title--],
            "Clear Law Enforcement for Criminal Alien Removal Act": [--list of bills that have this title--],
            "To provide for enhanced Federal, State, and local assistance in the enforcement of the immigration laws, to amend the Immigration and Nationality Act, to authorize appropriations to carry out the State Criminal Alien Assistance Program, and for other purposes.": [--list of bills that have this title--]
        }
    }
    """

    titles: Dict[str, List[str]]
    titlesNoYear: Dict[str, List[str]]


class BillsTitlesResponse(BaseModel):

    __root__: Dict[str, BillTitlesResponse]
