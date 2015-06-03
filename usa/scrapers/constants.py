"""
Module    : constants
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza usa constants


"""
CONTRACTS_URL = 'https://www.usaspending.gov/fpds/fpds.php?detail=c'

CONTRACT_KEYS = ('contracting_auth', 'date', 'desc', 'place', 'price',
                 'transaction_id', 'type', 'url', 'year')

COMPANY_KEYS = ('name', 'alt_name', 'founders', 'directors', 'type',
                'industry', 'address', 'alt_address', 'reg_date',
                'status', 'duns_num', 'url')

DOC_KEYS = ('obligatedAmount', 'signedDate', 'contractingOfficeAgencyID',
            'vendorName', 'streetAddress', 'DUNSNumber', 'phoneNo',
            '@spendingCategory', 'vendorAlternateName', 'city', 'state',
            'registrationDate', 'organizationalType',
            'productOrServiceCode', 'PIID', 'fiscal_year')

KEYS_MAP = {'obligatedAmount': 'price',
            'signedDate': 'date',
            'contractingOfficeAgencyID': 'contracting_auth',
            'vendorName': 'name',
            'streetAddress': 'address',
            'DUNSNumber': 'duns_num',
            'phoneNo': 'phone',
            '@spendingCategory': 'type',
            'vendorAlternateName': 'alt_name',
            'organizationalType': 'company_type',
            'city': 'city',
            'state': 'place',
            'registrationDate': 'reg_date',
            'productOrServiceCode': 'desc',
            'PIID': 'transaction_id',
            'fiscal_year': 'year',
            'url': 'url'}

# ============================================================================
# EOF
# ============================================================================
