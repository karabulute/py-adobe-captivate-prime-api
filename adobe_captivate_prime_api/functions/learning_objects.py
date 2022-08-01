import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_learning_objects(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    include: str = None,
    cursor: str = None,
    limit: int = 10,
    sort: str = "name",
    lo_types: str | list = "course",
    ignore_enhanced_lp: bool = True,
):
    """Get the details of all the learning objects that Learner is enrolled,
    completed or enabled by the Admin.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param include: str
    :type include: str
    :param cursor: str
    :param limit: int
    :param sort: str
    :param lo_types: str or list
    :param ignore_enhanced_lp: bool
    :type ignore_enhanced_lp: bool
    :return: List

    """

    sort_options = [
        "name",
        "-name",
        "date",
        "-date",
        "dueDate",
        "effectiveness",
        "rating",
        "-rating",
    ]

    if sort not in sort_options:
        sort = "name"
        logging.debug(
            'Invalid sort value, "name" used as default. Expected values: %s',
            sort_options,
        )

    lo_types_options = [
        "course",
        "learningProgram",
        "jobAid",
        "certification",
    ]

    if isinstance(lo_types, str):
        if lo_types not in lo_types_options:
            lo_types = "course"
            logging.debug(
                'Invalid lo_types value, "course" used as default. Expected values: %s',
                lo_types_options,
            )
    elif isinstance(lo_types, list):
        for lo_type in lo_types:
            if lo_type not in lo_types_options:
                lo_types.remove(lo_type)
                logging.debug(
                    "Invalid lo_type value(s) are removed, and used as %s. "
                    "Expected values: %s",
                    lo_types,
                    lo_types_options,
                )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "filter.loTypes": lo_types,
        "include": include,
        "filter.ignoreEnhancedLP": ignore_enhanced_lp,
    }

    return api.fetch(
        method="GET",
        endpoint="learningObjects",
        params=params,
    )


def get_learning_object(
    api: CaptivatePrimeAPI,
    learning_object_id: str,
    include: str = None,
):
    """Get detailed information of a learning object. It includes learning
    object creation date, published date, updated date, and so on. Refer to
    learning object model for more information.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param learning_object_id: str
    :param include: str
    :type include: str
    :return: List

    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"learningObjects/{learning_object_id}",
        params=params,
    )


def get_instance_summary_of_learning_object(
    api: CaptivatePrimeAPI,
    learning_object_id: str,
    learning_object_instance_id: str,
):
    """Retrieve miscellaneous information about a learningObject Instance viz.
    seatLimit, enrollmentCount, waitlistCount, completionCount.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param learning_object_id: str
    :param learning_object_instance_id: str
    :return: List

    """

    return api.fetch(
        method="GET",
        endpoint=f"learningObjects/{learning_object_id}"
        f"instances/{learning_object_instance_id}/summary",
    )
