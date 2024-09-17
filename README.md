# Verrix 4.0

## Overview

Verrix 4.0 is a Python script designed to process video files by removing silence from lectures recorded at UniTS (University of Trieste). The tool organizes and renames files based on their content, making them more accessible and efficient for users. It is very badly written in very little time, so lower your expectations. You can easily modify it, there are less than 90 lines of code.
## Features

- **Silence Removal**: Automatically removes silent segments from video lectures.
- **File Organization**: Renames files based on the date extracted from their names and appends a unique hash for identification.  It (dumbly) tries to rename the file formatting it as "YYYY-MM-DD_ (unique ID)". This has worked for my organization's original naming scheme, but it is untested with weird names. Year is also kinda-hardcoded.
- **User Interaction**: Provides a menu-driven interface for selecting files to process and options for retrying or shutting down the computer after processing.

## Requirements

- Python 3.x
- `subprocess` module (included in Python standard library)
- `os` module (included in Python standard library)
- `time` module (included in Python standard library)
- `hashlib` module (included in Python standard library)
- An external tool named [unsilence](https://github.com/miranhpark/unsilence) for processing audio.
- (optional) [sharedown](https://github.com/kylon/Sharedown) for downloading the videos from MS Sharepoint

## Installation

1. Clone the repository or download the script files `verrix_v4.py` and `verrix_v4.bat`.
2. Ensure you have Python installed on your system.
3. Ensure you installed all the requirements
4. Create a directory named `raw/` in the same folder you cloned the two verrix files in
5. Place your video files in the `raw/` directory.
6. Run the script from the CMD using the command:

   ```bash
   python verrix_v4.py
   ```
OR run it by double-clicking the .bat file.

## Usage

Upon running the script, you will be greeted with a menu that allows you to:

1. Choose whether to reprocess already processed files.
3. Decide if you want to shut down your computer after processing.
4. Select which files to render from the available list in the `raw/` directory.

Follow the prompts to complete your tasks.

## Directory Structure

- **raw/**: Place your original video files here.
- **unsorted/**: Processed video files will be saved here.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or new features.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/24242220/d57aa4d5-bb23-4dab-91d2-3a56563510e9/verrix_v4.bat
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/24242220/0e7fe6d0-e925-4f2d-82ad-fe7f952f4460/verrix_v4.py
[3] https://github.com/miranhpark/unsilence
