import os
import base64
from openai import AzureOpenAI

class AzureOpenAIUtility:
    def __init__(self):

        self.endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
        self.key = os.environ["AZURE_OPENAI_KEY"]
        self.deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
        self.search_endpoint = os.environ["AI_SEARCH_ENDPOINT"]
        self.search_key = os.environ["AI_SEARCH_ADMIN_KEY"]
        self.search_index = os.environ["AI_SEARCH_INDEX_NAME"]
        self.client = AzureOpenAI(azure_endpoint=self.endpoint, api_key=self.key, api_version="2025-01-01-preview",)

    def chat_with_ai_search(self, user_input: str):
        # Prepare the chat prompt
        chat_prompt = [
            {"role": "system","content": "You are an AI assistant that helps people find information."},
            {"role": "user","content": f"{user_input}"}
            ]

        # Include speech result if speech is enabled
        messages = chat_prompt

        # Generate the completion
        completion = self.client.chat.completions.create(
            model=self.deployment,
            messages=messages,
            max_tokens=6553,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False,
            extra_body={
            "data_sources": [{
            "type": "azure_search",
            "parameters": {
                "endpoint": f"{self.search_endpoint}",
                "index_name": f"{self.search_index}",
                "semantic_configuration": "default",
                "query_type": "simple",
                "fields_mapping": {
                "content_fields_separator": "\n",
                "content_fields": [
                    "content"
                ],
                "filepath_field": "filename",
                "title_field": "tags",
                "url_field": "filepath",
                "vector_fields": []
                },
                "in_scope": True,
                "filter": None,
                "strictness": 3,
                "top_n_documents": 5,
                "authentication": {
                    "type": "api_key",
                    "key": f"{self.search_key}"
                }
                }
            }]
        }
        )
    
    
        answer = completion.choices[0].message.content
        citations = completion.choices[0].message.context.get("citations", [])

        return {
            "answer": answer,
            "citations": citations
        }  
