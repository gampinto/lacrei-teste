from django.conf import settings
from django.http import JsonResponse

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key_header = request.headers.get("X-API-KEY")

        # Ele só vai permitir que a chave API seja inserida se existir e estiver correta.
        if api_key_header:
            if api_key_header == settings.SERVICE_API_KEY:
                request.is_internal_api = True
            else:
                return JsonResponse({"error": "API Key inválida"}, status=401)
        else:
            request.is_internal_api = False

        return self.get_response(request)
