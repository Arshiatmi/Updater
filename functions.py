def compare_versions(server_version: str, client_version: str) -> str:
    if server_version > client_version:
        return 1
    elif server_version < client_version:
        return -1
    else:
        return 0
