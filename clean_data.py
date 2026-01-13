import re

# 1. THE "DIRTY" DATA (Like the 'Animal Nature' or 'Oily' feedback)
# Imagine this is scraped from a site like Glassdoor or a Supplier Review
raw_feedback = """
    SUPPLIER_ID: 10293 | RATING: 4.5 stars | COMMENT: Great service!!! :)
    SUPPLIER_ID: ERROR_99 | RATING: 1.2 | COMMENT: Very slow response time...
    SUPPLIER_ID: 55621 | RATING: 5.0 | COMMENT: Excellent quality!
"""

# 2. THE REGEX PATTERN (The 'Sutta Veli' - Filtering for Truth)
# We only want to extract the clean ID and the numeric Rating
# Pattern: Find 'SUPPLIER_ID: ' followed by digits, then get the rating digits
pattern = r"SUPPLIER_ID:\s+(\d+)\s+\|\s+RATING:\s+(\d+\.\d+)"

# 3. THE "INTERNAL CHURNING" (Processing)
clean_data = re.findall(pattern, raw_feedback)

print("--- CLEANED DATA FOR ARIBA INTEGRATION ---")
for supplier_id, rating in clean_data:
    # This simulates a 'JSON' Payload that Ariba Cloud would accept
    ariba_payload = {
        "SupplierID": supplier_id,
        "ExternalRating": float(rating),
        "Source": "External_Glassdoor_Sync"
    }
    print(f"Pushing to Cloud: {ariba_payload}")
