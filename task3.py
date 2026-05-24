import os

files_data = []

for filename in os.listdir('exercise3'):
    if filename.endswith('.txt'):
        path = f'exercise3/{filename}'
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_info = {
                'filename': filename,
                'lines_count': len(lines),
                'content': lines
            }
            files_data.append(file_info)

files_data.sort(key=lambda x: x['lines_count'])

with open('result_file.txt', 'w', encoding='utf-8') as f:
   for file_data in files_data:
       f.write(file_data['filename'] + '\n')
       f.write(str(file_data['lines_count'])+ '\n')
       for line in file_data['content']:
           f.write(line)
       f.write('\n')
