import streamlit as st
import os
from PIL import Image
import pandas as pd 
from PyPDF2 import PdfReader

# Load Images
@st.cache_data
def load_image(image_file):
	img = Image.open(image_file)
	return img

def read_pdf(file):
	pdfReader = PdfReader(file)
	count = len(pdfReader.pages)
	all_page_text = ""
	for i in range(count):
		page = pdfReader.pages[i]
		all_page_text += page.extract_text()

	return all_page_text

# Fxn to Save Uploaded File to Directory
def save_uploaded_file(uploadedfile):
	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
		f.write(uploadedfile.getbuffer())

	return st.success("Saved file :{} in tempDir".format(uploadedfile.name))


def main():
	st.title("Multiple File Uploads")

	menu = ["Home","Dataset","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Upload Images")
		uploadedFiles = st.file_uploader("Upload Multiple Images",type=['png','jpeg','jpg'],
								   accept_multiple_files=True)
		if uploadedFiles is not None:
			st.write(uploadedFiles)
			for file in uploadedFiles:
				st.write(file.name)
				st.image(load_image(file),width=250)
				save_uploaded_file(file)

	elif choice == "Dataset":
		st.subheader("Upload Datasets")
		dataFiles = st.file_uploader("Upload CSV(s)",type=["csv"],
							  accept_multiple_files=True)
		if dataFiles is not None:
			st.write(dataFiles)
			for file in dataFiles:
				st.write(file.name)
				df = pd.read_csv(file)
				st.dataframe(df)
				save_uploaded_file(file)

	else:
		st.subheader("About App")

if __name__ == '__main__':
	main()