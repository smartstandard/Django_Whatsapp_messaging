# views.py
from django.conf import settings
from twilio.rest import Client
from django.http import JsonResponse

def send_whatsapp_message(request):
    # Initialize Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # Define message details
    message_body = 'Your verification code is: 01234567'  # Customize your message
    recipient_number = 'whatsapp:+380970838174'  # Replace with the recipient's WhatsApp number

    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        to=recipient_number
    )

    return JsonResponse({'message_sid': message.sid, 'status': 'Message sent!'})