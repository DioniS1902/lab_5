import re

regex = r'.*? - - \[(\d{2}\/\D{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) -\d+\] "GET .*?" 200 (.+)'


def convert_time(time): return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))


def get_bytes(string_data):
    return int(string_data[3]) if string_data[1] == '01/Jul/1995' and \
                                  convert_time("00:35:00") <= convert_time(data[2]) <= convert_time("1:12:00") and string_data[3] != '-' else 0


if __name__ == '__main__':
    with open('access_log_Jul95', 'r') as file:
        successful, bytes_size = 0, 0
        for line in file.readlines():
            data = re.match(regex, line)
            if data: bytes_size, successful = bytes_size + get_bytes(data), successful + 1
        print(f"Кількість успішних GET запитів {successful}, сумарна кількість байт {bytes_size}")
