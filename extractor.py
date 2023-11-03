import PySimpleGUI as sg
from functions import extract_archive

# GUI Theme
sg.theme("Dark2")

# Create labels and input elements for selecting file to extractor
select_file_label = sg.Text("Select Archive")
file_input = sg.Input()
file_browse_button = sg.FileBrowse("Browse", key="archive")

# Create labels and input elements for selecting the destination folder
select_destination_label = sg.Text("Select Destination folder:")
destination_input = sg.Input()
destination_browse_button = sg.FolderBrowse("Browse", key="folder")

# Create an "Extract" button for initiating the extraction process
extract_button = sg.Button("Extract")

# Create a Success message text field for successful extraction process
success_message = sg.Text(key="success", text_color="green")

# Create the main user interface window
layout = [[select_file_label, file_input, file_browse_button],
          [select_destination_label, destination_input, destination_browse_button],
          [extract_button, success_message]]
window = sg.Window("File Extractor",
                   layout=layout,
                   font=('Helvetica', 20))

# Wait for user interactions and collect user input from the GUI window
while True:
    event, values = window.read()

    match event:
        case 'Extract':
            filepath = values["archive"]
            folder_path = values["folder"]
            extract_archive(filepath, folder_path)
            window["success"].update(value="Extraction has been completed successfully!")
        case sg.WIN_CLOSED:
            break

# Close the GUI window after user interaction is complete
window.close()
