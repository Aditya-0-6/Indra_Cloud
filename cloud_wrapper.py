from google.cloud import storage

from cloud_config import GCS_BUCKET_NAME

import os
 
class CloudStorageWrapper:
    """
    A simple wrapper class for Google Cloud Storage operations.
    It abstracts away the direct SDK calls for common tasks.
    """
 
    def __init__(self):
        """Initializes the GCS client and connects to the configured bucket."""
        try:
            self.client = storage.Client()
            self.bucket = self.client.bucket(GCS_BUCKET_NAME)
            print(f"Wrapper connected to bucket: {GCS_BUCKET_NAME}")
        except Exception as e:
            print(f"ERROR: Could not initialize GCS client or connect to bucket. {e}")
            self.bucket = None
 
 
    def upload_file(self, local_path: str, remote_path: str) -> bool:

        """Uploads a local file to the cloud bucket."""

        if not self.bucket or not os.path.exists(local_path):

            print("Upload failed: Invalid bucket or local file not found.")

            return False
 
        try:

            blob = self.bucket.blob(remote_path)

            blob.upload_from_filename(local_path)

            print(f"✅ Upload successful: '{local_path}' -> '{GCS_BUCKET_NAME}/{remote_path}'")

            return True

        except Exception as e:

            print(f"❌ Upload failed for {local_path}: {e}")

            return False
 
    def download_file(self, remote_path: str, local_path: str) -> bool:

        """Downloads a file (blob) from the cloud bucket to a local path."""

        if not self.bucket:

            print("Download failed: Invalid bucket connection.")

            return False

        try:

            blob = self.bucket.blob(remote_path)

            # This will fail if the file doesn't exist in the bucket

            blob.download_to_filename(local_path)

            print(f"✅ Download successful: '{GCS_BUCKET_NAME}/{remote_path}' -> '{local_path}'")

            return True

        except Exception as e:

            print(f"❌ Download failed for {remote_path}: {e}")

            return False
 
