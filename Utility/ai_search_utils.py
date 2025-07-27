from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import uuid
import os

class AzureAISearchHelper:
    def __init__(self):
        service_endpoint = os.environ["AI_SEARCH_ENDPOINT"]
        self.index_name = os.environ["AI_SEARCH_INDEX_NAME"]
        self.credential = AzureKeyCredential(os.environ["AI_SEARCH_ADMIN_KEY"])
        self.index_client = SearchIndexClient(endpoint=service_endpoint, credential=self.credential)
        self.search_client = SearchClient(service_endpoint,self.index_name,self.credential)

    def upload_chunks(self, chunks, filepath="", filename="", tags=""):
        """
        Uploads chunks as documents to the search index.
        Each chunk will be a separate document with shared metadata.
        """
        documents = []
        for i, chunk in enumerate(chunks):
            doc = {
                "id": str(uuid.uuid4()),
                "content": chunk,
                "filepath": filepath,
                "filename": filename,
                "tags": tags
            }
            documents.append(doc)

        result = self.search_client.upload_documents(documents)
        return result
    
    def search_documents(self, query: str, top: int = 5):
        """
        Performs a search query on the Azure AI Search index.
        Returns top matched documents.
        """
        print("inside processor: AI Search Hepler 39 : value of query:"+query)
        results = self.search_client.search(search_text = query, top=top)
        print(results)
        documents = []
        for result in results:
            doc = result.copy()  # result is a SearchResult; convert to dict
            documents.append(doc)
        
        return documents