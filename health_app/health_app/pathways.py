from opal.core.pathway import PagePathway
from health_app import models


class AddPatient(PagePathway):
    display_name = "Add Patient"
    slug = "add_patient"
    icon = 'fa-plus'

    steps = [
        models.Demographics
    ]