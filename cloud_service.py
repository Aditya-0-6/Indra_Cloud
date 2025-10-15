from google.api_core.exceptions import GoogleAPICallError

from cloud_connector import CloudConnector
from cloud_errors import FileOperationError, InitializationError

import os
 
class CloudStorageWrapper:

    """

    High-level wrapper for cloud storage operations.

    It utilizes the connector and custom exception handling.

    """
 
    def __init__(self):

        self.connector = None

        try:

            self.connector = CloudConnector()

        except InitializationError as e:

            print(f"Service initialization failed: {e}")

    def is_ready(self) -> bool:

        """Check if the underlying connector is successfully initialized."""

        return self.connector is not None and self.connector.bucket is not None
 
 
    def upload_file(self, local_path: str, remote_path: str) -> bool:

        """Uploads a local file to the cloud, handling errors gracefully."""

        if not self.is_ready():

            return False

        if not os.path.exists(local_path):

            print(f"Upload failed: Local file not found at '{local_path}'.")

            return False
 
        try:

            blob = self.connector.get_blob(remote_path)

            blob.upload_from_filename(local_path)

            print(f"✅ Upload successful: {local_path} -> {remote_path}")

            return True

        except GoogleAPICallError as e:

            raise FileOperationError("upload", remote_path, e)

        except Exception as e:

            raise FileOperationError("upload", remote_path, e)
 
 
    def download_file(self, remote_path: str, local_path: str) -> bool:

        """Downloads a file (blob) from the cloud to a local path."""

        if not self.is_ready():

            return False

        try:

            blob = self.connector.get_blob(remote_path)

            blob.download_to_filename(local_path)

            print(f"✅ Download successful: {remote_path} -> {local_path}")

            return True

        except GoogleAPICallError as e:

            raise FileOperationError("download", remote_path, e)

        except Exception as e:

            raise FileOperationError("download", remote_path, e)
 
