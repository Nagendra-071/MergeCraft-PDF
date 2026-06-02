import streamlit as st
import pypdf
import io

st.title("📄 MergeCraft PDF")
st.write("Limit: 10 files at a time")

uploaded_files = st.file_uploader("Upload your PDFs here", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if len(uploaded_files) > 10:
        st.error("🛑 Too many files! The maximum allowed is 10. Please remove some files to proceed.")
    else:
        pdf_dict = {i: file for i, file in enumerate(uploaded_files, start=1)}
        
        st.write("### Current Order:")
        for i, file in pdf_dict.items():
            st.write(f"**Index {i}**: {file.name}")
            
        rearranged = st.text_input("To rearrange, enter the index numbers (example: 2 1 3) in your preferred order:")
        st.write("**Press Enter after typing your custom sequence.**")
        
        if rearranged:
            new_order_tuple = tuple(int(num) for num in rearranged.split())
            ordered_files = [pdf_dict[index] for index in new_order_tuple]
        else:
            ordered_files = uploaded_files

        if st.button("Merge PDFs"):
            writer = pypdf.PdfWriter()
            
            for file in ordered_files:
                file.seek(0)
                writer.append(io.BytesIO(file.read()))
                
            output_pdf = io.BytesIO()
            writer.write(output_pdf)
            output_pdf.seek(0)
            
            st.download_button(
                label="📥 Download Merged PDF",
                data=output_pdf,
                file_name="merged.pdf",
                mime="application/pdf"
            )