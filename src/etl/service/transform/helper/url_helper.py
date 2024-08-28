from urllib.parse import unquote

def decode_url(encoded_url):
    decoded_url = unquote(encoded_url)
    decoded_url = decoded_url.replace("&amp;", "&")
    
    if not decoded_url.startswith(('http://', 'https://')):
        decoded_url = f"https://{decoded_url}"
    
    return decoded_url

