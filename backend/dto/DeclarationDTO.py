from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

class DeclarationDTO(BaseModel):
    activityDate: datetime
    submissionDate: datetime  # The date of submission

    @field_validator('submissionDate')
    @classmethod
    def validate_activity_date(cls, value):
        # Define the minimum date for validation
        min_date = datetime.strptime("2024-01-01", "%Y-%m-%d")

        # Check if the submission date is present
        if value:
            submission_date = value
            
            if submission_date < min_date:
                raise ValueError("Data dokonania czynności nie może być wcześniejsza niż 01.01.2024 r.")
            # Validate the activity date
            if value < min_date:
                raise ValueError("Data dokonania czynności nie może być wcześniejsza niż 01.01.2024 r.")
            if value > submission_date:
                raise ValueError("Data dokonania czynności nie może być późniejsza niż data złożenia deklaracji.")
        
        return value
    

        