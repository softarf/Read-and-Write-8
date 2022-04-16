
import os

def data_input(path):
    file_names = []
    full_text = []
    for entry in os.listdir(path):
        if entry.rfind('.txt') == 1:
            file_names.append(entry)
            entry_path = os.path.join('temp', entry)
            with open(entry_path, 'r', encoding='utf8') as in_file:
                word_lines = []
                word_lines = in_file.readlines()
                full_text.append(word_lines)
    return file_names, full_text

def my_sorted(full_text):
    len_files = []
    for entry in full_text:
        len_files.append(len(entry))
    files_sorted = sorted(enumerate(len_files), key=lambda x: x[1])
    return files_sorted

def data_output(file_names, full_text, files_sorted):
    crlf = ''
    with open('temp\\out_f.txt', 'wt', encoding='utf8') as out_file:
        for i in range(len(full_text)):
            print(crlf + file_names[files_sorted[i][0]], file=out_file, end='')
            if crlf == '': crlf = '\n'
            print(crlf + str(files_sorted[i][1]), file=out_file)
            for eny in full_text[files_sorted[i][0]]:
                print(eny, file=out_file, end='')
            print(file=out_file, end='')
    return files_sorted


#                                         Головной блок
#                  1. Считать файлы.
base = os.getcwd()
dir_name = 'temp'
files_path = os.path.join(base, dir_name)
files_list, text_list = data_input(files_path)

#                  2. Отсортировать по возростанию.
res_sort = my_sorted(text_list)
print(res_sort)    # Для теста.

#                  3. Вывод результата.
data_output(files_list, text_list, res_sort)
 

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
