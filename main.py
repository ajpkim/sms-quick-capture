from typing import List
from datetime import datetime

from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse, Message

app = FastAPI()

@app.post("/webhook")
async def webhook(From: str = Form(...), Body: str = Form(...)):
    msg = Body

    # Verify msg format
    try:
        msg_type, content, tags = get_msg_parts(msg)
    except Exception as e:
        return send_error_response()

    # Handle message types
    if msg_type == '1':
        general_handler(content, tags)
    elif msg_type == '2':
        try:
            expense_handler(content, tags)
        except Exception as e:
            return send_error_response()
    else:
        return send_error_response()

    # Send success message
    response = MessagingResponse()
    response.message("Got it :)")

    return Response(content=str(response), media_type="application/xml")

def send_error_response():
    response = MessagingResponse()
    response.message(f"Invalid message")
    return Response(content=str(response), media_type="application/xml")

def get_msg_parts(msg):
    """
    Split the msg into 3 parts:
    - msg type
    - content
    - tags
    """
    msg_type = msg[0]
    msg = msg[2:]

    if "\n#\n" in msg:
        content, tags = msg.split('\n#\n')
        tags = tags.split('\n')
    else:
        content = msg
        tags = []
    return [msg_type, content, tags]

def expense_handler(content: str, tags=List[str]):
    fields = ['amount', 'category', 'description']
    data = dict(zip(fields, content.split('\n')))
    data['tags'] = tags
    print("Expense msg Data:", data)

def general_handler(content: str, tags=List[str]):
    data = {
        "content": content,
        'tags': tags,
    }
    print("General msg Data:", data)
