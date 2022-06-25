import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_external_profiles(
    api: CaptivatePrimeAPI,
    offset: int = 0,
    limit: int = 10,
):
    """
    Retrieves a list of external profiles given an account id
    which is subject to necessary permissions
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param offset: int
    :param limit: int
    :return: List
    """

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
    }

    return api.fetch(
        method="GET",
        endpoint="externalProfiles",
        params=params,
    )


def get_external_profile(
    api: CaptivatePrimeAPI,
    external_profile_id: str,
):
    """
    Retrieve an external profile specified by externalProfile id
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param external_profile_id: str
    :return: List
    """

    return api.fetch(
        method="GET",
        endpoint=f"externalProfiles/{external_profile_id}",
    )


def get_all_users_of_external_profile(
    api: CaptivatePrimeAPI,
    external_profile_id: str,
    user_states: str | list = None,
    offset: int = 0,
    limit: int = 10,
):
    """
    Retrieves a list of enrolled users, which is subject to
    necessary permissions, for the mentioned external profile
    specified by the externalProfile id.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param external_profile_id: str
    :param user_states: str or list
    :type user_states: str or list
    :param offset: int
    :param limit: int
    :return: List
    """

    user_states_options = [
        "ACTIVE",
        "DELETED",
        "SUSPENDED",
    ]

    if isinstance(user_states, str):
        if user_states not in user_states_options:
            user_states = None
            logging.debug(
                'Invalid lo_types value, "None" used as default. Expected values: %s',
                user_states_options,
            )
    elif isinstance(user_states, list):
        for user_state in user_states:
            if user_state not in user_states_options:
                user_states.remove(user_state)
                logging.debug(
                    "Invalid user_state value(s) are removed, and used as %s. "
                    "Expected values: %s",
                    user_states,
                    user_states_options,
                )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "filter.userStates": user_states,
    }

    return api.fetch(
        method="GET",
        endpoint=f"externalProfiles/{external_profile_id}/users",
        params=params,
    )


def create_external_profile(
    api: CaptivatePrimeAPI,
):
    """
    Creates an External Profile using given details
    and returns externalProfile created with its id.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError


def update_external_profile(
    api: CaptivatePrimeAPI,
):
    """
    Update an external profile by specifying externalProfile id.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError
