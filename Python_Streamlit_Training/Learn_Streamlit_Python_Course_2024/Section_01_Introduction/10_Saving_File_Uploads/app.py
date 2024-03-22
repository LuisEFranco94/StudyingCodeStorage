import streamlit as st
import os
from PIL import Image
import pandas as pd 

# Load Images
@st.cache_data
def load_image(image_file):
	img = Image.open(image_file)
	return img

# Fxn to Save Uploaded File to Directory
def save_uploaded_file(uploadedfile):
	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
		f.write(uploadedfile.getbuffer())
	return st.success("Saved file :{} in tempDir".format(uploadedfile.name))


def main():
	st.title("File Uploads & Saved File to Directory App")

	menu = ["Home","Dataset","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Upload Images")
		image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
		if image_file is not None:
			file_details = {"filename":image_file.name, "filetype":image_file.type}
			st.write(file_details)
			img = load_image(image_file)
			st.image(img,width=250)
			
            # Saving File to a directory called tempDir
			# tempDir/imagename.png
			with open(os.path.join("tempDir",image_file.name),"wb") as f:
				f.write(image_file.getbuffer())

			st.success("File Saved")


	elif choice == "Dataset":
		st.subheader("Dataset")
		datafile = st.file_uploader("Upload CSV",type=["csv"])
		if datafile is not None:
			file_details = {"filename":datafile.name,
			"filetype":datafile.type}
			df = pd.read_csv(datafile)
			st.dataframe(df)
			save_uploaded_file(datafile)


	else:
		st.subheader("About App")
		st.text("Jesus Saves @JCharisTech")
		st.text("Learn Streamlit - Jesse E.Agbe(JCharis)")

if __name__ == '__main__':
	main()