from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Wine
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        payment_intent_id = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None


        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username!= 'AnnoymousUser':
            profile.default_profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = shipping_details.address.street_address1
                profile.default_street_address2 = shipping_details.address.street_address2
                profile.default_town_or_city = shipping_details.address.town
                profile.default_county = shipping_details.address.county
                profile.default_postal_code = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try: 
                order = Order.objects.get(
                    first_name__iexact=shipping_details.first_name,
                    last_name__iexact=shipping_details.last_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.street_address1,
                    street_address2__iexact=shipping_details.address.street_address2,
                    town_or_city__iexact=shipping_details.address.town,
                    county__iexact=shipping_details.address.county,
                    postal_code__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_payment_intent_id=payment_intent_id,
                )

                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.first_name,
                    last_name=shipping_details.last_name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number_name=shipping_details.phone,
                    street_addresst=shipping_details.address.street_address1,
                    street_address2=shipping_details.address.street_address2,
                    town_or_city=shipping_details.address.town,
                    county=shipping_details.address.county,
                    postal_code=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_bag=bag,
                    stripe_payment_intent_id=payment_intent_id,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Wine.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
