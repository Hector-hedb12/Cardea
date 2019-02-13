from .fhirbase import fhirbase


class Signature(fhirbase):
    """
    A digital signature along with supporting context. The signature may
    be electronic/cryptographic in nature, or a graphical image
    representing a hand-written signature, or a signature process.
    Different signature approaches have different utilities.

    Attributes:
        type: An indication of the reason that the entity signed this
            document. This may be explicitly included as part of the signature
            information and can be used when determining accountability for
            various actions concerning the document.
        when: When the digital signature was signed.
        whoUri: A reference to an application-usable description of the
            identity that signed  (e.g. the signature used their private key).
        whoReference: A reference to an application-usable description of the
            identity that signed  (e.g. the signature used their private key).
        onBehalfOfUri: A reference to an application-usable description of the
            identity that is represented by the signature.
        onBehalfOfReference: A reference to an application-usable description
            of the identity that is represented by the signature.
        contentType: A mime type that indicates the technical format of the
            signature. Important mime types are application/signature+xml for X ML
            DigSig, application/jwt for JWT, and image/* for a graphical image of
            a signature, etc.
        blob: The base64 encoding of the Signature content. When signature is
            not recorded electronically this element would be empty.
    """

    __name__ = 'Signature'

    def __init__(self, dict_values=None):
        self.type = None
        # Type: array
        # reference to Coding

        self.when = None
        # Type: string

        self.whoUri = None
        # Type: string

        self.whoReference = None
        # reference to Reference: identifier

        self.onBehalfOfUri = None
        # Type: string

        self.onBehalfOfReference = None
        # reference to Reference: identifier

        self.contentType = None
        # Type: string

        self.blob = None
        # Type: string

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Signature',
             'child_variable': 'whoReference'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Signature',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Signature',
             'child_variable': 'onBehalfOfReference'},
        ]
