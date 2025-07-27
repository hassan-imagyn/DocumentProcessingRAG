import azure.functions as func
import logging
from Service.documentprocessing_service import DocumentProcessService
from Service.documentsearchprocessor_service import DocumentSearchProcessorService
from Service.aoi_chat_service import AOIChatService
import json
import os
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.function_name(name="process_document")
@app.route(route="process-doc", methods=["GET"])
def process_doc(req: func.HttpRequest) -> func.HttpResponse:
    filename = req.params.get("filename")
    if not filename:
        return func.HttpResponse("Missing filename", status_code=400)

    try:
        service = DocumentProcessService()
        result = service.documentprocess(filename)
        return func.HttpResponse(json.dumps(result, indent=2), mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

@app.function_name(name="search_documents")
@app.route(route="search", methods=["GET"])
def search_documents(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get("q")
    if not query:
        return func.HttpResponse("Missing 'q' parameter", status_code=400)

    try:
        service = DocumentSearchProcessorService()
        results = service.search(query)
        return func.HttpResponse(json.dumps(results, indent=2), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
    

@app.function_name(name="aoi_chat")
@app.route(route="aoi-chat", methods=["GET"])
def aoi_chat(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get("q")
    if not query:
        return func.HttpResponse("Missing 'q' parameter", status_code=400)

    try:
        service = AOIChatService()
        results = service.chat(query)
        return func.HttpResponse(json.dumps(results, indent=2), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
