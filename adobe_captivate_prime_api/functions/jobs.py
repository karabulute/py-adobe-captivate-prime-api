import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_jobs(
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
    sort: str = "id",
):
    """
    Jobs are requests for asynchronous task executions.
    Get the list of jobs submitted.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :return: List
    """

    sort_options = [
        "id",
        "-id",
        "dateCreated",
        "-dateCreated",
    ]

    if sort not in sort_options:
        sort = "id"
        logging.debug(
            'Invalid sort value, "id" used as default. Expected values: %s',
            sort_options,
        )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "sort": sort,
    }

    return api.fetch(
        method="GET",
        endpoint="jobs",
        params=params,
    )


def get_job(
    api: CaptivatePrimeAPI,
    job_id: str,
):
    """
    Get detailed information about the specified job like
    job type, dateCreated, dateCompleted and status.
    Refer to the job model.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param job_id: str
    :return: List
    """

    return api.fetch(
        method="GET",
        endpoint=f"jobs/{job_id}",
    )


def create_job(
    api: CaptivatePrimeAPI,
):
    """
    Create a new job based on the specified payload.
    For more details:
    https://captivateprime.adobe.com/docs/primeapi/v2/jobApi.html
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    """

    raise NotImplementedError
