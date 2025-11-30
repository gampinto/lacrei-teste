import unicodedata
import re

def sanitize_text(value: str) -> str:
    if not isinstance(value, str):
        return value

    # essa aqui bloqueia os espaços nas pontas
    value = value.strip()

    # bloqueia caracters invisíveis
    value = unicodedata.normalize("NFKC", value)

    # bloqueia uso de scripts
    value = re.sub(r"<script.*?>.*?</script>", "", value, flags=re.IGNORECASE)

    # limita o html
    value = re.sub(r"<.*?>", "", value)

    # limite de tamanho
    if len(value) > 255:
        value = value[:255]

    return value
