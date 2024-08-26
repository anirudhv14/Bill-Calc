import streamlit as st

# Title
st.title("Bill Splitter")

# Number of members
num_members = st.number_input("Enter the number of members:", min_value=0, value=0, step=1)
members = []
if(num_members >= 1):
    # Input for members
    st.header("Members Details")
    for i in range(num_members):
        member_name = st.text_input(f"Member {i+1} Name", "")
        members.append(member_name)


# Input for items
st.header("Bill Details")
num_items = st.number_input("Enter the number of items in the bill:", min_value=0, value=0, step=1)
items = []
if(num_items >= 1):
    for i in range(num_items):
        item_name = st.text_input(f"Item {i+1} Name", f"Item {i+1}")
        item_cost = st.number_input(f"Cost of {item_name}", min_value=0.0, step=0.01)
        items.append({"name": item_name, "cost": item_cost})

# Input for consumption per member
st.header("Consumption Details")
members_share = [0] * num_members  # Initialize the share for each member

for i, item in enumerate(items):
    st.subheader(f"Share of {item['name']}")
    total_percentage = 0
    for j,k in enumerate(members):
        percentage = st.number_input(f"Percentage of {item['name']} paid by Member {k}", min_value=0, max_value=100, value=100, step=1, key=f"{i}-{j}")
        members_share[j] += (percentage / 100) * item['cost']
        total_percentage += percentage
    
    if total_percentage != 100:
        st.warning(f"Total percentage for {item['name']} is not 100%! Current total is {total_percentage}%.")

# GST Amount
gst_amount = st.number_input("GST Amount (in %):", min_value=0, value=5, step=1)

# SC Amount
sc_amount = st.number_input("Service Charge Amount (in %):", min_value=0, value=0, step=1)

total_share_with_tax = [i + i * gst_amount/100 + i * sc_amount/100 for i in members_share]

# Display the results
st.header("Bill Split")
for i, share in enumerate(total_share_with_tax):
    st.write(f"{members[i]} should pay: ₹{share:.2f}")
st.write(f"Total = **₹{sum(total_share_with_tax)}**")

