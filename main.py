from connect import initialize_analyticsreporting
from functions import print_response, get_report
from credentials import VIEW_ID
from user_requirements_for_data_to_be_fetched import metrics_str, dimensions_str


def fetch_google_analytics_data(analytics):
    return get_report(analytics, VIEW_ID, metrics_str, dimensions_str)


def main():
    analytics = initialize_analyticsreporting()
    response = fetch_google_analytics_data(analytics)
    print_response(response)


if __name__ == '__main__':
    main()
