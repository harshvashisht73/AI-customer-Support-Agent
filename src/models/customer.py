

from pydantic import BaseModel, Field, EmailStr


class Customer(BaseModel):
    customer_id: str
    name: str
    email: EmailStr
    is_active: bool = True

if __name__ == "__main__":
    customer = Customer(
    customer_id="CUS1001",
    name="Rahul Sharma",
    email="rahul@example.com"
    )

    print(customer)
    print(customer.model_dump())
    print("Active:", customer.is_active)