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


def extract_archive(filepath, des_dir):
    """
    Extract the contents of a ZIP archive to a specified destination directory.

    :param filepath: The path to the ZIP archive that needs to be extracted.
    :param des_dir: The destination directory where the contents will be extracted.
    """
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(des_dir)


