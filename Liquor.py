import streamlit as st
import yagmail

# --- EMAIL FUNCTION ---
def send_email_notification(name, payment_method, delivery, total):
    # Your Gmail credentials
    sender_email = "tmalapane67@gmail.com"
    app_password = "erirnidtlthopofn"  # ← Use your Gmail app password

    yag = yagmail.SMTP(user=sender_email, password=app_password)
    message = f"""
    New Water Order Received:

    Name: {name}
    Payment Method: {payment_method}
    Delivery: {'Yes' if delivery else 'No'}
    Total Amount: R{total}
    """

    # Send to yourself
    yag.send(to=sender_email, subject="📦 New Water Order", contents=message)

# --- STREAMLIT UI ---
st.set_page_config(page_title="Purified Water Order", page_icon="💧", layout="centered")

st.title("💧 Order Purified Water – R10 per 5L")
st.markdown("**Support your health, stay hydrated!**")
st.markdown("---")

name = st.text_input("Enter your name:")
payment_method = st.selectbox("Select Payment Method:", ["Cash", "EFT (PayShap)"])
delivery = st.checkbox("Do you want delivery? (Add R5)")

# Cost calculation
base_price = 10
delivery_fee = 5 if delivery else 0
eft_fee = 2 if payment_method == "EFT (PayShap)" else 0
total_price = base_price + delivery_fee + eft_fee

st.markdown(f"### 🧾 Total Amount: **R{total_price}**")

if payment_method == "EFT (PayShap)":
    st.info(f"""
    Please send **R{total_price}** via **PayShap** to:

    **079 560 5334**  
    Bank: **TymeBank**  
    Use your **name** as reference.
    """)

if st.button("✅ Confirm & Send Order"):
    if name.strip() == "":
        st.error("Please enter your name before confirming.")
    else:
        send_email_notification(name, payment_method, delivery, total_price)
        st.success("Order submitted and email notification sent!")
        st.markdown(f"""
        📱 WhatsApp message to send:\n
        ```
        Name: {name}
        Payment: {payment_method}
        Delivery: {'Yes' if delivery else 'No'}
        Total: R{total_price}
        ```
        """)
