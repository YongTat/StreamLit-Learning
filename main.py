import streamlit as st
import pandas as pd
import os

st.set_page_config(layout = "wide")

@st.cache_resource
def getFileAsDataFrame(fileName: str, fileDir: str):
    df = pd.read_csv(fileDir+"\\"+fileName)
    return df

st.title("Tat's Personal Data Analyzer")

if "folderSet" not in st.session_state:
    st.session_state.folderSet = False

with st.form(key = "Folder_Directory"):
    test_dir = st.text_input("Folder Path:")
    st.write(test_dir)
    submit = st.form_submit_button("Confirm Folder")
    # Checks after submit
    if(submit):
        csv_files = os.listdir(test_dir)
        inputfiles = []
        outputfiles = []
        for file in csv_files:
            if file.endswith(".csv"):
                if file.startswith("stat_"):
                    outputfiles.append(file)
                else:
                    inputfiles.append(file)

        st.session_state.folderSet = True
        st.session_state.dir = test_dir
        st.session_state.inputfiles = inputfiles
        st.session_state.outputfiles = outputfiles


if st.session_state.folderSet:
    tabs = st.tabs(st.session_state.outputfiles)

    for tab, tab_header in zip(tabs, st.session_state.outputfiles):
        with tab:
            st.header(f"{tab_header}")
            df = getFileAsDataFrame(tab_header, st.session_state.dir)
            st.dataframe(df)
