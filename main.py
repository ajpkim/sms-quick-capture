from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse, Message

app = FastAPI()

@app.post("/webhook")
async def msg_handler(From: str = Form(...), Body: str = Form(...)):

    print("\nReceived Message")
    print("From:", From)
    print("Body:", Body)
    print()

    response = MessagingResponse()
    print("Empty Response Obj:", response)

    m1 = Message()
    m1.body("FIRST MESSAGE")

    m2 = Message()
    m2.body("SECOND MESSAGE")

    response.append(m1)

    response.append(m2)

    print("The XML of the response:\n", response.to_xml())



    return Response(content=str(response), media_type="application/xml")



"""
Need funcs that process the body and look for the tags I want to use.
"""


def find_tags(msg):
    pass
