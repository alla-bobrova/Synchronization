import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import base64

# Путь к блокноту
notebook_path = 'name.ipynb'

# Папка для сохранения изображений
output_folder = 'res'

# Количество запусков блокнота
runs = 100

# Создаем объект ExecutePreprocessor
executor = ExecutePreprocessor(timeout=600, kernel_name='python3')

# Читаем блокнот
with open(notebook_path, 'r') as f:
    notebook = nbformat.read(f, as_version=4)

# Создаем папку для сохранения изображений, если ее еще нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Запускаем блокнот и сохраняем изображения
for run in range(runs):
    # Клонируем блокнот перед каждым запуском
    cloned_notebook = notebook.copy()

    # Запускаем каждую ячейку блокнота
    executor.preprocess(cloned_notebook)

    # Сохраняем изображения
    for cell in cloned_notebook.cells:
        if cell.cell_type == 'code':
            for output in cell.outputs:
                if 'data' in output and 'image/png' in output.data:
                    png_data = output.data['image/png']
                    # print(f"Image data: {png_data[:50]}...")  # Отладочный вывод
                    # Преобразуем строку в байтовый объект
                    png_data_bytes = base64.b64decode(png_data)
                    # Создаем уникальное имя для файла
                    output_file = f'image_{run}_{cloned_notebook.cells.index(cell)}.png'
                    output_path = os.path.join(output_folder, output_file)
                    # Сохраняем изображение
                    with open(output_path, 'wb') as f:
                        f.write(png_data_bytes)
                        # print(f"Image saved to: {output_path}")  # Отладочный вывод

print("All runs completed")
