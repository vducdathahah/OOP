
from abc import ABC

class Person(ABC):
  
    def __init__(self, person_id: str, name: str):
        self.id = person_id
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(ID={self.id}, Name='{self.name}')"

class Patient(Person):
    
    def __init__(self, person_id: str, name: str, diagnosis: str):
        super().__init__(person_id, name)
        self.diagnosis = diagnosis

class Doctor(Person):
   
    def __init__(self, person_id: str, name: str, specialty: str):
        super().__init__(person_id, name)
        self.specialty = specialty

class Nurse(Person):
  
    def __init__(self, person_id: str, name: str):
        super().__init__(person_id, name)
        self.care_logs = []

    def record_care(self, surgery_id: str, notes: str) -> None:
   
        self.care_logs.append(f"Ca mổ {surgery_id}: {notes}")
        print(f"[Điều dưỡng {self.name}] Nhật ký: {notes}")

class Technician(Person):
    
    def __init__(self, person_id: str, name: str, equipment_skill: str):
        super().__init__(person_id, name)
        self.equipment_skill = equipment_skill
