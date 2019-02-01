## GUI for Copy and paste searchable text
##
##
## Author: 			Phillip Walker
## Contact: 		phil.walker@nssi.us
## Original Date: 	02/01/2019

import tkinter as tk


# Create initial window
window = tk.Tk()
window.title("Find My Stuff")

global_width = window.winfo_screenwidth()-80
global_height = window.winfo_screenheight()-200
window.geometry('%sx%s' % (global_width, global_height))


def searchTheText():
	"""This function will be used to search through the text in TEXT1 and change the background color of the text that matches."""
	# Remove highlight at beginning of each search.
	text1.tag_remove("highlight", "1.0", "end-1c")
	text2.tag_remove("highlight2", "1.0", "end-1c")
	
	found =0
	
	# Collect the first textbox into a string
	inputText = text1.get("1.0","end-1c")
	inputText.strip()
	
	# Collect the second textbox into a string
	searchText = text2.get("1.0","end-1c")
	searchText.strip()
	searchLength = len(searchText)
	
	# Search through the text for the key phrase
	for i in range(1,int(text1.index('end').split('.')[0])-1):
		line = text1.get(str(str(i) + '.' + str(0)),str(str(i) + '.' + 'end'))
		if searchText in line:
			found += 1
			# Determine the start point of the match, and highlight the match
			j = line.index(searchText) 
			pos1 = str(str(i) + '.' + str(j))
			pos2 = str(str(i) + '.' + str(j+searchLength))
			text1.tag_add("highlight", pos1, pos2)
			text1.tag_config("highlight", background="yellow", foreground="blue")

			#Check if the substring is still present in the current line
			testline = line[j+searchLength:]
			pastIndex = j+searchLength
			while searchText in testline:
				if len(testline) > 0:
					j = testline.index(searchText) 
					pos1 = str(str(i) + '.' + str(j+pastIndex))
					pos2 = str(str(i) + '.' + str(j+searchLength+pastIndex))
					text1.tag_add("highlight", pos1, pos2)
					text1.tag_config("highlight", background="yellow", foreground="blue")
					testline = testline[j+searchLength:]
					pastIndex += j+searchLength
	
	# Highlight the search text if it is not found in the pasted text
	if found == 0:
		text2.tag_add("highlight2", "1.0", "end-1c")
		text2.tag_config("highlight2", background="red", foreground="black")


# Label the first text box
lbl1 = tk.Label(window, text = "Paste text you want to search through below:")
lbl1.pack()


# Add a scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill=tk.Y)


# Add the first text box
text1 = tk.Text(window, height = 20, width = 200)
text1.insert(tk.INSERT, "Paste text Here!\n")
text1.pack()



# Set the scrollbar to correspond to the y-position of the first text box
text1.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = text1.yview)


# Label the second text box
lbl2 = tk.Label(window, text = "Add text that you want to search for:")
lbl2.pack()


# Add the second text box
text2 = tk.Text(window, height = 5, width = int(.95*global_width))
text2.insert(tk.INSERT, "Search here!")
text2.pack()


# Create the search button
button1 = tk.Button(window, text = "Search!", command = searchTheText)
button1.pack()


# Run the GUI
window.mainloop()
