import zipfile
import pathlib


def make_archive(filepaths, des_dir):
    """
    Create a ZIP archive from a list of file paths and save it to the specified destination directory.

    :param filepaths: A list of file paths to include in the ZIP archive.
    :param des_dir: The destination directory where the compressed ZIP file will be saved.
    """
    des_dir = pathlib.Path(des_dir, "compressed.zip")
    with zipfile.ZipFile(des_dir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
