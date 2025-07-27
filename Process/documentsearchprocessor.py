import os
from Utility.ai_search_utils import AzureAISearchHelper

class DocumentSearch:
    def __init__(self):
        self.search_helper = AzureAISearchHelper()

    def process_query(self, query: str):
        print("Im at line 9")
        results = self.search_helper.search_documents(query=query)
        print("Im at line 11")
        #print("Results;"+ results)
        if not results:
            return ["Empty"]

        parsed = []
        for doc in results:
            filename = doc.get("filename", "")
            content = doc.get("content", "")
            file_url = doc.get("filepath", "")

            parsed.append({
                "file_url": file_url,
                "content": content
            })

        return parsed
