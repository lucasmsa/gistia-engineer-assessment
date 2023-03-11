def get_google_sheets_csv_url(url: str) -> str:
    """
    Args:
        url (str)
    Returns:
        str: String with a parsed version of Google sheets
             resulting in a CSV
    """

    return url.replace("/edit#gid=", "/export?format=csv&gid=")