from django.db import models


class UnsavedForeignKey(models.ForeignKey):
    """An FK which can point to a unsaved obj"""
    allow_unsaved_instance_assignment = True


class UnsavedManyToManyField(models.ManyToManyField):
    """A M2M field which can point to a unsaved obj"""
    allow_unsaved_instance_assignment = True


class BaseModel(models.Model):
    """base model"""
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=255, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class CompanyBaseModel(BaseModel):
    """Company base model"""
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, verbose_name='name', null=True)
    founders = models.CharField(max_length=255, null=True)
    directors = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    alt_address = models.CharField(max_length=255, null=True)
    reg_date = models.DateField(null=True)
    status = models.CharField(max_length=255, null=True)
    duns_num = models.CharField(max_length=255, null=True)
    other = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=255, null=True)


class OfficialBaseModel(BaseModel):
    """Public official base model"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    # salaries = UnsavedManyToManyField('OfficialSalary')
    # real_estates = UnsavedManyToManyField('OfficialRealEstate')
    # movables = UnsavedManyToManyField('OfficialMovable')
    # companies = UnsavedManyToManyField('CompanyBaseModel')
    # spouse = UnsavedForeignKey('OfficialSpouse', null=True)
    # children = UnsavedManyToManyField('OfficialChild')
    other = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)


class OfficialSpouse(BaseModel):
    """Public official's spouse model"""
    name = models.CharField(max_length=255, blank=True)


class OfficialChild(BaseModel):
    """Public official's child model"""
    name = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    salary = models.CharField(max_length=255, blank=True)
    real_estate = models.CharField(max_length=255, blank=True)
    movables = models.CharField(max_length=255, blank=True)
    companies = models.CharField(max_length=255, blank=True)


class OfficialMovable(BaseModel):
    """Public official movable property"""


class OfficialRealEstate(BaseModel):
    """Public official real estate model"""


class OfficialSalary(BaseModel):
    """public official salary model"""


class ProcurementBaseModel(BaseModel):
    """Procurement base model

    """
    contact_person = models.CharField(max_length=255, blank=True)
    contracting_auth = models.CharField(max_length=255, blank=True, verbose_name='Contracting Authority')
    date = models.DateField(null=True, verbose_name='Contract Date')
    desc = models.CharField(max_length=255, blank=True, verbose_name='Description')
    year = models.CharField(max_length=255, blank=True)
    place = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    transaction_id = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    vendor = UnsavedForeignKey('CompanyBaseModel', null=True)
    other = models.CharField(max_length=255, blank=True)


# ============================================================================
# EOF
# ============================================================================
