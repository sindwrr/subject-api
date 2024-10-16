import connexion
import six

from swagger_server.models.subject import Subject  # noqa: E501
from swagger_server import util


def subjects_get():  # noqa: E501
    """Retrieve a list of subjects

    Fetch a list of all the subjects in the curriculum. # noqa: E501


    :rtype: List[Subject]
    """
    return 'do some magic!'


def subjects_post(body):  # noqa: E501
    """Add a new subject

    Add a new subject to the curriculum. # noqa: E501

    :param body: Subject information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Subject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def subjects_subject_id_delete(subject_id):  # noqa: E501
    """Delete a subject

    Delete a specific subject from the library using its ID. # noqa: E501

    :param subject_id: ID of the subject to delete
    :type subject_id: int

    :rtype: None
    """
    return 'do some magic!'


def subjects_subject_id_get(subject_id):  # noqa: E501
    """Get a specific subject

    Fetch details of a specific subject using its ID. # noqa: E501

    :param subject_id: ID of the subject to retrieve
    :type subject_id: int

    :rtype: Subject
    """
    return 'do some magic!'


def subjects_subject_id_put(body, subject_id):  # noqa: E501
    """Update a subject

    Update the details of an existing subject. # noqa: E501

    :param body: Updated subject information
    :type body: dict | bytes
    :param subject_id: ID of the subject to update
    :type subject_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Subject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
