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
    total_consumed_members = 0
    
    # Initialize a list for member checkboxes
    consumed = [False] * num_members

    # Checkboxes for each member to indicate if they consumed the item
    for j, member in enumerate(members):
        consumed[j] = st.checkbox(f"Did {member} consume {item['name']}?", key=f"consumed_{i}_{j}")

    # Calculate the total number of consumed members
    total_consumed_members = sum(consumed)

    # If there are consumed members, divide the cost equally among them
    if total_consumed_members > 0:
        item_share_per_member = item['cost'] / total_consumed_members
        for j, member in enumerate(members):
            if consumed[j]:
                members_share[j] += item_share_per_member

    # Warn if no one has consumed the item
    if total_consumed_members == 0:
        st.warning(f"No members have consumed {item['name']}.")

    # Display the per member share for each item
    st.write(f"Per member share for {item['name']} is {item_share_per_member:.2f}")

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

