from .fhirbase import fhirbase


class GraphDefinition(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.

    Attributes:
        resourceType: This is a GraphDefinition resource
        url: An absolute URI that is used to identify this graph definition
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this graph definition is (or will be)
            published. The URL SHOULD include the major version of the graph
            definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        version: The identifier that is used to identify this version of the
            graph definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the graph
            definition author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence.
        name: A natural language name identifying the graph definition. This
            name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        status: The status of this graph definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this graph definition
            is authored for testing purposes (or education/evaluation/marketing),
            and is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the graph definition was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the graph definition
            changes.
        publisher: The name of the individual or organization that published
            the graph definition.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the graph
            definition from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate graph definition
            instances.
        jurisdiction: A legal or geographic region in which the graph
            definition is intended to be used.
        purpose: Explaination of why this graph definition is needed and why
            it has been designed as it has.
        start: The type of FHIR resource at which instances of this graph
            start.
        profile: The profile that describes the use of the base resource.
        link: Links this graph makes rules about.
    """

    __name__ = 'GraphDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'GraphDefinition'
        # Type: string
        # possible values: GraphDefinition

        self.url = None
        # Type: string

        self.version = None
        # Type: string

        self.name = None
        # Type: string

        self.status = None
        # Type: string
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # Type: boolean

        self.date = None
        # Type: string

        self.publisher = None
        # Type: string

        self.contact = None
        # Type: array
        # reference to ContactDetail

        self.description = None
        # Type: string

        self.useContext = None
        # Type: array
        # reference to UsageContext

        self.jurisdiction = None
        # Type: array
        # reference to CodeableConcept

        self.purpose = None
        # Type: string

        self.start = None
        # Type: string

        self.profile = None
        # Type: string

        self.link = None
        # Type: array
        # reference to GraphDefinition_Link

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'GraphDefinition_Link',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'link'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'useContext'},
        ]


class GraphDefinition_Link(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.

    Attributes:
        path: Path in the resource that contains the link.
        sliceName: Which slice (if profiled).
        min: Minimum occurrences for this link.
        max: Maximum occurrences for this link.
        description: Information about why this link is of interest in this
            graph definition.
        target: Potential target for the link.
    """

    __name__ = 'GraphDefinition_Link'

    def __init__(self, dict_values=None):
        self.path = None
        # Type: string

        self.sliceName = None
        # Type: string

        self.min = None
        # Type: int

        self.max = None
        # Type: string

        self.description = None
        # Type: string

        self.target = None
        # Type: array

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class GraphDefinition_Target(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.

    Attributes:
        type: Type of resource this link refers to.
        profile: Profile for the target resource.
        compartment: Compartment Consistency Rules.
        link: Additional links from target resource.
    """

    __name__ = 'GraphDefinition_Target'

    def __init__(self, dict_values=None):
        self.type = None
        # Type: string

        self.profile = None
        # Type: string

        self.compartment = None
        # Type: array
        # reference to GraphDefinition_Compartment

        self.link = None
        # Type: array
        # reference to GraphDefinition_Link

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'GraphDefinition_Compartment',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition_Target',
             'child_variable': 'compartment'},

            {'parent_entity': 'GraphDefinition_Link',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition_Target',
             'child_variable': 'link'},
        ]


class GraphDefinition_Compartment(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.

    Attributes:
        code: Identifies the compartment.
        rule: identical | matching | different | no-rule | custom.
        expression: Custom rule, as a FHIRPath expression.
        description: Documentation for FHIRPath expression.
    """

    __name__ = 'GraphDefinition_Compartment'

    def __init__(self, dict_values=None):
        self.code = None
        # Type: string

        self.rule = None
        # Type: string
        # possible values: identical, matching, different, custom

        self.expression = None
        # Type: string

        self.description = None
        # Type: string

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.rule is not None:
            for value in self.rule:
                if value is not None and value.lower() not in [
                        'identical', 'matching', 'different', 'custom']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'identical, matching, different, custom'))
