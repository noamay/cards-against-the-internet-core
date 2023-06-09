import random
import string


def generate_random_id(length=6, used_ids: list[str] = None) -> str:
    letters = string.ascii_uppercase + string.digits
    random_id = ''.join(random.choice(letters) for i in range(6))
    if random_id in used_ids:
        return generate_random_id(length, used_ids)
    return random_id
