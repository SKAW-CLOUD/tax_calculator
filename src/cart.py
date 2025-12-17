def apply_discount(price, discount_percentage):
    """
    Applies a discount to a price.
    Example: apply_discount(100, 20) should return 80.0
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    # FIX: Calculate discount as a percentage of the price
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    
    if final_price < 0:
        return 0.0
    return float(final_price)

def calculate_tax(subtotal, tax_rate):
    """
    Calculates tax based on a decimal rate (e.g., 0.05 for 5%).
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    
    tax = subtotal * tax_rate
    return float(tax)
