
from Process.documentprocessing import DocumentProcessor

class DocumentProcessService:
    def __init__(self):
        # Compose processor
        self.processor = DocumentProcessor()

    def documentprocess(self, filename):
        return self.processor.process_document(filename)
