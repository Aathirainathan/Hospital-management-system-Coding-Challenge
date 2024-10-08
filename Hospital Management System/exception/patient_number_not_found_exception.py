import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient number not found."):
        self.message = message
        super().__init__(self.message)
