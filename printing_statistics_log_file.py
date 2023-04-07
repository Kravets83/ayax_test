import re


def open_log_file(file_name: str) -> list:
    with open(file_name, 'r') as log_file:
        log_list = log_file.read().split("\n")
        return log_list


def get_data_handler_big(file_name: str) -> dict:
    handler_big_dict = dict()
    data_from_file = open_log_file(file_name)
    for sensor_data in data_from_file:
        if (re.search(r"'(.*?)'", sensor_data)) != None:
            sensor_data_list = (((re.search(r"'(.*?)'", sensor_data)).group())[1:-2].split(";"))
            if sensor_data_list[0] == "BIG":
                handler_big_dict[sensor_data_list[2]] = handler_big_dict.get(sensor_data_list[2], []) + [
                    sensor_data_list[-1]]
    return handler_big_dict


def printing_test_result(file_name: str):
    state_dict = get_data_handler_big(file_name)
    failed_tests_list = []
    complited_tests = []

    for i in state_dict.keys():
        failed_tests_list.append(f'Devise {i} was removed') if 'DD' in state_dict[i] else complited_tests.append(
            f'Devise {i} sent {len(state_dict[i])} statuses')
    print((f'Filed test {len(failed_tests_list)} devises').center(52, "-"))
    print(*failed_tests_list, sep="\n")
    print((f'Success test {len(complited_tests)} devises'.center(52, "-")))
    print(*complited_tests, sep="\n")


if __name__ == "__main__":
    printing_test_result('app_2 (1).log')
