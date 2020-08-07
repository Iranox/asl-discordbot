import time


def verify_timestamp(string):
    try:
        time.strptime(string, "%Y-%m-%d")
        return True
    except ValueError:
        try:
            time.strptime(string, "%Y-%m-%d %H")
            return True
        except ValueError:
            try:
                time.strptime(string, "%Y-%m-%d %H:%M")
                return True
            except ValueError:
                try:
                    time.strptime(string, "%Y-%m-%d %H:%M:%S")
                    return True
                except ValueError:
                    try:
                        time.strptime(string, "%Y-%m-%dT%H:%M:%S.%f")
                        return True
                    except ValueError:
                        return False
