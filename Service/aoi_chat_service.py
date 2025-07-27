from Process.aoi_chat_processor import AOIChatProcessor

class AOIChatService:
    def __init__(self):
        self.processor = AOIChatProcessor()

    def chat(self, query: str):
        return self.processor.process_user_input(query)
