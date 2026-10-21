
# from pathlib import Path
# import json

# goki = Path(__file__).resolve()
# goku = Path(__file__).resolve().parents[2]
# # print("***")
# # print(Path(__file__).resolve().parents[2])
# # #print(Path(__file__).resolve().parents[3])

# # print("this is here: ",goku)
# # print()
# # print("this is here: ",goki)

# new_path = (goku / "data" / "mock_data" / "refunds.json")
# print("this is new path: ",new_path)

# with open(new_path, "r", encoding="utf-8") as file:
#     refunds = json.load(file)
# print("***")
# print(refunds)

# for refund in refunds: 
#     if refund.get("order_id") == order_id: 
#         return refund 

# return None

# from refund_status import get_refund_status
# # refund = get_refund_status("ORD1004")
# # print(refund["status"])
# from order_lookup import lookup_order
# res = lookup_order("ORD1004")
# print(res["status"])