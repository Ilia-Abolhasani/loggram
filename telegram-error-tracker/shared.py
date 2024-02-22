import json
from hashlib import sha256
from datetime import datetime, timezone


class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_timestamp_utc():
    current_utc_time = datetime.now(timezone.utc)
    utc_timestamp = int(current_utc_time.timestamp())
    return utc_timestamp
