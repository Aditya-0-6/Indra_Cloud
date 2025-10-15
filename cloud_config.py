# cloud_config.py
# --- Configuration Settings ---
# IMPORTANT: Replace this with your actual Google Cloud Storage bucket name.
GCS_BUCKET_NAME = "your-unique-cloud-storage-bucket-name"

# The name of the local file to use for testing
TEST_FILE_NAME = "local_data_to_upload.txt"

# The desired name/path of the file once it's in the cloud bucket
REMOTE_BLOB_PATH = f"data_uploads/{TEST_FILE_NAME}"

# The name for the file after downloading it
DOWNLOADED_FILE_NAME = "downloaded_cloud_data.txt"

# --- Authentication Prerequisite ---
# Ensure you have installed the client library:
# pip install google-cloud-storage
#
# And authenticated your environment (e.g., via):
# gcloud auth application-default login
