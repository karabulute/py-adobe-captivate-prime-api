import logging

from adobe_captivate_prime_api import CaptivatePrimeAPI


def get_all_users(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    include: str = None,
    offset: int = 0,
    limit: int = 10,
    cursor: str = None,
    sort: str = "id",
    user_filter: str = None,
    user_id: str = None,
):
    """
    Get the list of all the users available for
    your organization’s Captivate Prime account.
    It includes the list of all users with their names,
    badge details, points earned and so on
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param include: str
    :type include: str
    :param cursor: str
    :param user_filter: str
    :param offset: int
    :param limit: int
    :param sort: str
    :param user_id: str
    :return: List
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

    filter_options = [
        "gamification",
        "gamificationAll",
    ]

    if user_filter not in filter_options:
        user_filter = None
        logging.debug(
            'Invalid filter value, "None" used as default. Expected values: %s',
            filter_options,
        )

    params = {
        "page[offset]": offset,
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "include": include,
        "filter": user_filter,
        "userId": user_id if user_filter == "gamification" else None,
    }

    return api.fetch(
        method="GET",
        endpoint="users",
        params=params,
    )


def get_user(
    api: CaptivatePrimeAPI,
    user_id: str,
    include: str = None,
):
    """
    Get the detailed information of any user
    for your account. It includes the user name,
    email-id, badges, points earned and so on
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param include: str
    :return: List
    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}",
        params=params,
    )


def get_all_badges_of_user(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_id: str,
    limit: int = 10,
    cursor: str = None,
    sort: str = "dateAchieved",
    include: str = None,
):
    """
    Get a list of user badges for a user in your organization
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param limit: int
    :param sort: str
    :param cursor: str
    :param user_id: str
    :param include: str
    :type include: str
    :return:
    """

    sort_options = [
        "dateAchieved",
        "-dateAchieved",
    ]

    if sort not in sort_options:
        sort = "dateAchieved"
        logging.debug(
            'Invalid sort value, "dateAchieved" used as default. Expected values: %s',
            sort_options,
        )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/userBadges",
        params=params,
    )


def get_badge_of_user(
    api: CaptivatePrimeAPI,
    user_id: str,
    badge_id: str,
    include: str = None,
):
    """
    Get detailed information of a user badge.
    It includes id, type, badge name and learner name
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param badge_id: str
    :param include: str
    :type include: str
    :return:
    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/userBadges/{badge_id}",
        params=params,
    )


def get_user_groups_of_user(
    api,
    user_id: str,
    offset: int = 0,
    limit: int = 10,
    sort: str = "name",
):
    """
    Get a list of User Groups for a User.
    It includes the user group name, description, state and so on
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param offset: int
    :param limit: int
    :param sort: str
    :return: List
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
        endpoint=f"users/{user_id}/userGroups",
        params=params,
    )


def get_all_user_skills_of_user(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_id: str,
    include: str = None,
    offset: int = 0,
    limit: int = 10,
    sort: str = "dateAchieved",
):
    """
    Get detailed information of a user skill.
    It includes id, type, points earned, created and archived date
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param include: str
    :param offset: int
    :param limit: int
    :param sort: str
    :return: List
    """

    sort_options = [
        "dateAchieved",
        "-dateAchieved",
    ]

    if sort not in sort_options:
        sort = "dateAchieved"
        logging.debug(
            'Invalid sort value, "dateAchieved" used as default. Expected values: %s',
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
        endpoint=f"users/{user_id}/userSkills",
        params=params,
    )


