import sys
import os

cwd = os.getcwd()
sys.path.append(cwd)

import re

from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
    
    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'hepb_vaccination': self.get_field('hepb_vaccination'),
            'medical_problems': self.get_field('medical_problems')
        }
    
    def get_field(self, field_name):
        
        pattern_dict = {
            'patient_name': ('Birth Date\n\n([A-Za-z\s-]+?)\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', 0),
            'phone_number': ('(\(\d{3}\)\s\d{3}-\d{4})\sWeight', 0),
            'hepb_vaccination': ('Have you had the Hepatitis B vaccination\?.*(Yes|No)', re.DOTALL),
            'medical_problems': ('asthma, seizures, headaches[^a-zA-Z]*([a-zA-Z].*)', 0)
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object[0], self.text, flags=pattern_object[1])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn i
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

'''

    pp = PatientDetailsParser(document_text)
    print(pp.parse())
