from PyInstaller.utils.hooks import copy_metadata, collect_data_files

datas = copy_metadata("streamlit")

datas += copy_metadata("streamlit_autorefresh")
