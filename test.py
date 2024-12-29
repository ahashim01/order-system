import asyncio
import httpx
import random
import time

CLIENT = httpx.AsyncClient()

def generate_dynamic_data(num_stores, num_orders_per_store):
    data = {}
    order_id = 1
    
    for store_id in range(1, num_stores + 1):
        orders = []
        
        for _ in range(num_orders_per_store):
            customer_id = random.randint(1, 3)  
            product_sku = random.randint(1, 2)

            # 50% chance to create a duplicate order with the same order data
            if orders and random.random() > 0.5:
                duplicate_order = random.choice(orders)
                orders.append({
                    'order_id': duplicate_order['order_id'],
                    'customer_id': duplicate_order['customer_id'],
                    'product_sku': duplicate_order['product_sku'],
                    'event_status':'order.status.update'
                })
            else:
                orders.append({
                    'order_id': order_id,
                    'customer_id': customer_id,
                    'product_sku': product_sku,
                    'event_status':'order.created'

                })
            order_id += 1
        
        data[store_id] = {'orders': orders}
    
    return data

def create_dummy_json_for_salla(num_stores, num_orders_per_store) -> list:
    res = []
    data = generate_dynamic_data(num_stores, num_orders_per_store)
    for store_id, store_data in data.items():
        for order in store_data['orders']:
            order_id = order['order_id']
            customer_id = order['customer_id']
            event_status = order['event_status']
            product_sku = order['product_sku']
            order_json = {
                        "event_status": event_status,
                        "merchant": store_id,
                        "created_at": "Mon Apr 22 2024 11:57:16 GMT+0300",
                        "data":
                        {
                            "id": order_id,
                            "cart_reference_id": None,
                            "reference_id": order_id,
                            "urls":
                            {
                                "customer": "https://salla.sa/dev-8bdttknhfwt21yxn/order/7Gey9lbm4DoV143K4jkM5xK8ZrYREJjN",
                                "admin": "https://s.salla.sa/orders/order/7Gey9lbm4DoV143K4jkM5xK8ZrYREJjN"
                            },
                            "date":
                            {
                                "date": "2024-04-22 11:57:15.000000",
                                "timezone_type": 3,
                                "timezone": "Asia/Riyadh"
                            },
                            "updated_at":
                            {
                                "date": "2024-04-22 11:57:15.687605",
                                "timezone_type": 3,
                                "timezone": "Asia/Riyadh"
                            },
                            "source": "dashboard",
                            "source_device": "desktop",
                            "source_details":
                            {
                                "type": "dashboard",
                                "value": None,
                                "device": "desktop",
                                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                                "ip": None
                            },
                            "status":
                            {
                                "id": 566146469,
                                "name": "بإنتظار المراجعة",
                                "slug": "under_review",
                                "customized":
                                {
                                    "id": 1718648626,
                                    "name": "بإنتظار المراجعة"
                                }
                            },
                            "is_price_quote": False,
                            "payment_method": "mada",
                            "currency": "SAR",
                            "amounts":
                            {
                                "sub_total":
                                {
                                    "amount": 5,
                                    "currency": "SAR"
                                },
                                "shipping_cost":
                                {
                                    "amount": 0,
                                    "currency": "SAR"
                                },
                                "cash_on_delivery":
                                {
                                    "amount": 0,
                                    "currency": "SAR"
                                },
                                "tax":
                                {
                                    "percent": "0.00",
                                    "amount":
                                    {
                                        "amount": 0,
                                        "currency": "SAR"
                                    }
                                },
                                "discounts": [],
                                "total":
                                {
                                    "amount": 5,
                                    "currency": "SAR"
                                }
                            },
                            "can_cancel": False,
                            "show_weight": False,
                            "can_reorder": False,
                            "is_pending_payment": False,
                            "pending_payment_ends_at": 172799,
                            "total_weight": None,
                            "rating_link": None,
                            "shipping": None,
                            "shipments": None,
                            "shipment_branch": [],
                            "customer":
                            {
                                "id": customer_id,
                                "first_name": "Ammar",
                                "last_name": "Alzahrani",
                                "mobile": 562601855,
                                "mobile_code": "+966",
                                "email": "ammarjmhor10@gmail.com",
                                "urls":
                                {
                                    "customer": "https://salla.sa/dev-8bdttknhfwt21yxn/profile",
                                    "admin": "https://s.salla.sa/customers/BR274XKlNyP9waGk88naGzELkVx6bQrj"
                                },
                                "avatar": "https://cdn.assets.salla.network/prod/admin/cp/assets/images/avatar_male.png",
                                "gender": "male",
                                "birthday": None,
                                "city": "جدة",
                                "country": "السعودية",
                                "country_code": "SA",
                                "currency": "AED",
                                "location": "",
                                "updated_at":
                                {
                                    "date": "2024-04-19 21:33:23.000000",
                                    "timezone_type": 3,
                                    "timezone": "Asia/Riyadh"
                                },
                                "groups": []
                            },
                            "items": [
                            {
                                "id": 507504912,
                                "name": "telegram",
                                "sku": product_sku,
                                "quantity": 1,
                                "currency": "SAR",
                                "weight": 0,
                                "weight_label": None,
                                "amounts":
                                {
                                    "price_without_tax":
                                    {
                                        "amount": 5,
                                        "currency": "SAR"
                                    },
                                    "total_discount":
                                    {
                                        "amount": 0,
                                        "currency": "SAR"
                                    },
                                    "tax":
                                    {
                                        "percent": "0.00",
                                        "amount":
                                        {
                                            "amount": 0,
                                            "currency": "SAR"
                                        }
                                    },
                                    "total":
                                    {
                                        "amount": 5,
                                        "currency": "SAR"
                                    }
                                },
                                "notes": "",
                                "product":
                                {
                                    "id": 1488099704,
                                    "type": "digital",
                                    "promotion":
                                    {
                                        "title": None,
                                        "sub_title": None
                                    },
                                    "quantity": None,
                                    "status": "hidden",
                                    "is_available": False,
                                    "sku": "",
                                    "name": "telegram",
                                    "price":
                                    {
                                        "amount": 5,
                                        "currency": "SAR"
                                    },
                                    "sale_price":
                                    {
                                        "amount": 0,
                                        "currency": "SAR"
                                    },
                                    "currency": "SAR",
                                    "url": "https://salla.sa/dev-8bdttknhfwt21yxn/telegram/p1488099704",
                                    "thumbnail": "",
                                    "has_special_price": False,
                                    "regular_price":
                                    {
                                        "amount": 5,
                                        "currency": "SAR"
                                    },
                                    "calories": None,
                                    "mpn": "",
                                    "gtin": "",
                                    "description": "",
                                    "favorite": None,
                                    "features":
                                    {
                                        "availability_notify": None,
                                        "show_rating": True
                                    }
                                },
                                "options": [],
                                "images": [],
                                "codes": [],
                                "files": [],
                                "reservations": None,
                                "product_reservations": []
                            }],
                            "bank": None,
                            "tags": [],
                            "store":
                            {
                                "id": 1178631873,
                                "store_id": 1178631873,
                                "user_id": 1963520092,
                                "user_email": "8bdttknhfwt21yxn@email.partners",
                                "username": "dev-8bdttknhfwt21yxn",
                                "name":
                                {
                                    "ar": "متجر تجريبي",
                                    "en": None
                                },
                                "avatar": "https://salla-dev.s3.eu-central-1.amazonaws.com/logo/logo-fashion.jpg"
                            }
                        }
                    }
            res.append(order_json)

    return res

