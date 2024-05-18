import os
import nbformat

# Directory containing your Jupyter notebooks
directory = '.'

# Function to add a cell to the beginning of a notebook
def add_cell_to_notebook(notebook_path, cell_content):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create a new cell with the specified content
    new_cell = nbformat.v4.new_markdown_cell(cell_content)
    
    # Add the new cell to the beginning of the notebook
    nb.cells.insert(0, new_cell)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.ipynb'):
        notebook_path = os.path.join(directory, filename)
        colab_link = f'https://colab.research.google.com/github/lukebarousse/Python_Data_Analytics_Course/blob/main/{filename}'
        badge = f'<a target="_blank" href="{colab_link}">\n  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>\n</a>'
        cell_content = f'{badge}'
        add_cell_to_notebook(notebook_path, cell_content)
        print(f'{notebook_path}: Added cell.')

print("FINISHED: Added cells to all notebooks.")
