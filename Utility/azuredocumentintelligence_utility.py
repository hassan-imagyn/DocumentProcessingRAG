import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

class AzureDocumentInteliganceUtility:
    def __init__(self):
        endpoint = os.environ["AZURE_DOC_INTEL_ENDPOINT"]
        key = os.environ["AZURE_DOC_INTEL_KEY"]
        self.client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    def extract_text_from_bytes(self, file_bytes: bytes):
        """
        Uses Azure Document Intelligence Read model to extract plain text from a file.
        """
        poller = self.client.begin_analyze_document(
            model_id="prebuilt-layout",  # or use 'prebuilt-layout' if you want layout info
            analyze_request = AnalyzeDocumentRequest(
                bytes_source=file_bytes
           )
        )

        result = poller.result()
        
        return result.content
