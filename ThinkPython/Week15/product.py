import os
cwd = os.getcwd()

resources_folder = 'C:\Users\Joe\Resources'
# real path is actually:'C:\Users\Joe\AppData\Local\Logos\Data\2zlr00mp.2au\ResourceManager\Resources'
# my function can't get past '2zlr00mp.2au', so I have copied the resource folder to a location which is easier to find

downloaded_folder = 'C:\Users\Joe\Downloaded'
# real path is actually: 'C:\Users\Joe\AppData\Local\Logos\Data\renamed\ResourceManager\Resources'

def get_file_dict(listfiles):
	"""Takes the list of the files expected to be in the Resources folder and makes a dictionary. 
    """
	file_dict = dict()
	fin = open('listfiles.txt')
	line = fin.readline()
	for line in fin:
		file_name = line.strip()
		file_dict[file_name] = 'not found'
	return file_dict
	
def get_file_list(logos_subfolder):
	"""Makes a list of files found in the deignated folder.  
	Used to check both the Resources folder, where the resources should be, and the Downloaded folder, which should be empty.
    """
	file_list = []
	for root, dirs, files in os.walk(logos_subfolder):
		for filename in files:
			file_list.append(filename)
	return file_list

def check_for_resources(file_dict, file_list):
	"""Compares files found in the Resources folder with the files it is supposed to have
	"""
	for file_names in file_list:
		if file_names in file_dict:
			file_dict[file_names] = 'found'
		else:
			file_dict[file_names] = 'extra'
	return file_dict

def write_report(checked_dict, downloaded_list):
	"""Writes results to resourcesreport.txt
	"""
	found_resources = []
	notfound_resources = []
	extra_resources = []
	resources_report = open('resourcesreport.txt', 'w')
	if len(downloaded_list) < 1:
		resources_report.write('Downloaded folder is empty, as expected.')
		resources_report.write('\n') 
		resources_report.write('\n')
	else:
		resources_report.write('File(s) found in the Downloaded folder, this is a problem:')
		add_list(downloaded_list, resources_report)
	for keyz in checked_dict:
		if checked_dict[keyz] == 'found':
				found_resources.append(keyz)
		elif checked_dict[keyz] == 'not found':
			notfound_resources.append(keyz)
		else: extra_resources.append(keyz)
	resources_report.write('Missing resources:')
	add_list(notfound_resources, resources_report)
	resources_report.write('Extra resources:')
	add_list(extra_resources, resources_report)
	resources_report.write('Found resources:')
	add_list(found_resources, resources_report)
	resources_report.close()
	
def add_list(file_list, resources_report):
	file_list.sort()
	resources_report.write('\n')
	for filenamez in file_list:
		resources_report.write(filenamez)
		resources_report.write('\n')
	resources_report.write('\n')

resources_dict = get_file_dict('listfiles.txt')
resources_list = get_file_list(resources_folder)
downloaded_list = get_file_list(downloaded_folder)
checked_dict = check_for_resources(resources_dict, resources_list)
write_report(checked_dict, downloaded_list)

print 'Go to',
print cwd,
print 'for resourcesreport.txt'



