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
    alt_name = models.CharField(max_length=255, verbose_name='name', blank=True)
    founders = models.CharField(max_length=255, blank=True)
    directors = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    industry = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    alt_address = models.CharField(max_length=255, blank=True)
    registration_date = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    duns_num = models.CharField(max_length=255, blank=True)
    other = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)


class OfficialBaseModel(BaseModel):
    """Public official base model"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    salaries = UnsavedManyToManyField('OfficialSalary')
    real_estates = UnsavedManyToManyField('OfficialRealEstate')
    movables = UnsavedManyToManyField('OfficialMovable')
    companies = UnsavedManyToManyField('CompanyBaseModel')
    spouse = UnsavedForeignKey('OfficialSpouse', null=True)
    children = UnsavedManyToManyField('OfficialChild')
    other = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)


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
# ============================================================================
# EOF
# ============================================================================
