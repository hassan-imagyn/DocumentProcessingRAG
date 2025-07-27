from Process.documentsearchprocessor import DocumentSearch

class  DocumentSearchProcessorService:
    def __init__(self):
        self.processor = DocumentSearch()

    def search(self, query: str):
        return self.processor.process_query(query)