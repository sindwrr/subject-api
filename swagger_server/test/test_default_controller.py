# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.subject import Subject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_subjects_get(self):
        """Test case for subjects_get

        Retrieve a list of subjects
        """
        response = self.client.open(
            '/subjects',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subjects_post(self):
        """Test case for subjects_post

        Add a new subject
        """
        body = Subject()
        response = self.client.open(
            '/subjects',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subjects_subject_id_delete(self):
        """Test case for subjects_subject_id_delete

        Delete a subject
        """
        response = self.client.open(
            '/subjects/{subjectId}'.format(subject_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subjects_subject_id_get(self):
        """Test case for subjects_subject_id_get

        Get a specific subject
        """
        response = self.client.open(
            '/subjects/{subjectId}'.format(subject_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subjects_subject_id_put(self):
        """Test case for subjects_subject_id_put

        Update a subject
        """
        body = Subject()
        response = self.client.open(
            '/subjects/{subjectId}'.format(subject_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
