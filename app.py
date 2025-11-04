import streamlit as st

st.set_page_config(page_title="Simple Shopping Home", page_icon="🛒", layout="centered")

st.title("🛒 Welcome to ShopEase")

st.markdown("""
Browse our featured products and add your favorites to the cart!
""")

# Example Products
products = [
    {"name": "Smartphone", "price": 12000, "desc": "Latest Android phone"},
    {"name": "Headphones", "price": 1500, "desc": "Wireless headphones"},
    {"name": "Fitness Band", "price": 2000, "desc": "Track your steps & health"},
    {"name": "Laptop", "price": 45000, "desc": "High performance laptop"},
]

st.header("Featured Products")
cart = []

for idx, prod in enumerate(products):
    col1, col2 = st.columns([5,1])
    with col1:
        st.subheader(prod["name"])
        st.write(prod["desc"])
        st.write(f"**₹{prod['price']}**")
    with col2:
        if st.button("Add to Cart", key=f"cart_{idx}"):
            cart.append(prod["name"])
            st.success(f"Added {prod['name']} to cart!")

st.write("---")
st.header("Your Cart")
if cart:
    st.write("You have added:")
    for item in cart:
        st.write(f"- {item}")
else:
    st.write("Your cart is empty.")

st.write("Made using Streamlit")
