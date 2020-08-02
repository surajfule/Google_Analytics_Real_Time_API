from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from credentials import KEY_FILE_LOCATION, SCOPES


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analytics', 'v3', credentials=credentials)

    return analytics

