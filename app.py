import streamlit as st
import pandas as pd

from recovery.device import list_devices
from recovery.scanner import scan_drive


st.set_page_config(
    page_title="ExRecover",
    layout="wide"
)


st.title("🛠 ExRecover")
st.caption(
    "Read-only exFAT recovery tool"
)


st.warning(
"""
Safety mode:
- Source drives are opened READ ONLY
- No formatting
- No writes to source media
"""
)


devices = list_devices()


drive = st.selectbox(
    "Select external drive",
    devices
)


if st.button("Scan"):

    with st.spinner(
        "Scanning drive..."
    ):

        results = scan_drive(
            drive
        )


    df=pd.DataFrame(results)

    st.success(
        f"{len(df)} files found"
    )

    st.dataframe(
        df,
        use_container_width=True
    )
