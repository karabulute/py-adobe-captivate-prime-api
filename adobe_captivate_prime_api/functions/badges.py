"""Module providing set of Badge API functions."""
import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_badges(
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
    sort: str = "name",
) -> list:
    """Get a list of all badges created for an account in your organization.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :return: list

    """

    sort_options = [
        "name",
        "-name",
    ]

    if sort not in sort_options:
        sort = "name"
        logging.debug(
            'Invalid sort value, "name" used as default. Expected values: %s',
            sort_options,
        )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "sort": sort,
    }

    return api.fetch(
        method="GET",
        endpoint="badges",
        params=params,
    )


def get_badge(
    api: CaptivatePrimeAPI,
    badge_id: str,
) -> list:
    """Get detailed information of a badge. The information includes badge
    name, badge image URL and status of the badge. Refer to badge model.

    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param badge_id: str
    :return: list

    """

    return api.fetch(
        method="GET",
        endpoint=f"badges/{badge_id}",
    )
