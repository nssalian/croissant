import streamlit as st

from core.state import CurrentStep
from core.state import Metadata
from utils import needed_field
from utils import set_form_step


def render_overview():
    metadata = st.session_state[Metadata]
    name = st.text_input(
        label=needed_field("Name"),
        value=metadata.name,
        placeholder="Dataset",
    )
    description = st.text_area(
        label="Description",
        value=metadata.description,
        placeholder="Provide a clear description of the dataset.",
    )
    st.subheader(f"{len(metadata.distribution)} Resources")
    st.subheader(f"{len(metadata.record_sets)} Record Sets")
    st.session_state[Metadata].update_metadata(
        name=name,
        description=description,
        license=metadata.license,
        url=metadata.url,
        citation=metadata.citation,
    )
