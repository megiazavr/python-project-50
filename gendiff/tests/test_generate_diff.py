def generate_diff(file1, file2, format='stylish'):
    data1 = parser_file(file1)
    data2 = parser_file(file2)
    if data1 == 'Error' or data2 == 'Error':
        return print('Файла не существует')
    diff = build_diff(data1, data2)
    if format == 'stylish':
        return formater_stylish(diff)
    elif format == 'plain':
        return '\n'.join(formater_plain(diff))
    elif format == 'json':
        return formater_json(diff)
    else:
        raise ValueError('Unknown format!!!')

def main():
    file1, file2, format_ = parse_args()
    print(generate_diff(file1, file2, format_))

if __name__ == '__main__':
    main()


def test_generate_diff1():
    file1 = 'file1.json'
    file2 = 'file2.json'
    correct_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1, file2) == correct_result
