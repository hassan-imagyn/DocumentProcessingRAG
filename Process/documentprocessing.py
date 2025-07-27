from Utility.azure_blob_utility import AzureBlobUtility
from Utility.tika_extractor import TikaExtractor
from Utility.chunking_utility import Chunker
from Utility.ai_search_utils import AzureAISearchHelper
from Utility.azuredocumentintelligence_utility import AzureDocumentInteliganceUtility
import os
class DocumentProcessor:
    def __init__(self):
        self.blob_helper = AzureBlobUtility()
        self.tika_processor = TikaExtractor(self.blob_helper)
        self.chunker = Chunker(500)
        self.search_helper = AzureAISearchHelper()
        self.azureDocInt = AzureDocumentInteliganceUtility()

    def process_document(self, filename):
        # Step 1: Read blob
        print("Read blob")
        file_bytes = self.blob_helper.download_blob_as_bytes(filename)

        # Step 2: Parse text with Tika
        #content = self.tika_processor.parse_from_bytes(file_bytes, filename)
        print("Parse text")
        content = self.azureDocInt.extract_text_from_bytes(file_bytes)
        if not content:
            raise Exception(f"No content extracted from file: {filename}")
        print("Chunk the content")
        # Step 3: Chunk the content
        chunks = self.chunker.chunk_text(content)
        
        print("Upload to AI Search")
        # Step 4: Upload to AI Search
        filepath = os.environ["Blob_baseUrl"]+"/"+os.environ["BLOB_CONTAINER_NAME"]+"/"+filename
        result = self.search_helper.upload_chunks(chunks,filepath,filename, "")

        return {"uploaded": len(chunks), "search_response": str(result)}
