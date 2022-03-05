from fastapi import APIRouter
from btiapp import views

router = APIRouter()

router.get(
    "/bills/titles",
    summary="Retrieve titles and titlesNoYear information for the dedicated bills.",
    tags=["bill-titles-by-bills"],
    response_model="",
    name="get-bill-titles-by-bills"
)(views.get_bill_titles_by_bills)

router.get(
    "/bills/titles/{billnumber}",
    summary="Retrieve titles and titlesNoYear information for a specific bill.",
    tags=["bill-titles-by-bill"],
    response_model="",
    name="get-bill-titles-by-bill"
)(views.get_bill_titles_by_bill)

router.get(
    "/titles/{title}",
    summary="Retrieve titles and titlesNoYear information that matches to a specific title.",
    tags=["get-matching-titles"],
    response_model="",
    name="get-matching-titles"
)(views.get_matching_titles)

router.post(
    "/bills/titles/{billnumber}",
    summary="Add new title to a specific bill data.",
    tags=["add-new-title-to-bill"],
    response_model="",
    name="add-new-title-to-bill"
)(views.add_new_title_to_bill)