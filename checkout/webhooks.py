from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe

@require_POST
@csrf_exempt
def webhook(request):
    webhook_secret = settings.WEBHOOK_SECRET_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    if sig_header is None:
        return HttpResponse("Missing Stripe Signature", status=400)

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=str(e), status=400)

    print(f"Received event: {event['type']}")

    # Here you can handle the event, e.g.:
    # handler = StripeWH_handler(request)
    # response = getattr(handler, f"handle_{event['type'].replace('.', '_')}", handler.handle_event)(event)

    return HttpResponse(status=200)
