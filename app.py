import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="Ids Med Parts Monitor", layout="wide")

# Initialize session state
if "parts" not in st.session_state:
    st.session_state.parts = []

# Custom CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .modal {
        display: none;
        position: fixed;
        z-index: 10000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
    }
    .modal-content {
        background-color: #fefefe;
        margin: 10% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 400px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add Part Modal
components.html(
    """
    <button id="openModal" type="button">Add New Part</button>
    <div id="pinModal" class="modal">
        <div class="modal-content">
            <h3>Enter PIN</h3>
            <input type="password" id="pinInput" placeholder="Enter PIN" style="width: 100%; padding: 8px; margin-bottom: 10px;" />
            <button id="pinSubmit" type="button">Submit</button>
        </div>
    </div>
    <div id="formModal" class="modal">
        <div class="modal-content">
            <h3>Add New Part</h3>
            <form id="partForm">
                <input name="part_number" placeholder="Part Number" style="width:100%; padding:8px; margin-bottom:8px;" required />
                <input name="part_name" placeholder="Part Name" style="width:100%; padding:8px; margin-bottom:8px;" required />
                <input name="quantity" type="number" placeholder="Quantity" style="width:100%; padding:8px; margin-bottom:8px;" required />
                <input name="date" type="date" value="{datetime.today().strftime('%Y-%m-%d')}" style="width:100%; padding:8px; margin-bottom:8px;" required />
                <button type="submit">Add Part</button>
            </form>
        </div>
    </div>
    <script>
    const openBtn = document.getElementById("openModal");
    const pinModal = document.getElementById("pinModal");
    const formModal = document.getElementById("formModal");
    const pinInput = document.getElementById("pinInput");
    const pinSubmit = document.getElementById("pinSubmit");
    const correctPin = "0101";

    openBtn.onclick = () => {
        pinModal.style.display = "block";
        pinInput.focus();
    };

    pinSubmit.onclick = () => {
        if (pinInput.value === correctPin) {
            pinModal.style.display = "none";
            formModal.style.display = "block";
            document.querySelector("input[name='part_number']").focus();
        } else {
            alert("Wrong PIN!");
        }
    };

    window.onclick = (event) => {
        if (event.target == pinModal) pinModal.style.display = "none";
        if (event.target == formModal) formModal.style.display = "none";
    };

    const form = document.getElementById("partForm");
    form.onsubmit = (e) => {
        e.preventDefault();
        const data = Object.fromEntries(new FormData(form).entries());
        window.parent.postMessage({ type: "ADD_PART", data }, "*");
        formModal.style.display = "none";
        form.reset();
    };
    </script>
    """,
    height=900,
)

# Handle new parts from frontend
msg = st.experimental_get_query_params().get("msg", [None])[0]
if msg:
    st.write("Message:", msg)

st.markdown("### Parts Data")

if st.session_state.parts:
    df = pd.DataFrame(st.session_state.parts)
    st.dataframe(df, use_container_width=True)
    fig = px.bar(df, x="part_name", y="quantity", title="Stock Overview")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No parts added yet.")
