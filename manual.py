import streamlit as st

st.set_page_config(page_title="Smart Court Booking Manual", layout="wide")
st.title("📘 Smart Online Court Booking System ")

# Sidebar with only 2 options
section = st.sidebar.radio("📚 Navigate", [
    "Installation Guide",
    "User Manual"
])

# =========================
# 📁 Installation Guide
# =========================
if section == "Installation Guide":
    st.header("Installation Guide (For Developers)")
    
    st.subheader("Requirements")
    st.write("""
    - Python 3.8 or newer  
    - pip (Python package manager)  
    - Streamlit  
    - SQLite3
    """)

    st.subheader("Steps")
    st.markdown("""
    **1. Clone or Download the Project Folder**
    - Include the following files:
        - `app.py` (main script)  
        - `style.css` (for custom styles)  
        - `logo.png`, `logo1.png` (branding images)  
        - `qr.png` (QR to system link)

    **2. Open Terminal and Navigate to Folder**
    ```bash
    cd path\\to\\your\\project
    ```

    **3. Install Required Packages**
    ```bash
    pip install streamlit pandas
    ```

    **4. Run the Application**
    ```bash
    streamlit run app.py
    ```

    **5. Access the System**
    - In your browser:  
      [https://court-booking-fz4hesyxcn6nfjryrbn5at.streamlit.app](https://court-booking-fz4hesyxcn6nfjryrbn5at.streamlit.app)
    - Or scan the QR code below:
    """)
    
    st.image("qr.png", caption="Scan to open the app", width=200)

# =========================
# 👤 User Manual
# =========================
elif section == "User Manual":
    st.header("User Manual")

    st.markdown("""
    ### 1. Logging In
    - Clients: Use any username and password
    - Admin:  
      - Username: `admin`  
      - Password: `123456`

    ---
    ### 2. Booking a Court (Client)
    1. Select a court (e.g., Court 1 to Court 6)  
    2. Choose a date  
    3. Pick an available time slot  
    4. Enter your phone number (9–12 digits)  
    5. Click the time slot to confirm booking  
    6. A success message will appear
    """)
    
    st.image("login_step2.png", caption="Step 2: Enter credentials", use_container_width=True)

    st.markdown("""
    ### 3. Viewing Bookings
    - **Clients**: View personal bookings via the sidebar  
    - **Admins**: View all bookings and details
    """)
    
    st.image("login_step3.png", caption="Step 3: view booking", use_container_width=True)

    st.markdown("""
    ### 4. Admin Functions
    - Cancel bookings  
    - Download CSV of all bookings  
    - Login with Admin credentials only

    ### 5. Logging Out
    - Click **Logout** in the sidebar to end your session

    ---
    ### 📞 Admin Contact
    - **Name**: Muhammad Fauzan Syafiq  
    - **Email**: fauzansyafiq18@google.com  
    - **Phone**: +6011-2545 8006
    """)
