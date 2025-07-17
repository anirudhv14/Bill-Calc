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

distribution_method = st.radio("Select the method of consumption distribution:", ("Equal", "Proportional"))

if distribution_method == "Proportional":
    st.info("Using Proportional distribution for all items.")
    # Proportional distribution logic goes here
    for i, item in enumerate(items):
        st.subheader(f"Share of {item['name']}")
        total_percentage = 0
        total_consumed_members = 0

        # Initialize a list for member checkboxes
        consumed = [False] * num_members

        # Checkboxes for each member to indicate if they consumed the item
        for j, member in enumerate(members):
        # Input for percentage share for each member \
            # if total_consumed_members == 0:
            percentage = st.number_input(f"Percentage share for {member} (0-100):", min_value=0, max_value=100, value=0, key=f"percentage_{i}_{j}")
            # consumed[j] = st.checkbox(f"Did {member} consume {item['name']}?", key=f"consumed_{i}_{j}")
            consumed[j] = True if (percentage > 0) else False
            total_percentage += percentage
            if percentage > 0:
                total_consumed_members += 1

        # Calculate the share for each member based on their percentage
        if total_consumed_members > 0:
            for j, member in enumerate(members):
                if consumed[j]:
                    members_share[j] += item['cost'] * (percentage / 100)
            # Display the per member share for each item
            st.write(f"Per member share for {item['name']} is {item['cost'] * (percentage / 100):.2f} for each member who consumed it.")
        # Warn if no one has consumed the item
        if total_consumed_members == 0:
            st.warning(f"No members have consumed {item['name']}.")
        # Check if total percentage exceeds 100%
        if total_percentage > 100:
            st.error("Total percentage exceeds 100%. Please adjust the percentages for each member.")
        elif total_percentage < 100:
            st.warning("Total percentage is less than 100%. Please ensure all percentages add up to 100% for proportional distribution.")
        else:
            st.success("Total percentage is valid.")

else:
    st.info("Using Equal distribution for all items.")

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
            
            # Display the per member share for each item
            st.write(f"Per member share for {item['name']} is {item_share_per_member:.2f}")

        # Warn if no one has consumed the item
        if total_consumed_members == 0:
            st.warning(f"No members have consumed {item['name']}.")

# GST Amount
gst_amount = st.number_input("GST Amount (in %):", min_value=0.0, value=5.0, step=0.01)

# SC Amount
sc_amount = st.number_input("Service Charge Amount (in %):", min_value=0.0, value=0.0, step=0.01)

total_share_with_tax = [i + i * gst_amount/100 + i * sc_amount/100 for i in members_share]

# Display the results
st.header("Bill Split")
for i, share in enumerate(total_share_with_tax):
    st.write(f"{members[i]} should pay: ₹{share:.2f}")
st.write(f"Total = **₹{sum(total_share_with_tax)}**")

