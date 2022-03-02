from typing import List, Optional
from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/bill/titles")
def get_bill_titles_by_bills(bills: List[str]):
    pass

@app.get("/bills/titles/{billnumber}")
def get_bill_titles_by_bill():
    pass

@app.get("/titles/{title}")
def get_matching_titles(fuzzy: Optional[bool] = True):
    pass


@app.post("/bill/titles/{billnumber}")
def add_new_title_to_bill():
    pass