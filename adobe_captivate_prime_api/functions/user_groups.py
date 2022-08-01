import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_user_groups(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
    sort: str = "name",
    read_only: bool = None,
    states: str = None,
    catalog_id: str = None,
) -> list:
    """Get a list of User Groups for an account. It includes the user group
    name, description, state and so on.

    :param api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :param catalog_id: str
    :param read_only: bool
    :param states: str
    :return: list

    """

    sort_options = [
        "name",
        "-name",
        "dateCreated",
        "-dateCrated",
    ]

    if sort not in sort_options:
        sort = "name"
        logging.debug(
            'Invalid sort value, "name" used as default. Expected values: %s',
            sort_options,
        )

    state_options = [
        "Active",
        "Deleted",
    ]

    if states not in state_options:
        states = None
        logging.debug(
            'Invalid sort value, "None" used as default. Expected values: %s',
            state_options,
        )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "sort": sort,
        "catalogId": catalog_id,
        "filter.readOnly": str(read_only),
        "filter.states": states,
    }

    return api.fetch(
        method="GET",
        endpoint="userGroups",
        params=params,
    )


def get_user_group(
    api: CaptivatePrimeAPI,
    user_group_id: str = None,
) -> list:
    """Get detailed information of a single user group. It includes the user
    group name, description, state and so on.

    :param api: CaptivatePrimeAPI
    :param user_group_id: str
    :return: list

    """

    return api.fetch(
        method="GET",
        endpoint=f"userGroups/{user_group_id}",
    )


def search_user_groups(
    api: CaptivatePrimeAPI,
    limit: int = 10,
    cursor: str = None,
    sort: str = "name",
    name_starts_with: str = None,
) -> list:
    """Retrieves a list of User Groups search results whose name contains the
    input query name.

    :param api: CaptivatePrimeAPI
    :param limit: int
    :type limit: int
    :param cursor: str
    :type cursor: str
    :param sort: str
    :type sort: str
    :param name_starts_with: str
    :type name_starts_with: str
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
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "nameStartsWith": name_starts_with,
    }

    return api.fetch(
        method="GET",
        endpoint="userGroups/search",
        params=params,
    )


def get_child_user_groups_of_user_group(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_group_id: str,
    offset: int = 0,
    limit: int = 10,
    sort: str = "id",
    read_only: bool = None,
    states: str = None,
    catalog_id: str = None,
) -> list:
    """Get a list of immediate child User Groups within a User Group. It
    includes the user group name, description, state and so on.

    :param api: CaptivatePrimeAPI
    :param user_group_id: str
    :param offset: int
    :param limit: int
    :param sort: str
    :param catalog_id: str
    :param read_only: bool
    :param states: str
    :return: list

    """

    sort_options = [
        "name",
        "-name",
        "dateCreated",
        "-dateCrated",
    ]

    if sort not in sort_options:
        sort = "name"
        logging.debug(
            'Invalid sort value, "name" used as default. Expected values: %s',
            sort_options,
        )

    state_options = [
        "Active",
        "Deleted",
    ]

    if states not in state_options:
        states = None
        logging.debug(
            'Invalid sort value, "None" used as default. Expected values: %s',
            state_options,
        )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "sort": sort,
        "catalogId": catalog_id,
        "filter.readOnly": str(read_only),
        "filter.states": states,
    }

    return api.fetch(
        method="GET",
        endpoint=f"userGroups/{user_group_id}/userGroups",
        params=params,
    )


def get_all_users_of_user_group(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_group_id: str,
    offset: int = 0,
    limit: int = 10,
    sort: str = "id",
    include: str = None,
) -> list:
    """Retrieves the list of users with the giver user group id.

    :param api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :param sort: str
    :param user_group_id: str
    :param include: str
    :type include: str
    :return: list

    """

    sort_options = [
        "id",
        "-id",
        "name",
        "-name",
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
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"userGroups/{user_group_id}/users",
        params=params,
    )


def add_users_to_user_group(
    api: CaptivatePrimeAPI,
) -> None:
    """Add one or more users to the group.

    :param api: CaptivatePrimeAPI
    :raise NotImplementedError: Not implemented.

    """
    raise NotImplementedError


def delete_users_from_user_group(
    api: CaptivatePrimeAPI,
) -> None:
    """Delete one or more users from the group.

    :param api: CaptivatePrimeAPI
    :raise NotImplementedError: Not implemented.

    """
    raise NotImplementedError
