def format_message(msg_id, message):
    return f"MSG|{msg_id}|{message}"

def format_ack(msg_id):
    return f"ACK|{msg_id}"

def format_join(group):
    return f"JOIN|{group}"

def parse_message(data):
    parts = data.split("|")

    if len(parts) < 2:
        return None, None, None

    msg_type = parts[0]
    field = parts[1]

    content = None
    if len(parts) > 2:
        content = "|".join(parts[2:])

    return msg_type, field, content