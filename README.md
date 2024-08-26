
# Bill Splitter

## Overview

**Bill Splitter** is a simple web application built using Streamlit, designed to help groups of people split their bill based on individual consumption. The app allows users to enter the number of members, items, and the percentage of each item consumed by each member. Additionally, the app also allows users to include GST and Service Charges to accurately calculate each member's share.

## Features

- **User-Friendly Interface:** Input forms for entering members, items, and the percentage share of each item.
- **Customizable GST & Service Charges:** Ability to input GST and Service Charges to accurately split the bill.
- **Real-Time Calculation:** Each member's share is calculated in real-time, including the tax and service charges.
- **Total Bill Summary:** A summary of the total amount payable by each member and the total bill amount is displayed.

## How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/bill-splitter.git
   cd bill-splitter
   ```

2. **Install Dependencies:**

   Ensure you have Python installed. Then, install the necessary packages using pip:

   ```bash
   pip install streamlit
   ```

3. **Run the Application:**

   Launch the Streamlit application using the following command:

   ```bash
   streamlit run app.py
   ```

4. **Access the Application:**

   The application will open in your default web browser at `http://localhost:8501`. Follow the on-screen instructions to split your bill.

## Usage

1. **Enter the Number of Members:**
   - Input the total number of members involved in the bill splitting.

2. **Enter Member Details:**
   - Input the name of each member.

3. **Enter Bill Items:**
   - Input the total number of items on the bill.
   - For each item, specify the name and cost.

4. **Specify Consumption Details:**
   - For each item, enter the percentage of the item cost that each member is responsible for.

5. **Include GST and Service Charges:**
   - Optionally include GST and Service Charge percentages.

6. **View Bill Split:**
   - The app will display how much each member should pay, including their share of taxes and service charges.
   - A summary of the total bill is also displayed.

## Example

Here is an example of how you can use the Bill Splitter:

1. **Number of Members:** 3
2. **Members:** Alice, Bob, Charlie
3. **Items:** 
   - Item 1: Pizza - ₹500
   - Item 2: Drinks - ₹300
4. **Consumption Details:** 
   - Pizza: Alice 50%, Bob 30%, Charlie 20%
   - Drinks: Alice 30%, Bob 40%, Charlie 30%
5. **GST:** 5%
6. **Service Charge:** 10%

The application will then calculate and display how much each member should pay, taking into account their individual consumption, GST, and service charge.


## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or feedback, please reach out to [anirudhv2001@ymail.com](mailto:anirudhv2001@ymail.com).
