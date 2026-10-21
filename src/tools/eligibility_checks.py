
from src.tools.refund_status import get_refund_status
from src.tools.order_lookup import lookup_order



def check_cancellation_eligibility(order_id: str) -> dict:
    """Check whether an order can be requested for cancellation."""

    order = lookup_order(order_id)

    if order is None:
        return {
            "order_id": order_id,
            "eligible": False,
            "message": "Order not found."
        }

    status = order.get("status")

    if status == "processing":
        return {
            "order_id": order_id,
            "eligible": True,
            "message": (
                "The order is processing. "
                "A cancellation request can be submitted, "
                "but approval is not guaranteed."
            )
        }

    if status == "shipped":
        return {
            "order_id": order_id,
            "eligible": False,
            "message": (
                "The order has shipped and normally cannot "
                "be cancelled. A return may be requested "
                "after delivery, subject to the return policy."
            )
        }

    if status == "delivered":
        return {
            "order_id": order_id,
            "eligible": False,
            "message": (
                "Delivered orders cannot be cancelled. "
                "A return may be requested subject to the "
                "return policy."
            )
        }

    if status == "cancelled":
        return {
            "order_id": order_id,
            "eligible": False,
            "message": "The order is already cancelled."
        }

    return {
        "order_id": order_id,
        "eligible": False,
        "message": f"Unknown order status: {status}."
    }


def check_refund_eligibility(order_id: str) -> dict:
    """Check the available refund record for an order."""

    order = lookup_order(order_id)

    if order is None:
        return {
            "order_id": order_id,
            "eligible": False,
            "message": "Order not found."
        }

    refund = get_refund_status(order_id)

    if refund is None:
        return {
            "order_id": order_id,
            "eligible": False,
            "message": (
                "No refund record found. "
                "Further eligibility checks are required."
            )
        }

    refund_status = refund.get("status")

    if refund_status == "approved":
        return {
            "order_id": order_id,
            "eligible": True,
            "message": "The refund has been approved."
        }

    if refund_status == "processed":
        return {
            "order_id": order_id,
            "eligible": True,
            "message": "The refund has already been processed."
        }

    if refund_status == "pending":
        return {
            "order_id": order_id,
            "eligible": False,
            "message": "The refund is pending. Approval is not yet confirmed."
        }

    return {
        "order_id": order_id,
        "eligible": False,
        "message": f"Unknown refund status: {refund_status}."
    }
