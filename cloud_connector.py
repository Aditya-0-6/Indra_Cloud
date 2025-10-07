 from google.cloud import storage

from google.api_core.exceptions import GoogleAPICallError

from cloud_config import GCS_BUCKET_NAME

from cloud_errors import InitializationError
 
class CloudConnector:

    """Handles the low-level connection and object retrieval from GCS."""
 
    def __init__(self):

        """Connects to the GCS client and retrieves the bucket reference."""

        self.bucket = None

        try:

            client = storage.Client()

            self.bucket = client.bucket(GCS_BUCKET_NAME)

            # Optional: Check if bucket exists (can add an API call here for stricter check)

            print(f"Connector initialized and attached to bucket: {GCS_BUCKET_NAME}")

        except GoogleAPICallError as e:

            # Catch specific Google errors for configuration issues

            raise InitializationError(f"GCS API Error during init: {e}")

        except Exception as e:

            raise InitializationError(f"Unexpected error during GCS initialization: {e}")
 
    def get_blob(self, remote_path: str) -> storage.Blob:

        """Returns a reference to a GCS Blob object."""

        if not self.bucket:

            raise InitializationError("Connector is not fully initialized. Cannot get blob.")

        return self.bucket.blob(remote_path)
 
