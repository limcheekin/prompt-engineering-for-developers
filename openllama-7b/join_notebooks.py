import nbformat
import os

# giving directory name
dirname = '.'

# giving file extension
ext = ('ipynb')

notebooks = []

files = os.listdir(dirname)
files.sort()
# iterating over all files
for file in files:
    print("file", file)
    if file.endswith(ext):
        # Reading the notebooks
        print(file)
        notebooks.append(nbformat.read(file, 4))

# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=notebooks[0].metadata)

for notebook in notebooks:
    # Concatenating the notebooks
    final_notebook.cells += notebook.cells

# Saving the new notebook
nbformat.write(final_notebook, '0-combined.ipynb')
