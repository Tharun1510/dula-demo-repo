def process_customer_order(order_data, is_vip, stock_level, payment_status):
    # A monolithic, untested god-function
    if not order_data:
        return False
    else:
        if is_vip:
            if payment_status == "PAID":
                if stock_level > 0:
                    for item in order_data['items']:
                        if item['available']:
                            try:
                                # fake logic
                                print("Processing VIP")
                                if item['weight'] > 50:
                                    print("Heavy item processing")
                                else:
                                    print("Light item processing")
                            except Exception as e:
                                print(e)
                        else:
                            return "Item missing"
                else:
                    return "Out of stock"
            elif payment_status == "PENDING":
                return "Wait for payment"
        else:
            if payment_status == "PAID":
                for item in order_data['items']:
                    if stock_level > 0:
                        try:
                            print("Processing Normal")
                        except Exception as e:
                            print(e)
                    else:
                        break
            else:
                return "Unpaid normal user"
    return True
