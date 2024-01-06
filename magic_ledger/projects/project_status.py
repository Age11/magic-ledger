ACTIVE = "active"
INACTIVE = "inactive"
DELETED = "deleted"

is_valid_project_status = lambda project_status: project_status in [ACTIVE, INACTIVE, DELETED]