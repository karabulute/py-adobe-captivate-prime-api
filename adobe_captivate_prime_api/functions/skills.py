import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_skills(
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
    sort: str = "name",
    include: str = None,
) -> list:
    """Get a list of all the skills for an account in your organization. It
    includes the skill name and description of each skill.

    :param api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :param include: str
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
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint="skills",
        params=params,
    )


def get_skill(
    api: CaptivatePrimeAPI,
    skill_id: str,
    include: str = None,
) -> list:
    """Get detailed information of any skill. It includes the skill name and
    description of the skill.

    :param api: CaptivatePrimeAPI
    :param skill_id: str
    :param include: str
    :return: list

    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"skills/{skill_id}",
        params=params,
    )


def search_skill_interest(
    api: CaptivatePrimeAPI,
    skill_interest_types: str,
    limit: int = 10,
    cursor: str = None,
    name_starts_with: str = None,
) -> list:
    """Retrieves a list of skill interest search results whose name contains
    the input query name.

    :param api: CaptivatePrimeAPI
    :param skill_interest_types: str
    :param name_starts_with: str
    :param cursor: str
    :param limit: int
    :return: list

    """

    skill_interest_type_options = [
        "ADMIN_DEFINED",
        "INDUSTRY_ALIGNED",
    ]

    if skill_interest_types not in skill_interest_type_options:
        skill_interest_types = "ADMIN_DEFINED"
        logging.debug(
            'Invalid skill_interest_types value, "ADMIN_DEFINED" used as default. '
            "Expected values: %s",
            skill_interest_type_options,
        )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "filter.skillInterestTypes": skill_interest_types,
        "nameStartsWith": name_starts_with,
    }

    return api.fetch(
        method="GET",
        endpoint="skillInterest/search",
        params=params,
    )
