import sys
import os

cwd = os.getcwd()
sys.path.append(cwd)

from backend.src.parser_patient_details import PatientDetailsParser
import pytest

@pytest.fixture()
def doc_1_kathy():
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
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc_2_jerry():
    document_text = '''
Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020
'''
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PatientDetailsParser('')

def test_get_name(doc_1_kathy, doc_2_jerry, doc_3_empty):
    assert doc_1_kathy.get_field('patient_name') == "Kathy Crawford"
    assert doc_2_jerry.get_field('patient_name') == "Jerry Lucas"
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_kathy, doc_2_jerry, doc_3_empty):
    assert doc_1_kathy.get_field('phone_number') == "(737) 988-0851"
    assert doc_2_jerry.get_field('phone_number') == "(279) 920-8204"
    assert doc_3_empty.get_field('phone_number') == None

def test_get_hepb_vaccination(doc_1_kathy, doc_2_jerry, doc_3_empty):
    assert doc_1_kathy.get_field('hepb_vaccination') == "No"
    assert doc_2_jerry.get_field('hepb_vaccination') == "Yes"
    assert doc_3_empty.get_field('hepb_vaccination') == None

def test_get_medical_problems(doc_1_kathy, doc_2_jerry, doc_3_empty):
    assert doc_1_kathy.get_field('medical_problems') == "Migraine"
    assert doc_2_jerry.get_field('medical_problems') == "N/A"
    assert doc_3_empty.get_field('medical_problems') == None

def test_parse(doc_1_kathy, doc_2_jerry, doc_3_empty):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == "Kathy Crawford"
    assert record_kathy['phone_number'] == "(737) 988-0851"
    assert record_kathy['hepb_vaccination'] == "No"
    assert record_kathy['medical_problems'] == "Migraine"

    record_jerry = doc_2_jerry.parse()
    assert record_jerry =={
        'patient_name': "Jerry Lucas",
        'phone_number': "(279) 920-8204",
        'hepb_vaccination': "Yes",
        'medical_problems': "N/A"
    }

    record_empty = doc_3_empty.parse()
    assert record_empty =={
        'patient_name': None,
        'phone_number': None,
        'hepb_vaccination': None,
        'medical_problems': None
    }