def create_dummy_json_for_zid(num_stores, num_orders_per_store) -> list:
    
    res = []
    data = generate_dynamic_data(num_stores, num_orders_per_store)
    for store_id, store_data in data.items():
        for order in store_data['orders']:
            order_id = order['order_id']
            customer_id = order['customer_id']
            event_status = order['event_status']
            product_sku = order['product_sku']
            order_json = {
                'event_status': event_status,
                "id": order_id,
                "code": order_id,
                "tags": [],
                "coupon": {
                    "id": 395523,
                    "code": "H99",
                    "name": "ام محمد",
                    "discount": "-21.7391",
                    "discount_string": "-21.74 SAR"
                },
                "source": "تطبيق المتجر",
                "weight": 0,
                "payment": {
                    "method": {
                    "code": "zidpay",
                    "name": "بطاقة إئتمانية",
                    "type": "cc",
                    "cart_payment_request_token": None
                    },
                    "invoice": [
                    {
                        "code": "sub_totals_before_vat",
                        "title": "المجموع غير شامل الضريبة",
                        "value": "217.39130434783000",
                        "value_string": "217.39 SAR"
                    },
                    {
                        "code": "coupon",
                        "title": "قسيمة التخفيض",
                        "value": "-21.73913043478300",
                        "value_string": "-21.74 SAR"
                    },
                    {
                        "code": "sub_totals_after_coupon_discount",
                        "title": "قيمة المنتجات بعد التخفيض",
                        "value": "195.65217391304000",
                        "value_string": "195.65 SAR"
                    },
                    {
                        "code": "taxable_amount",
                        "title": "المبلغ الخاضع للضريبة",
                        "value": "195.65217391304000",
                        "value_string": "195.65 SAR"
                    },
                    {
                        "code": "vat",
                        "title": "ضريبة القيمة المضافة (15%)",
                        "value": "29.34782608695700",
                        "value_string": "29.35 SAR"
                    },
                    {
                        "code": "sub_totals_after_vat",
                        "title": "مجموع المنتجات شامل ضريبة القيمة المضافة",
                        "value": "225.00000000000000",
                        "value_string": "225.00 SAR"
                    },
                    {
                        "code": "total",
                        "title": "المجموع الكلي",
                        "value": "225.00000000000000",
                        "value_string": "225.00 SAR"
                    }
                    ]
                },
                "currency": {
                    "order_currency": {
                    "id": 4,
                    "code": "SAR",
                    "exchange_rate": 1
                    },
                    "order_store_currency": {
                    "id": 4,
                    "code": "SAR",
                    "exchange_rate": None
                    }
                },
                "customer": {
                    "id": customer_id,
                    "name": "Alanoud aqab alashammari",
                    "note": "",
                    "type": "individual",
                    "email": "",
                    "mobile": "97455055560",
                    "verified": 1
                },
                "language": "ar",
                "products": [
                    {
                    "id": "73258621-2e34-43a7-b678-187db3f4ea34",
                    "sku": product_sku,
                    "meta": None,
                    "name": "500 علبة ماء 330 مل",
                    "price": 250,
                    "total": 250,
                    "images": [
                        {
                        "id": "df706bc2-6aa3-4dd0-811d-0c37e01bb75e",
                        "origin": "https://media.zid.store/thumbs/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e-thumbnail-500x500.png",
                        "thumbs": {
                            "large": "https://media.zid.store/thumbs/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e-thumbnail-1000x1000.png",
                            "small": "https://media.zid.store/thumbs/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e-thumbnail-500x500.png",
                            "medium": "https://media.zid.store/thumbs/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e-thumbnail-770x770.png",
                            "fullSize": "https://media.zid.store/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e.png",
                            "thumbnail": "https://media.zid.store/thumbs/16a6d508-7fbe-4546-ad35-14c3556f254d/df706bc2-6aa3-4dd0-811d-0c37e01bb75e-thumbnail-370x370.png"
                        }
                        }
                    ],
                    "weight": None,
                    "options": [],
                    "quantity": 1,
                    "vouchers": None,
                    "net_price": 217.39130434783,
                    "parent_id": None,
                    "is_taxable": True,
                    "tax_amount": "32.60869565217400",
                    "gross_price": 250,
                    "parent_name": None,
                    "price_before": None,
                    "price_string": "250.00 SAR",
                    "total_before": None,
                    "total_string": "250.00 SAR",
                    "custom_fields": [],
                    "is_discounted": False,
                    "product_class": None,
                    "net_sale_price": None,
                    "tax_percentage": 0.15,
                    "additions_price": 0,
                    "gross_sale_price": None,
                    "net_price_string": "217.39 SAR",
                    "short_description": {
                        "ar": "",
                        "en": ""
                    },
                    "tax_amount_string": "32.61 SAR",
                    "gross_price_string": "250.00 SAR",
                    "net_additions_price": 0,
                    "price_before_string": None,
                    "total_before_string": None,
                    "price_with_additions": 250,
                    "gross_additions_price": 0,
                    "net_sale_price_string": None,
                    "additions_price_string": "0.00 SAR",
                    "gross_sale_price_string": None,
                    "net_price_with_additions": 217.39130434783,
                    "net_additions_price_string": None,
                    "tax_amount_string_per_item": "32.60 SAR",
                    "price_with_additions_string": "250.00 SAR",
                    "gross_additions_price_string": None,
                    "net_price_with_additions_string": "217.39 SAR"
                    }
                ],
                "shipping": {
                    "method": {
                    "id": None,
                    "code": None,
                    "icon": "https://media.zid.store/static/delivery.png",
                    "name": "لا يتطلب شحن",
                    "courier": None,
                    "waybill": None,
                    "tracking": {
                        "url": None,
                        "number": None,
                        "status": None
                    },
                    "return_shipment": None,
                    "is_system_option": False,
                    "waybill_tracking_id": None,
                    "estimated_delivery_time": None,
                    "has_waybill_and_packing_list": False,
                    "had_errors_while_fetching_waybill": False
                    },
                    "address": {
                    "lat": None,
                    "lng": None,
                    "city": {
                        "id": 1495,
                        "name": "NA"
                    },
                    "meta": None,
                    "street": "NA",
                    "country": {
                        "id": 184,
                        "name": "NA"
                    },
                    "district": "NA",
                    "short_address": None,
                    "formatted_address": "NA"
                    }
                },
                "store_id": store_id,
                "histories": [
                    {
                    "comment": "تم تغيير حالة الطلب إلى \"تم التوصيل\"",
                    "created_at": "2024-04-11 01:03:51",
                    "changed_by_id": 231688,
                    "changed_by_type": "تاجر",
                    "order_status_id": 5,
                    "order_status_name": "تم التوصيل",
                    "changed_by_details": {
                        "by": "مشروع سقيا",
                        "action": "تم تغيير حالة الطلب إلى \"تم التوصيل\"",
                        "comment": "تغيير جماعي لحالة الطلب ."
                    },
                    "humanized_created_at": "منذ 3 ثواني"
                    },
                    {
                    "comment": "تم تغيير حالة الطلب إلى \"جاري التجهيز\"",
                    "created_at": "2024-04-08 21:26:58",
                    "changed_by_id": 447711,
                    "changed_by_type": "تاجر",
                    "order_status_id": 2,
                    "order_status_name": "جاري التجهيز",
                    "changed_by_details": {
                        "by": "عبد الله حمامي",
                        "action": "تم تغيير حالة الطلب إلى \"جاري التجهيز\"",
                        "comment": "تغيير جماعي لحالة الطلب ."
                    },
                    "humanized_created_at": "منذ يومين"
                    },
                    {
                    "comment": "تم ارسال فاتورة الطلب",
                    "created_at": "2024-04-08 18:05:35",
                    "changed_by_id": 8114623,
                    "changed_by_type": "عميل",
                    "order_status_id": 1,
                    "order_status_name": "جديد",
                    "changed_by_details": {
                        "by": "Alanoud aqab alashammari",
                        "action": "تم ارسال فاتورة الطلب",
                        "comment": ""
                    },
                    "humanized_created_at": "منذ يومين"
                    },
                    {
                    "comment": "تم إنشاء الطلب .",
                    "created_at": "2024-04-08 18:05:33",
                    "changed_by_id": 8114623,
                    "changed_by_type": "عميل",
                    "order_status_id": 1,
                    "order_status_name": "جديد",
                    "changed_by_details": {
                        "by": "Alanoud aqab alashammari",
                        "action": "تم إنشاء الطلب .",
                        "comment": ""
                    },
                    "humanized_created_at": "منذ يومين"
                    }
                ],
                "order_url": "https://example.com/o/uCExgVrIDx/inv",
                "store_url": "https://example.com/",
                "created_at": "2024-04-08 18:05:33",
                "issue_date": "08-04-2024 | 09:05 م",
                "store_name": "مشروع سقيا",
                "updated_at": "2024-04-11 01:03:51",
                "order_total": "225.00000000000000",
                "source_code": "mobile_app",
                "gift_message": None,
                "order_status": {
                    "code": "delivered",
                    "name": "تم التوصيل"
                },
                "payment_link": None,
                "cod_confirmed": False,
                "currency_code": "SAR",
                "customer_note": "",
                "is_gift_order": 0,
                "reseller_meta": None,
                "return_policy": None,
                "is_reactivated": False,
                "packages_count": 1,
                "payment_status": "paid",
                "products_count": 1,
                "gift_card_details": None,
                "inventory_address": None,
                "is_guest_customer": 0,
                "requires_shipping": False,
                "order_total_string": "225.00 SAR",
                "transaction_amount": 225,
                "weight_cost_details": [],
                "shipping_method_code": None,
                "transaction_reference": "4843ff56-7dc0-406f-b067-35ba9061e3bd",
                "zidship_ticket_number": None,
                "has_different_consignee": None,
                "is_quick_checkout_order": False,
                "is_reseller_transaction": False,
                "products_sum_total_string": "250.00 SAR",
                "transaction_amount_string": "225.00 SAR",
                "reverse_order_label_request": None,
                "has_different_transaction_currency": False
            }
            res.append(order_json)

    return res

