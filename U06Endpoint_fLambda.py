import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    bodyPost = json.loads(event["body"])

    payment_data = {
        "transaction_amount": float(bodyPost["transaction_amount"]),
        "token": bodyPost["token"],
        "installments": int(bodyPost["installments"]),
        "payment_method_id": bodyPost["payment_method_id"],
        "issuer_id": bodyPost["issuer_id"],
        "payer": {
            "email": bodyPost["payer"]["email"],
            "identification": {
                "type": bodyPost["payer"]["identification"]["type"], 
                "number": bodyPost["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]

    print(payment)
    
    resp = {
        "statusCode": 200,
        "body": json.dumps(payment),
    }

    return resp