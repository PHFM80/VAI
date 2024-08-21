# utils.py
import qrcode
import base64
from io import BytesIO

def generar_codigo_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    
    # Convertir la imagen a base64 para guardarla en el campo 'codigo_qr'
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str
