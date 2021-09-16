import uuid


def generate_id() -> str:
    """
    Generates unique id 
    """
    return uuid.uuid4().hex
