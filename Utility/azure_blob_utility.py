from azure.storage.blob import BlobServiceClient
import os

class AzureBlobUtility:
    def __init__(self):
        blobconnectionstring = os.environ["BLOB_CONNECTION_STRING"]
        blobcontainername = os.environ["BLOB_CONTAINER_NAME"]
        self.blob_service = BlobServiceClient.from_connection_string(blobconnectionstring)
        self.container_name = blobcontainername

    def download_blob_to_tmp(self, blob_name: str) -> str:
        blob_client = self.blob_service.get_blob_client(container=self.container_name, blob=blob_name)
        local_path = f"/tmp/{blob_name}"

        with open(local_path, "wb") as file:
            file.write(blob_client.download_blob().readall())

        return local_path

    def download_blob_as_bytes(self, blob_name):
        print("blob name :"+ blob_name)
        print(self.blob_service)
        blob_client = self.blob_service.get_blob_client(container=self.container_name, blob=blob_name)
        return blob_client.download_blob().readall()