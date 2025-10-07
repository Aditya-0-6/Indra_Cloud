 
from cloud_wrapper import CloudStorageWrapper

from cloud_config import (

    TEST_FILE_NAME,

    REMOTE_BLOB_PATH,

    DOWNLOADED_FILE_NAME

)

import os
 
def create_dummy_file(filename):

    """Utility function to create a temporary local file for testing."""

    with open(filename, "w") as f:

        f.write("This is a test line written by the cloud wrapper example.\n")

    print(f"\n--- Created test file: {filename} ---")
 
def cleanup_files(filenames):

    """Utility function to remove local files after testing."""

    print("\n--- Cleaning up local files... ---")

    for filename in filenames:

        try:

            os.remove(filename)

            print(f"Removed: {filename}")

        except FileNotFoundError:

            print(f"File not found during cleanup: {filename}")
 
if __name__ == "__main__":

    # 1. Setup the test environment

    create_dummy_file(TEST_FILE_NAME)
 
    # 2. Instantiate the wrapper

    storage_service = CloudStorageWrapper()
 
    # 3. Perform the Upload

    print("\n--- Testing Upload ---")

    upload_success = storage_service.upload_file(

        local_path=TEST_FILE_NAME,

        remote_path=REMOTE_BLOB_PATH

    )
 
    # 4. Perform the Download (only if upload succeeded)

    if upload_success:

        print("\n--- Testing Download ---")

        storage_service.download_file(

            remote_path=REMOTE_BLOB_PATH,

            local_path=DOWNLOADED_FILE_NAME

        )
 
    # 5. Verify downloaded content (optional)

    if os.path.exists(DOWNLOADED_FILE_NAME):

        print(f"\n--- Verification of Downloaded File ({DOWNLOADED_FILE_NAME}) ---")

        with open(DOWNLOADED_FILE_NAME, "r") as f:

            content = f.read().strip()

            print(f"Content: '{content}'")

    # 6. Cleanup

    cleanup_files([TEST_FILE_NAME, DOWNLOADED_FILE_NAME])

    print("\nExample finished.")
 