async def send_request(store_type_name, json_data):
    try:
        if random.random() > 0.9:
            await asyncio.sleep(random.uniform(0.1, 0.1))
        r = await CLIENT.post(f'http://localhost:8000/webhooks/{store_type_name}/', json=json_data, timeout=10)
    except httpx.RequestError as exc:
        return False
    return r.is_success

async def send_webhook_request(num_stores, num_orders_per_store) -> None:
    jsons = {
        'salla': create_dummy_json_for_salla(num_stores, num_orders_per_store),
        'zid': create_dummy_json_for_zid(num_stores, num_orders_per_store)
    }
    zid_requests = [send_request('zid', json_data) for json_data in jsons['zid']]
    salla_requests = [send_request('salla', json_data) for json_data in jsons['salla']]
    results = await asyncio.gather(*zid_requests, *salla_requests)
    if all(results):
        print('ALL REQURESTS PASSED')
        return True
    print('SOME OR ALL REQURESTS FAILED')
    return False

async def main():
    loads = {
        'USUAL': {
            'num_stores': 7,
            'num_orders_per_store': 3,
        },
        'LOW': {
            'num_stores': 1,
            'num_orders_per_store': 1,
        }
    }
    print('-' * 50)
    for load, data in loads.items():
        print(f'LOAD: {load}')
        r = await send_webhook_request(**data)
        print(f'PASSED: {r}')
        print('-' * 50)
        time.sleep(3)
    return 'DONE'

asyncio.run(
    main()
)