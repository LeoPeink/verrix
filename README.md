# Verrix 4.0

## Overview

Verrix 4.0 is a Python script designed to process video files by removing silence from lectures recorded at UniTS (University of Trieste). The tool organizes and renames files based on their content, making them more accessible and efficient for users.

## Features

- **Silence Removal**: Automatically removes silent segments from video lectures.
- **File Organization**: Renames files based on the date extracted from their names and appends a unique hash for identification.
- **User Interaction**: Provides a menu-driven interface for selecting files to process and options for retrying or shutting down the computer after processing.

## Requirements

- Python 3.x
- `subprocess` module (included in Python standard library)
- `os` module (included in Python standard library)
- `time` module (included in Python standard library)
- `hashlib` module (included in Python standard library)
- An external tool named `unsilence` for processing audio.

## Installation

1. Clone the repository or download the script files `verrix_v4.py`[2] and `verrix_v4.bat`[1].
2. Ensure you have Python installed on your system.
3. Place your video files in the `raw/` directory.
4. Run the script using the command:

   ```bash
   python verrix_v4.py
   ```

## Usage

Upon running the script, you will be greeted with a menu that allows you to:

1. Choose whether to reprocess already processed files.
2. Decide if you want to shut down your computer after processing.
3. Select which files to render from the available list in the `raw/` directory.

Follow the prompts to complete your tasks.

## Directory Structure

- **raw/**: Place your original video files here.
- **unsorted/**: Processed video files will be saved here.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/24242220/d57aa4d5-bb23-4dab-91d2-3a56563510e9/verrix_v4.bat
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/24242220/0e7fe6d0-e925-4f2d-82ad-fe7f952f4460/verrix_v4.py
