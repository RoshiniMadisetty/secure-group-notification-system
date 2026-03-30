def create_msg(seq, group, data):
    return f"MSG|{seq}|{group}|{data}"

def create_ack(seq):
    return f"ACK|{seq}"

def create_join(group):
    return f"JOIN|{group}"

def parse_message(msg):
    parts = msg.split("|")

    if parts[0] == "MSG":
        return ("MSG", int(parts[1]), parts[2], parts[3])

    elif parts[0] == "ACK":
        return ("ACK", int(parts[1]), None, None)

    elif parts[0] == "JOIN":
        return ("JOIN", None, parts[1], None)

    return None, None, None, None