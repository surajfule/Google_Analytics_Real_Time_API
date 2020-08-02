import gc
from googleapiclient.errors import HttpError
from json_file_operations import write_data_to_file, write_data_to_backup_json_file, read_data_from_backup_json_file


def get_report(analytics, view_id, metrics_str, dimensions_str):
    """Queries the Analytics Reporting API V4.

  Args:
    :param analytics: An authorized Analytics Reporting API V4 service object.
    :param view_id:
  Returns:
    The Analytics Reporting API V4 response.
  """

    try:
        return analytics.data().realtime().get(
            ids=view_id,
            metrics=metrics_str,
            dimensions=dimensions_str).execute()

    except TypeError as error:
        # Handle errors in constructing a query.
        print('There was an error in constructing your query : %s' % error)

    except HttpError as error:
        # Handle API errors.
        print('Arg, there was an API error : %s : %s' %
              (error.resp.status, error._get_reason()))


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

  Args:
    response: An Analytics Reporting API V4 response.
  """
    real_time_data_list = []

    if response.get('rows', []):
        for row in response.get('rows', []):
            i = 0
            object_in_real_time_data_list = {}

            for header in response.get('columnHeaders'):
                object_in_real_time_data_list[header.get('name')] = row[i]
                i = i + 1
            real_time_data_list.append(object_in_real_time_data_list)
            object_in_real_time_data_list = {}
    else:
        print('No Results Found')

    backup_json_data_list = read_data_from_backup_json_file(
        "Backup.json")  # Read data from Backup.json file and store in a List

    print("Backup List", len(backup_json_data_list), backup_json_data_list)  # Backup Data List

    print("RealTime   ", len(real_time_data_list), real_time_data_list)  # Realtime Json Data List

    updated_list = [x for x in real_time_data_list if x not in backup_json_data_list]

    for item in real_time_data_list:
        if item not in backup_json_data_list:
            backup_json_data_list.append(item)

    write_data_to_backup_json_file(backup_json_data_list)  # Update Backup.json file for next Run

    write_data_to_file(updated_list)

    del real_time_data_list
    del updated_list
    del backup_json_data_list
    gc.collect()
