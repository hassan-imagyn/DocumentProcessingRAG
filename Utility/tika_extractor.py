from tika import parser
from Utility.azure_blob_utility import AzureBlobUtility
import tempfile
class TikaExtractor:
    def __init__(self, blob_utility: AzureBlobUtility):
        self.blob_utility = blob_utility

    def extract_text_from_blob(self, blob_name: str) -> str:
        local_path = self.blob_utility.download_blob_to_tmp(blob_name)
        parsed = parser.from_file(local_path)
        return parsed.get("content", "").strip()

    def parse_from_bytes(self, file_bytes, filename="tempfile"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{filename}") as temp:
            temp.write(file_bytes)
            temp.flush()
            parsed = parser.from_file(temp.name)
        return parsed.get("content", "").strip()