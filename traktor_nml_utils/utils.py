def duration_str_to_milliseconds(duration_str: str):
    """
    Convert duration string (HH:MM:SS) to milliseconds for Cue points
    :param str duration_str: duration string (HH:MM:SS)
    :return:
    """
    h, m, s = duration_str.split(":")
    return float((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)
