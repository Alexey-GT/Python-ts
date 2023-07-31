import os


def group_rename_files(desired_name, number_digits, source_extension, final_extension, name_range=None):
    directory = '.'  # текущий каталог
    counter = 1  # счетчик для порядкового номера

    if name_range is not None and len(name_range) == 2:
        start, end = name_range
    else:
        start, end = 0, None

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            original_name = os.path.splitext(filename)[0]

            original_name = original_name[start:end]

            new_name = desired_name + str(counter).zfill(number_digits) + final_extension

            os.rename(filename, new_name)

            counter += 1


group_rename_files("new_file_", 3, ".txt", ".jpg", [3, 6])
