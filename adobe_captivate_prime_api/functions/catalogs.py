import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_catalogs(
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
    sort: str = "name",
) -> list:
    """Get a list of catalogs for an account in your organization.

    :param api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :return: list

    """

    sort_options = [
        "name",
        "-name",
        "dateCreated",
        "-dateCreated",
        "dateUpdated",
        "-dateUpdated",
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
        endpoint="catalogs",
        params=params,
    )


def get_catalog(
    api: CaptivatePrimeAPI,
    catalog_id: str,
) -> list:
    """Get detailed information of a catalog. It includes created and updated
    date, name, id, and status.

    :param api: CaptivatePrimeAPI
    :param catalog_id: str
    :return: list

    """

    return api.fetch(
        method="GET",
        endpoint=f"catalogs/{catalog_id}",
    )
