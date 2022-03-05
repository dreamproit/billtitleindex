from django.db import models
from django.utils.translation import ugettext_lazy as _
from sqlalchemy import null

    
class BillBasic(models.Model):
    """ 
        ### Bill Basic Information Model 
    """
    BILL_TYPE_CHOICES = (
        ('hr', 'H.R. 1234'),            # It stands for House of Representatives, but it is the prefix used for bills introduced in the House.
        ('hres', 'H.Res. 1234'),        # It stands for House Simple Resolution.
        ('hconres', 'H.Con.Res. 1234'), # It stands for House Concurrent Resolution.
        ('hjres', 'H.J.Res. 1234'),     # It stands for House Joint Resolution.
        ('s', 'S. 1234'),               # It stands for Senate and it is the prefix used for bills introduced in the Senate. Any abbreviation besides "S." is incorrect.
        ('sres', 'S.Res. 1234'),        # It stands for Senate Simple Resolution.
        ('sconres', 'S.Con.Res. 1234'), # It stands for Senate Concurrent Resolution.
        ('sjres', 'S.J.Res. 1234'),     # It stands for Senate Joint Resolution.
    )
    
    # [bill_type][number]-[congress]
    bill_id = models.CharField(verbose_name=_("bill_id"), max_length=20)
    
    # Bill_type can be one of hr, hres, hjres, hconres, s, sres, sjres, sconres. 
    # These are distinct sorts of legislative documents. 
    # Two of these(hr, s) are for bills. The remaining are types of resolutions. 
    # It is important that when you display these types that you use the standard abbreviations.
    # 
    # Simple resolutions only get a vote in their originating chamber. 
    # Concurrent resolutions get a vote in both chambers but do not go to the President. 
    # Neither has the force of law. 
    # Joint resolutions can be used either to propose an amendment to the constitution or to propose a law. 
    # When used to propose a law, they have exactly the same procedural steps as bills.
    bill_type = models.CharField(verbose_name=_("bill_type"), max_length=10, choices=BILL_TYPE_CHOICES)
    
    # The bill number is a positive integer. 
    # Bills die at the end of a Congress and numbering starts with 1 at the beginning of each new Congress.
    number = models.IntegerField(verbose_name=_("number"))
    # [congress][bill_type][number]
    bill_number = models.CharField(verbose_name=_("bill_number"), max_length=20)
    congress = models.IntegerField(verbose_name=_("congress"))
    introduced_at = models.DateField(verbose_name=_("introduction date"), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(verbose_name=_("updated time"), auto_now=False, auto_now_add=False)


class BillTitles(models.Model):
    """ 
        ### Bill Titles Model
    
        Bills can have "official" descriptive titles (almost always), "short" catchy titles (sometimes), and "popular" nickname titles (rare). 
        They can have many of these titles, given at various stages of a bill's life. 
        The current official, short, and popular titles are kept in top-level official_title, short_title, and popular_title fields.
        
        Popular titles are assigned by the Library of Congress, and can be added at any time.
    """
    bill_basic = models.OneToOneField(BillBasic, verbose_name=_("bill_basic"), related_name="billtitles", on_delete=models.CASCADE)
    official_title = models.CharField(verbose_name=_("official_title"), max_length=2000, blank=True, null=True)
    popular_title = models.CharField(verbose_name=_("popular_title"), max_length=2000, blank=True, null=True)
    short_title = models.CharField(verbose_name=_("short_title"), max_length=2000, blank=True, null=True)


class BillStageTitle(models.Model):
    """ 
        ### Bill Status XML Title Model
        
        A bill may have multiple titles for any given stage. 
        `is_for_portion` is `true` when the title is for a portion of the bill, 
        and these titles should not be used when choosing a title for display for the entire bill. 
    """
    TITLE_TYPE_CHOICES = (
        ('O', 'official'),
        ('P', 'popular'),
        ('S', 'short'),
    )
    bill_basic = models.ForeignKey(BillBasic, verbose_name=_("bill_basic"), related_name="billstagetitle", on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("title"), max_length=2000)
    titleNoYear = models.CharField(verbose_name=_("titleNoYear"), max_length=2000)
    type = models.CharField(verbose_name=_("type"), max_length=10, choices=TITLE_TYPE_CHOICES, blank=True, null=True)
    As = models.CharField(verbose_name=_("as"), max_length=50, blank=True, null=True)
    is_for_portion = models.BooleanField(verbose_name=_("is_for_portion"), blank=True, null=True)