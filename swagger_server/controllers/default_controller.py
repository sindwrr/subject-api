import connexion
import six
import time
from swagger_server.models.subject import Subject  # noqa: E501
from swagger_server import util
from swagger_server.metrics import *
from swagger_server.logger import logger
from opentelemetry import trace
from swagger_server.controllers.tracing import tracer
import time
import random


def record_metrics(method, endpoint):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    start_time = time.time()

    def observe_latency(status_code=None):
        duration = time.time() - start_time
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
        if status_code:
            REQUEST_STATUS_CODES.labels(method=method, endpoint=endpoint, status_code=status_code).inc()

    return observe_latency

def subjects_get():  # noqa: E501
    observer = record_metrics("GET", "/subjects")
    with tracer.start_as_current_span("subjects_get") as span:
        try:
            logger.info("Got a GET query")
            span.set_attribute("http.method", "GET")
            span.set_attribute("http.route", "/subjects")

            delay = random.uniform(0.1, 2.0)
            time.sleep(delay)
            span.set_attribute("processing.delay", delay)
            
            observer(status_code="200")
            span.set_status(trace.Status(trace.StatusCode.OK))
            return "GET query success!"
        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            
            observer(status_code="500")
            ERROR_COUNT.labels(method="GET", endpoint="/subjects").inc()
            logger.error(f"Failed to process the GET query: {str(e)}")
            return f"GET query fail! Exception: {str(e)}"


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
