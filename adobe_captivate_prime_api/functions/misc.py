"""Module providing set of Miscellaneous API functions."""
from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_account_info(
    api: CaptivatePrimeAPI,
) -> list:
    """Get detailed information for an account in your organization.

    :param api: CaptivatePrimeAPI
    :return:

    """

    return api.fetch(
        method="GET",
        endpoint="account",
    )


def check_elthor_support(
    api: CaptivatePrimeAPI,
    version: str,
) -> list:
    """Checks if a version of the elthor desktop app is supported.

    :param api: CaptivatePrimeAPI
    :param version: str
    :return: list

    """

    params = {
        "version": version,
    }

    return api.fetch(
        method="GET",
        endpoint="elthor/check",
        params=params,
    )


def get_user_info(
    api: CaptivatePrimeAPI,
    include: str,
) -> list:
    """Get the detailed information of the user who is currently logged in.

    :param api: CaptivatePrimeAPI
    :param include: str
    :return: list

    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint="user",
        params=params,
    )


def go(  # pylint:disable=invalid-name
    api: CaptivatePrimeAPI,
) -> None:
    """Go Urls. Authentication is not required.

    :param api: CaptivatePrimeAPI
    :raise NotImplementedError: Not implemented.

    """

    raise NotImplementedError
