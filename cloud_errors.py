class CloudError(Exception):

    """Base exception for all custom cloud wrapper errors."""

    pass
 
class InitializationError(CloudError):

    """Raised when the cloud client or bucket cannot be initialized."""

    def __init__(self, message="Cloud client failed to initialize."):

        super().__init__(message)
 
class FileOperationError(CloudError):

    """Raised when an upload or download operation fails."""

    def __init__(self, operation: str, path: str, original_error: Exception):

        message = f"Failed to {operation} file at path '{path}'. Original Error: {original_error}"

        super().__init__(message)
