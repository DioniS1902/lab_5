import re

regex = r'(.*?) - - \[(\d{2}\/\D{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) -\d+\] "(.*?)" (\d+) (\d+)'


def search_data(data_string: str):
    data = re.match(regex, data_string)
    if data:
        if 'GET' in data[4] and data[5] == '200':
            time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(data[3].split(':'))))
            start_time, end_time = 35 * 60, 1 * 60 ** 2 + 12 * 60
            return int(data[6]) if data[2] == '01/Jul/1995' and start_time <= time <= end_time else 0
    return None


if __name__ == '__main__':
    with open('access_log_Jul95', 'r') as file:
        all_bytes = [search_data(i) for i in file.readlines() if search_data(i)]
        print(f"Кількість успішних GET запитів {len(all_bytes)}, сумарна кількість байт {sum(all_bytes)}")
