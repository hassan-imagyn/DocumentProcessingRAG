from Utility.azure_openai_utility import AzureOpenAIUtility

class AOIChatProcessor:
    def __init__(self):
        self.openai_helper = AzureOpenAIUtility()

    def process_user_input(self, user_input: str):
        result = self.openai_helper.chat_with_ai_search(user_input)

        citationslist = []
        for citation in result["citations"]:
            filename = citation.get("filepath", "")
            filepath = citation.get("url", "")
            if filename and filepath:
                citationslist.append({
                        "filename": filename,
                        "filepath": filepath
                    })

        return {
            "response": result["answer"],
            "citations": citationslist
        }