def get_user_skill_of_user(
    api: CaptivatePrimeAPI,
    user_id: str,
    user_skills_id: str,
    include: str = None,
):
    """
    Get detailed information of a user skill.
    It includes id, type, points earned, created and archived date
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param user_skills_id: str
    :param include: str
    :return: List
    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/userSkills/{user_skills_id}",
        params=params,
    )


def get_all_user_notifications_of_user(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_id: str,
    cursor: str = None,
    limit: int = 10,
    read: bool = None,
    announcements_only: bool = False,
    language: str = "en_US",
    user_selected_channels: str | list = None,
):
    """
    Get the list of all the users available for
    your organization’s Captivate Prime account.
    It includes the list of all users with their names,
    badge details, points earned and so on
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param cursor: str
    :param limit: int
    :param read: bool
    :param announcements_only: bool
    :param language: str
    :param user_selected_channels: str or list
    :return: List
    """

    user_selected_channels_options = [
        "jobAid::adminEnrollment",
        "certification::adminEnrollment",
        "certification::autoEnrollment",
        "certification::completed",
        "certification::badgeIssued",
        "certification::completionReminder",
        "certification::expired",
        "certification::recurrenceEnrollment",
        "certification::republished",
        "certification::learnerCertificationApprovalRequestApproved",
        "certification::learnerCertificationApprovalRequestDenied",
        "certification::deadlineMissed",
        "course::adminEnrollment",
        "course::autoEnrollment",
        "course::badgeIssued",
        "course::l1FeedbackPrompt",
        "course::deadlineMissed",
        "course::completed",
        "course::completionReminder",
        "course::sessionReminder",
        "course::republished",
        "course::courseOpenForEnrollment",
        "course::learnerEnrollmentRequestApproved",
        "course::learnerEnrollmentRequestDenied",
        "course::waitListCleared",
        "course::learnerNominationRequest",
        "learningProgram::adminEnrollment",
        "learningProgram::autoEnrollment",
        "learningProgram::badgeIssued",
        "learningProgram::republished",
        "learningProgram::deadlineMissed",
        "learningProgram::completionReminder",
        "learningProgram::completed",
        "learningProgram::l1Feedback",
        "competency::assigned",
        "competency::badgeIssued",
        "competency::achieved",
        "manager::added",
        "admin::added",
        "author::added",
        "integrationAdmin::added",
        "social::commentedOnPost",
        "social::curationRequest",
        "social::commentedOnComment",
        "social::postLive",
        "social::postRejected",
        "social::reportAbuse",
        "social::addedAsModerator",
        "social::postUploadFailed",
        "announcement::received",
    ]

    if user_selected_channels not in user_selected_channels_options:
        user_selected_channels = None
        logging.debug(
            'Invalid filter value, "None" used as default. Expected values: %s',
            user_selected_channels_options,
        )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "read": str(read),
        "announcementsOnly": str(announcements_only),
        "language": language,
        "userSelectedChannels": user_selected_channels,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/userNotifications",
        params=params,
    )


def get_all_user_skill_interests_of_user(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_id: str,
    skill_interest_types: str,
    include: str = None,
    offset: int = 0,
    limit: int = 10,
    sort: str = "dateAchieved",
):
    """
    Get detailed information of a user skill interest.
    It includes id, user_id, skill_id, created date and source of creation
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param skill_interest_types: str
    :param include: str
    :param offset: int
    :param limit: int
    :param sort: str
    :return: List
    """

    sort_options = [
        "dateCreated",
        "-dateCreated",
    ]

    if sort not in sort_options:
        sort = "dateCreated"
        logging.debug(
            'Invalid sort value, "dateCreated" used as default. Expected values: %s',
            sort_options,
        )

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
        "page[offset]": offset,
        "page[limit]": limit,
        "sort": sort,
        "include": include,
        "filter.skillInterestTypes": skill_interest_types,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/skillInterests",
        params=params,
    )


def get_all_enrollments_of_user(  # pylint:disable=too-many-arguments
    api: CaptivatePrimeAPI,
    user_id: str,
    include: str = None,
    cursor: str = None,
    limit: int = 10,
    sort: str = "name",
    lo_types: str | list = "course",
    states: str = None,
):
    """
    Get the details of all the learning objects that
    Learner is enrolled, completed or enabled by the Admin
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param include: str
    :type include: str
    :param cursor: str
    :param limit: int
    :param sort: str
    :param lo_types: str or list
    :param states: str
    :return: List
    """

    sort_options = [
        "dateEnrolled",
        "-dateEnrolled",
    ]

    if sort not in sort_options:
        sort = "dateEnrolled"
        logging.debug(
            'Invalid sort value, "dateEnrolled" used as default. Expected values: %s',
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

    state_options = [
        "active",
    ]

    if states not in state_options:
        states = None
        logging.debug(
            'Invalid sort value, "None" used as default. Expected values: %s',
            state_options,
        )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "include": include,
        "filter.loTypes": lo_types,
        "filter.states": states,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/enrollments",
        params=params,
    )


def get_enrollment_of_user(
    api: CaptivatePrimeAPI,
    user_id: str,
    enrollment_id: str,
    include: str = None,
):
    """
    Get specific enrollment given user's id and enrollmentId
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param enrollment_id: str
    :param include: str
    :return: List
    """

    params = {
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/enrollments/{enrollment_id}",
        params=params,
    )


def get_all_accounts_of_email(
    api: CaptivatePrimeAPI,
    email: str,
    only_active: bool = True,
    social_enabled_accounts: bool = False,
):
    """
    Get a list of all Captivate Prime accounts for a given email id.
    This API does not require an authentication check.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param email: str
    :param only_active: bool
    :param social_enabled_accounts: bool
    :return: List
    """

    params = {
        "onlyActive": str(only_active),
        "socialEnabledAccounts": str(social_enabled_accounts),
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{email}/accounts",
        params=params,
    )


def get_all_user_badges_of_user_for_learning_object(  # pylint:disable=too-many-arguments,line-too-long  # noqa: E501
    api: CaptivatePrimeAPI,
    user_id: str,
    learning_object_id: str,
    include: str = None,
    cursor: str = None,
    limit: int = 10,
    sort: str = "name",
):
    """
    Get the details of all the learning objects that
    Learner is enrolled, completed or enabled by the Admin.
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :param user_id: str
    :param learning_object_id: str
    :param include: str
    :param cursor: str
    :param limit: int
    :param sort: str
    :return: List
    """

    sort_options = [
        "dateAchieved",
        "-dateAchieved",
    ]

    if sort not in sort_options:
        sort = "dateAchieved"
        logging.debug(
            'Invalid sort value, "dateAchieved" used as default. Expected values: %s',
            sort_options,
        )

    params = {
        "page[limit]": limit,
        "page[cursor]": cursor,
        "sort": sort,
        "include": include,
    }

    return api.fetch(
        method="GET",
        endpoint=f"users/{user_id}/learningObjects/{learning_object_id}/userBadges",
        params=params,
    )


def enroll_user_to_instance_of_learning_object(
    api: CaptivatePrimeAPI,
):
    """
    Post a request to enroll to a learning object by specifying
    the learning object id and learning object instance id
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError


