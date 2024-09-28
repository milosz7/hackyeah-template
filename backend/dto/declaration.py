from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, conint, validator
from datetime import datetime

class DeclarationDTO(BaseModel):
    activityDate: datetime  # The date of the activity
    submissionDate: datetime  # The date of submission

    @validator('activityDate')
    def validate_activity_date(cls, value, values):
        # Define the minimum date for validation
        min_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        
        # Check if the submission date is present
        if 'submissionDate' in values:
            submission_date = values['submissionDate']
            
            # Validate the activity date
            if value < min_date:
                raise ValueError("Data dokonania czynności nie może być wcześniejsza niż 01.01.2024 r.")
            if value > submission_date:
                raise ValueError("Data dokonania czynności nie może być późniejsza niż data złożenia deklaracji.")
        
        return value
        