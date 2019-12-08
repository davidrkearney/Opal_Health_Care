"""
health_app models.
"""
from django.db.models import fields

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

class TODOItem(models.EpisodeSubrecord):
    job       = fields.CharField(max_length=200)
    due_date  = fields.DateField(blank=True, null=True)
    details   = fields.TextField(blank=True, null=True)
    completed = fields.BooleanField(default=False)



# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""