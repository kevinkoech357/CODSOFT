import uuid


# Valid if ID is in uuid format
def is_valid_uuid(user_id):
    """
    Check if the given user ID is in valid UUID format.

    Args:
        user_id (str): The user ID to be validated.

    Returns:
        bool: True if the ID is a valid UUID, False otherwise.
    """
    try:
        uuid.UUID(user_id, version=4)
        return True
    except ValueError:
        return False
