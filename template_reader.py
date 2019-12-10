from string import Template


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        # print(template_file_content)
    return template_file_content

