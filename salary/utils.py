def parse_line(line):

    parts = line.strip().split(',')
    if len(parts) == 2:
        try:
            return int(parts[1])
        except ValueError:
            return None
    return None
