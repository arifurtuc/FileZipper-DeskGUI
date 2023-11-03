import PySimpleGUI as sg
from functions import make_archive

# GUI Theme
sg.theme("Dark2")

# Create labels and input elements for selecting files to compress
select_files_label = sg.Text("Select files to compress:")
files_input = sg.Input()
files_browse_button = sg.FilesBrowse("Browse", key="files")

# Create labels and input elements for selecting the destination folder
select_destination_label = sg.Text("Select destination folder:")
destination_input = sg.Input()
destination_browse_button = sg.FolderBrowse("Browse", key="folder")

# Create a "Compress" button for initiating the compression process
compress_button = sg.Button("Compress")

# Create a Success message text field for successful compression process
success_message = sg.Text(key="success", text_color="green")

# Create the main user interface window
layout = [[select_files_label, files_input, files_browse_button],
          [select_destination_label, destination_input, destination_browse_button],
          [compress_button, success_message]]
window = sg.Window("File Compressor",
                   layout=layout,
                   font=('Helvetica', 20))

# Wait for user interactions and collect user input from the GUI window
while True:
    event, values = window.read()

    match event:
        case 'Compress':
            if values["files"] and values["folder"]:
                filepaths = values["files"].split(";")
                folder_path = values["folder"]
                make_archive(filepaths, folder_path)
                window["success"].update(value="Compression has been completed successfully!")
            elif not values["files"]:
                sg.popup("Select files first!",
                         font=("Helvetica", 20),
                         title="Selection Error")
            elif not values["folder"]:
                sg.popup("Select destination folder!",
                         font=("Helvetica", 20),
                         title="Selection Error")
        case sg.WIN_CLOSED:
            break

# Close the GUI window after user interaction is complete
window.close()
