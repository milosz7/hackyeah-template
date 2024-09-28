from pydantic import BaseModel, EmailStr, model_validator
from datetime import datetime

class DeclarationDTO(BaseModel):
    Data:        datetime   # 4                                                                                                                                                                                                                                                                                                                                                                                                        
    CelZlozenia: int        # 6
    P_7:         int
    P_20:        int
    P_21:        int
    P_22:        int
    P_23:        str
    P_26:        float
    P_27:        float
    P_46:        float
    P_53:        float
    P_62:        int
    pouczenie:   int

    @model_validator(mode='after')
    def validate_data(self):
        min_date = datetime.strptime("2024-01-01", "%Y-%m-%d")

        if self.Data < min_date:
            raise ValueError("Data dokonania czynności nie może być wcześniejsza niż 01.01.2024 r.")
        
        if self.CelZlozenia != 1:
            raise ValueError("Cel Złozenia musi być równy 1")
        
        if self.P_7 != 1 and self.P_7 != 5:
            raise ValueError("PODMIOT SKŁADAJĄCY DEKLARACJĘ musi być równy 1 lub 5")
        
        if self.P_20 != 1:
            raise ValueError("PRZEDMIOT OPODATKOWANIA musi być równy 1")
        
        if self.P_21 != 0 and self.P_21 != 1 and self.P_21 != 2:
            raise ValueError("MIEJSCE POŁOŻENIA RZECZY LUB WYKONYWANIA PRAWA MAJĄTKOWEGO musi być równy 0 lub 1 lub 2")
        
        if self.P_22 != 0 and self.P_22 != 1 and self.P_22 != 2:
            raise ValueError("MIEJSCE DOKONANIA CZYNNOŚCI CYWILNOPRAWNEJ musi być równy 0 lub 1 lub 2")
        
        if not self.P_23:
            raise ValueError("ZWIĘZŁE OKREŚLENIE TREŚCI I PRZEDMIOTU CZYNNOŚCI CYWILNOPRAWNEJ nie może być puste")
        
        if self.P_26 >= 1000:
            if self.P_26 % 1 != 0:
                raise ValueError("PODSTAWA OPODATKOWANIA DLA UMOWY SPRZEDAŻY musi być zaokrąglone do liczby całkowitej o ile jest większe lub równe od 1000")
            
        # TODO rest
        
        return self   