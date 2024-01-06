SUPPLIER = "supplier"
CLIENT = "client"
AFFILIATE = "affiliate"
PROJECT = "project"

is_valid_org_type = lambda org_type: org_type in [SUPPLIER, CLIENT, AFFILIATE, PROJECT]