def add_external_gamification_point_to_user(
    api: CaptivatePrimeAPI,
):
    """
    Add gamification points gained by learner on external systems
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError


def redeem_external_gamification_point_of_user(
    api: CaptivatePrimeAPI,
):
    """
    Takes the gamification points redeemed by a user from
    an external portal and marks it as redeemed in Prime
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError


def create_learner_module_grade_for_use(
    api: CaptivatePrimeAPI,
):
    """
    Takes the attributes that are provided and creates a Learner module
    grade record. Returns the learner module grade that is created
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """
    raise NotImplementedError


def update_enrollment_of_user(
    api: CaptivatePrimeAPI,
):
    """
    Update user's enrollment by providing userId and enrollmentId.
    Presently only lastAccessDate can be updated, other fields
    if present in the body will be ignored
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def delete_enrollment_of_user(
    api: CaptivatePrimeAPI,
):
    """
    Place a request to un-enroll a user from
    a learning object instance by passing the enrollment id
    :param api: CaptivatePrimeAPI
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def create_user(
    api: CaptivatePrimeAPI,
):
    """
    Takes the attributes that are provided and creates a user.
    Returns a user with the corresponding user id populated
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def delete_user(
    api: CaptivatePrimeAPI,
):
    """
    Delete the user with the given user id
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def update_user(
    api: CaptivatePrimeAPI,
):
    """
    Learner can modify bio, uiLocale, contentLocale, timezone
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def add_skill_interest_to_user(
    api: CaptivatePrimeAPI,
):
    """
    Add a user skill interest
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError


def delete_skill_interest_of_user(
    api: CaptivatePrimeAPI,
):
    """
    Delete a user skill interest
    :type api: CaptivatePrimeAPI
    :return:
    :rtype:
    """

    raise NotImplementedError
