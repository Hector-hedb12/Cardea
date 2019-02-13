from .fhirbase import fhirbase


class EnrollmentResponse(fhirbase):
    """
    This resource provides enrollment and plan details from the processing
    of an Enrollment resource.

    Attributes:
        resourceType: This is a EnrollmentResponse resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        request: Original request resource reference.
        outcome: Processing status: error, complete.
        disposition: A description of the status of the adjudication.
        created: The date when the enclosed suite of services were performed
            or completed.
        organization: The Insurer who produced this adjudicated response.
        requestProvider: The practitioner who is responsible for the services
            rendered to the patient.
        requestOrganization: The organization which is responsible for the
            services rendered to the patient.
    """

    __name__ = 'EnrollmentResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'EnrollmentResponse'
        # Type: string
        # possible values: EnrollmentResponse

        self.status = None
        # Type: string

        self.request = None
        # reference to Reference: identifier

        self.outcome = None
        # reference to CodeableConcept

        self.disposition = None
        # Type: string

        self.created = None
        # Type: string

        self.organization = None
        # reference to Reference: identifier

        self.requestProvider = None
        # reference to Reference: identifier

        self.requestOrganization = None
        # reference to Reference: identifier

        self.identifier = None
        # Type: array
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'request'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'outcome'},
        ]
