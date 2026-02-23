def place_order(customer_name, main_item, price, quantity=1, *extra_items, discount_code="NONE", **metadata):
    """
    1. customer_name, main_item: Required Positional
    2. price: Required Positional (used for math)
    3. quantity: Default Argument
    4. *extra_items: Variable-length Positional (tuple)
    5. discount_code: Keyword-only/Default Argument
    6. **metadata: Variable-length Keyword (dictionary)
    """
    print(f"\n--- ORDER CONFIRMATION FOR: {customer_name.upper()} ---")
    print(f"Main Product: {main_item} (Qty: {quantity})")
    
    # Handling *args (Extra items)
    if extra_items:
        print(f"Add-ons: {', '.join(extra_items)}")
    else:
        print("Add-ons: None")

    # Handling **kwargs (Additional details)
    if metadata:
        print("Special Instructions:")
        for key, value in metadata.items():
            print(f"  - {key.replace('_', ' ').title()}: {value}")

    # Calculating Total
    subtotal = price * quantity
    # Simple logic for a specific discount code
    final_total = subtotal * 0.9 if discount_code == "SAVE10" else subtotal
    
    print("-" * 30)
    print(f"Discount Applied: {discount_code}")
    print(f"FINAL BILL AMOUNT: ₹{final_total:,.2f}")
    print("=" * 40)

# --- Calling the function using all argument types ---

place_order(
    "Alice Vance",            # Required
    "Gaming Laptop",          # Required
    1200.00,                  # Required (price)
    2,                        # Default override (quantity)
    "Mouse Pad", "Webcam",    # *args (Variable items)
    discount_code="SAVE10",   # Keyword argument
    delivery_type="Express",  # **kwargs (Extra metadata)
    gift_wrap=True            # **kwargs (Extra metadata)
)