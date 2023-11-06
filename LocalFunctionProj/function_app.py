import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="AngAPIAzureflask")

@app.route(route="APIAng")
def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.route == 'hello':
        name = req.params.get('name', 'World')
        return func.HttpResponse(f'Hello {name}!')

    return func.HttpResponse("HttpExample function processed a request!")
