from datetime import datetime as dt
import json


def write_data_to_file(mylist):
    if len(mylist) > 0:
        with open('data.json', 'w', encoding='utf-8') as f:
            for item in mylist:
                f.write('{')
                counter = 0
                for key, value in item.items():

                    if counter == 0:
                        if key == 'rt:pageTitle' or key == 'rt:source' or key == 'rt:trafficType' or key == 'rt:country' or key == 'rt:userType':
                            f.write('"' + str(key) + '"' + ':' + '"' + str(value) + '"')
                        else:
                            f.write('"' + str(key) + '"' + ':' + value)
                    elif counter != 0:
                        if key == 'rt:pageTitle' or key == 'rt:source' or key == 'rt:trafficType' or key == 'rt:country' or key == 'rt:userType':
                            f.write(',"' + str(key) + '"' + ':' + '"' + str(value) + '"')
                        else:
                            f.write(',"' + str(key) + '"' + ':' + value)
                    counter = counter + 1
                f.write('},\n')
            f.close()
    else:
        print("File is EMPTY")
        with open('data.json', 'w', encoding='utf-8') as f:
            f.close()


def list_for_selected_time_period(final_data_list, filtered_data_list, minute_value):
    current_hour = int(dt.now().hour)
    current_minute = int(dt.now().minute)

    if (current_minute - minute_value) >= 0:
        for item in final_data_list:
            if int(item['ga:hour']) == current_hour:
                if int(item['ga:minute']) >= (current_minute - minute_value):
                    filtered_data_list.append(item)
    elif (current_minute - minute_value) < 0:
        for item in final_data_list:
            if int(item['ga:hour']) == current_hour - 1:
                if int(item['ga:minute']) >= 60 - (minute_value - current_minute):
                    filtered_data_list.append(item)

    if current_minute - minute_value >= 0:
        print("GA Data From Past", minute_value, "Mins :  ", item['ga:date'], " [", current_hour, ":",
              current_minute - minute_value,
              " - ", current_hour, ":", current_minute, "]")
    else:
        print("GA Data From Past", minute_value, "Mins :  ", item['ga:date'], " [", current_hour - 1, ":",
              60 - (minute_value - current_minute), " - ", current_hour, ":", current_minute, "]")

    return filtered_data_list


def write_data_to_backup_json_file(mylist):
    if len(mylist) > 0:
        with open('Backup.json', 'w', encoding='utf-8') as f:
            json.dump(mylist, f)
            f.close()
    else:
        print("List is Empty")
        with open('data.json', 'w', encoding='utf-8') as f:
            f.close()


def read_data_from_backup_json_file(filename):
    with open(filename, 'r') as fp:
        line = fp.readline()
        a = json.loads(line)
        fp.close()
    return a
