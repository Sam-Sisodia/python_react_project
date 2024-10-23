from enum import Enum

class UserRole(Enum):
    INDIVIDUAL = "individual"
    ENTERPRISE = "enterprise"
    GOVERNMENT = "government"
    REGULAR = "regular"  # Adding REGULAR for your print statement

# Printing the REGULAR user role
print(UserRole.REGULAR)
