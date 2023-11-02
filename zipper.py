import PySimpleGUI as sg

# Create labels and input elements for selecting files to compress
select_files_label = sg.Text("Select files to compress:")
files_input = sg.Input()
files_browse_button = sg.FilesBrowse("Browse")

# Create labels and input elements for selecting the destination folder
select_destination_label = sg.Text("Select destination folder:")
destination_input = sg.Input()
destination_browse_button = sg.FolderBrowse("Browse")

# Create a "Compress" button for initiating the compression process
compress_button = sg.Button("Compress")

# Create the main user interface window
window = sg.Window("File Compressor",
                   layout=[[select_files_label, files_input, files_browse_button],
                           [select_destination_label, destination_input, destination_browse_button],
                           [compress_button]],
                   font=('Helvetica', 20))

# Wait for user interactions and collect user input from the GUI window
user_input = window.read()

# Close the GUI window after user interaction is complete
window.close()
