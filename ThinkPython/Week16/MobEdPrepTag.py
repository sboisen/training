import os
import shutil
import glob


# Prompt for resource ID to use throughout

str_resource = raw_input("Enter resource ID (all caps):\n")
str_resource_path = os.path.join("T:", "Resources", str_resource)
dct_resource_subfolder_paths =	{"send": os.path.join(str_resource_path, "Send"),
								"raw":		{"source": os.path.join(str_resource_path, "Raw", "Source"),
											"reference": os.path.join(str_resource_path, "Raw", "Reference")
											},
								"images":	{"final": os.path.join(str_resource_path, "Final", "Images"),
											"bullet": os.path.join(str_resource_path, "XML", "smart-bullets")
											},
								"xml": os.path.join(str_resource_path, "XML"),
								}


if os.path.exists(str_resource_path):
	

	# Move transcription files out of text resource Raw>Source folder
	# Will handle later
	

	# Create Send folder, if necessary
	

	if not os.path.exists(dct_resource_subfolder_paths["send"]):
		os.mkdir(dct_resource_subfolder_paths["send"])
	

	# Copy *.xml files to Send folder
	
	lst_xml_file_paths = glob.glob(os.path.join(dct_resource_subfolder_paths["xml"], "*.xml"))
	for str_xml_file_path in lst_xml_file_paths:
		shutil.copy(str_xml_file_path, dct_resource_subfolder_paths["send"])
	
	# Copy Raw>Reference and Raw>Source to Send folder
	

	for str_raw_key in dct_resource_subfolder_paths["raw"]:
		if os.path.exists(dct_resource_subfolder_paths["raw"][str_raw_key]):
			str_raw_path_end = os.path.basename(dct_resource_subfolder_paths["raw"][str_raw_key])
			str_send_path = os.path.join(dct_resource_subfolder_paths["send"], str_raw_path_end)
			if not os.path.exists(str_send_path):
				shutil.copytree(dct_resource_subfolder_paths["raw"][str_raw_key], str_send_path)
			
			# Copy Final>Images and XML>smart-bullets to Send>Source folder
			
			if str_raw_key == "source":
				for str_image_key in dct_resource_subfolder_paths["images"]:
					if os.path.exists(dct_resource_subfolder_paths["images"][str_image_key]):
						str_img_path_end = os.path.basename(dct_resource_subfolder_paths["images"][str_image_key])
						str_send_image_path = os.path.join(str_send_path, str_img_path_end)
						if not os.path.exists(str_send_image_path):
							shutil.copytree(dct_resource_subfolder_paths["images"][str_image_key], str_send_image_path)
						
					else:
						print("Your " + str_image_key + " image folder is missing")
			
		else:
			print("Your raw " + str_raw_key + " folder is missing")
	

	# Create SMIL folder under video resource Raw>Source
	# Move *.smil files from video Final>Videos>1>350 folder to Raw>Source>SMIL
	# Will handle later
	
else:
	print("Your resource folder is missing")

