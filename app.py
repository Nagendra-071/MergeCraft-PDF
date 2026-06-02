import streamlit as st
import pypdf
import io

st.title("📄 Custom PDF Merger")
st.write("Limit: 10 files")

uploaded_files = st.file_uploader("Upload your PDFs here(Maximum 10 files )", type="pdf", accept_multiple_files=True, max_file=10)

    


if uploaded_files:
    pdf_dict = {i: file for i, file in enumerate(uploaded_files, start=1)}
    
    st.write("### Current Order:")
    for i, file in pdf_dict.items():
        st.write(f"**Index {i}**: {file.name}")
        
    rearranged = st.text_input("To rearrange, enter the index numbers (example: 2 1 3) in your preferred order with space after each index :")
    st.write("**Press Enter after rearrange.**")
    
    if rearranged:
        new_order_tuple = tuple(int(num) for num in rearranged.split())
        ordered_files = [pdf_dict[index] for index in new_order_tuple]
    else:
        ordered_files = uploaded_files

    if st.button("Merge PDFs"):
        writer = pypdf.PdfWriter()
        
        for file in ordered_files:
            file.seek(0)  # Resets internal file pointer to prevent EmptyFileError
            writer.append(io.BytesIO(file.read()))
            
    # 2. Save the merged data into a temporary in-memory buffer    
        output_pdf = io.BytesIO()
        writer.write(output_pdf)
        output_pdf.seek(0)
        
        st.download_button(
            label="📥 Download Merged PDF",
            data=output_pdf,
            file_name="merged.pdf",
            mime="application/pdf"
        )