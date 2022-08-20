import tkinter
import math
from PIL import ImageTk, Image

canvasEvent = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))

class inputWindow:
	def __init__(self):
        #main window object
		self.__mainWindow = tkinter.Tk()
		self.__mainWindow.title("Image Editor")
		
		#images used in the gui
		self.__mainImage = Image.new("RGB", (480, 960))
		self.__previewImage = Image.new("RGB", (480, 960))
		self.__tkinterImage = ImageTk.PhotoImage(Image.new("RGB", (480, 960)))
		
		#variables used to store mouse coords
		self.__mouseX = 0
		self.__mouseY = 0
		self.__numMousePositions = 0
		self.__mouseFilterSelected = False
		self.__mouseCoordsList = list()
		
		#scrollbar stuff
		self.__canvas = tkinter.Canvas(self.__mainWindow)
		self.__scrollbar = tkinter.Scrollbar(self.__mainWindow, orient = 'vertical', command = self.__canvas.yview)
		self.__canvas.configure(yscrollcommand = self.__scrollbar.set)
		
		self.__masterFrame = tkinter.Frame(self.__canvas)
		self.__masterFrameID = self.__canvas.create_window((0, 0), window = self.__masterFrame, anchor = 'nw')
		
		self.__masterFrame.bind('<Configure>', self.__configureMasterFrame)
		self.__canvas.bind('<Configure>', self.__configureCanvas)
		
		#frames
		self.__loadLabelFrame = tkinter.Frame(self.__masterFrame)
		self.__loadEntryFrame = tkinter.Frame(self.__masterFrame)
		self.__saveLabelFrame = tkinter.Frame(self.__masterFrame)
		self.__saveEntryFrame = tkinter.Frame(self.__masterFrame)
		self.__basicFilterLabelFrame = tkinter.Frame(self.__masterFrame)
		self.__basicFilterOptionsFrame = tkinter.Frame(self.__masterFrame)
		self.__variableFilterLabelFrame = tkinter.Frame(self.__masterFrame)
		self.__variableFilterOptionsFrame = tkinter.Frame(self.__masterFrame)
		self.__variableFilterEntryFrame = tkinter.Frame(self.__masterFrame)
		self.__mouseFilterInstructionsFrame = tkinter.Frame(self.__masterFrame)
		self.__mouseFilterOptionsFrame = tkinter.Frame(self.__masterFrame)
		self.__changesButtonLabelFrame = tkinter.Frame(self.__masterFrame)
		self.__changesButtonFrame = tkinter.Frame(self.__masterFrame)

        #fills label frames
		self.__loadLabel = tkinter.Label(self.__loadLabelFrame, text = "Enter The Image you Want to Load: ")
		self.__loadLabel.pack()
		
		self.__saveLabel = tkinter.Label(self.__saveLabelFrame, text = "Enter Filename you Want to Save the Image Under: ")
		self.__saveLabel.pack()
		
		self.__basicFilterLabel = tkinter.Label(self.__basicFilterLabelFrame, text = "Select Static Filter you Would Like to Apply: ")
		self.__basicFilterLabel.pack()
		
		self.__variableFilterLabel = tkinter.Label(self.__variableFilterLabelFrame, text = "Select Variable Filter you Would Like to Apply: ")
		self.__variableFilterLabel.pack()
		
		self.__changesButtonLabel = tkinter.Label(self.__changesButtonLabelFrame, text = "Click Apply to Save Changes to Current Image\nClick Discard to Revert All Changes Before the Last Apply or Load or Save: ")
		self.__changesButtonLabel.pack()
		
		#image load entry frame
		self.__loadEntry = tkinter.Entry(self.__loadEntryFrame, width = 40, bd = 4)
		self.__loadEntry.insert(0,"ImageInput/sampleName.jpg")
		self.__loadButton = tkinter.Button(self.__loadEntryFrame, text = "Load Image", command = self.__loadImage)
		self.__loadEntry.pack(side = "left", padx = 4)
		self.__loadButton.pack(side = "left", padx = 4)
		
		#image save entry frame
		self.__saveEntry = tkinter.Entry(self.__saveEntryFrame, width = 40, bd = 4)
		self.__saveEntry.insert(0,"ImageOutput/sampleName.jpg")
		self.__saveButton = tkinter.Button(self.__saveEntryFrame, text = "Save Image", command = self.__saveImage)
		self.__saveEntry.pack(side = "left", padx = 4)
		self.__saveButton.pack(side = "left", padx = 4)
		
		#basic filter entry frame
		self.__basicFilterOptions = ["None", "Sunset", "Negative", "Smooth", "Contrast", "Brighten", "Darken",  "Night Vision", "Greyscale", "Shrink", "Expand", "Rotate"]
		self.__basicFilterStringVar = tkinter.StringVar(self.__mainWindow)
		self.__basicFilterStringVar.set(self.__basicFilterOptions[0])
		self.__basicFilterOptionsMenu = tkinter.OptionMenu(self.__basicFilterOptionsFrame, self.__basicFilterStringVar, *self.__basicFilterOptions)
		self.__basicFilterButton = tkinter.Button(self.__basicFilterOptionsFrame, text = "Apply Filter", command = lambda: self.__basicFilter(self.__previewImage, self.__basicFilterStringVar.get()))
		self.__basicFilterOptionsMenu.pack(side = "left", padx = 4)
		self.__basicFilterButton.pack(side = "left", padx = 4)
		
		#variable filter entry frame
		self.__variableFilterOptions = ["None", "RGB Multiplier", "Brightness Multiplier", "Accent Multiplier"]
		self.__variableFilterStringVar = tkinter.StringVar(self.__mainWindow)
		self.__variableFilterStringVar.set(self.__variableFilterOptions[0])
		self.__variableFilterOptionsMenu = tkinter.OptionMenu(self.__variableFilterOptionsFrame, self.__variableFilterStringVar, *self.__variableFilterOptions)
		self.__modifyVariableFilterButton = tkinter.Button(self.__variableFilterOptionsFrame, text = "Modify Filter", command = lambda: self.__modifyFilter(self.__variableFilterStringVar.get()))
		self.__variableFilterButton = tkinter.Button(self.__variableFilterOptionsFrame, text = "Apply Filter", state = "disabled", command = lambda: self.__variableFilter(self.__previewImage, self.__variableFilterStringVar.get()))
		self.__variableFilterOptionsMenu.pack(side = "left", padx = 4)
		self.__modifyVariableFilterButton.pack(side = "left", padx = 4)
		self.__variableFilterButton.pack(side = "left", padx = 4)
		
		#Mouse input Entry Frame
		self.__mouseFilterInstructionStringVar = tkinter.StringVar()
		self.__mouseFilterInstructionStringVar.set("Select Variable Mouse Filter and Shape and Follow Instructions about Specific Filters: ")
		self.__mouseFilterInstructions = tkinter.Label(self.__mouseFilterInstructionsFrame, textvariable = self.__mouseFilterInstructionStringVar)
		self.__mouseFilterInstructions.pack()
		
		#Mouse input variable filter entry frame
		self.__mouseFilterOptions = ["None", "Remove", "Sunset", "Negative", "Smooth", "Contrast", "Brighten", "Darken",  "Night Vision"]
		self.__mouseFilterShapeOptions = ["None", "Crop", "Square", "Circle"]
		self.__mouseFilterStringVar = tkinter.StringVar(self.__mainWindow)
		self.__mouseFilterShapeStringVar = tkinter.StringVar(self.__mainWindow)
		self.__mouseFilterStringVar.set(self.__mouseFilterOptions[0])
		self.__mouseFilterShapeStringVar.set(self.__mouseFilterShapeOptions[0])
		self.__mouseFilterOptionsMenu = tkinter.OptionMenu(self.__mouseFilterOptionsFrame, self.__mouseFilterStringVar, *self.__mouseFilterOptions)
		self.__mouseFilterOptionsShapeMenu = tkinter.OptionMenu(self.__mouseFilterOptionsFrame, self.__mouseFilterShapeStringVar, *self.__mouseFilterShapeOptions)
		self.__mouseFilterButton = tkinter.Button(self.__mouseFilterOptionsFrame, text = "Apply Filter", command = lambda: self.__selectArea(self.__mouseFilterShapeStringVar.get()))
		self.__mouseFilterOptionsMenu.pack(side = "left", padx = 4)
		self.__mouseFilterOptionsShapeMenu.pack(side = "left", padx = 4)
		self.__mouseFilterButton.pack(side = "left", padx = 4)
		
		#variable filter variable entry
		self.__lineOneFrame = tkinter.Frame(self.__variableFilterEntryFrame)
		self.__variable1FilterEntryLabelStringVar = tkinter.StringVar()
		self.__variable1FilterEntryLabel = tkinter.Label(self.__lineOneFrame, textvariable = self.__variable1FilterEntryLabelStringVar)
		self.__variable1FilterEntry = tkinter.Entry(self.__lineOneFrame, width = 12, bd = 4)
		self.__variable1FilterEntryLabel.pack(side = "left", padx = 4)
		self.__variable1FilterEntry.pack(side = "left", padx = 4)
		
		self.__lineTwoFrame = tkinter.Frame(self.__variableFilterEntryFrame)
		self.__variable2FilterEntryLabelStringVar = tkinter.StringVar()
		self.__variable2FilterEntryLabel = tkinter.Label(self.__lineTwoFrame, textvariable = self.__variable2FilterEntryLabelStringVar)
		self.__variable2FilterEntry = tkinter.Entry(self.__lineTwoFrame, width = 12, bd = 4)
		self.__variable2FilterEntryLabel.pack(side = "left", padx = 4)
		self.__variable2FilterEntry.pack(side = "left", padx = 4)
		
		self.__lineThreeFrame = tkinter.Frame(self.__variableFilterEntryFrame)
		self.__variable3FilterEntryLabelStringVar = tkinter.StringVar()
		self.__variable3FilterEntryLabel = tkinter.Label(self.__lineThreeFrame, textvariable = self.__variable3FilterEntryLabelStringVar)
		self.__variable3FilterEntry = tkinter.Entry(self.__lineThreeFrame, width = 12, bd = 4)
		self.__variable3FilterEntryLabel.pack(side = "left", padx = 4)
		self.__variable3FilterEntry.pack(side = "left", padx = 4)
		
		#image Changes Apply/Discard Frame
		self.__applyChangesButton = tkinter.Button(self.__changesButtonFrame, text = "Apply Changes", command = self.__applyChanges)
		self.__discardChangesButton = tkinter.Button(self.__changesButtonFrame, text = "Discard Changes", command = self.__discardChanges)
		self.__applyChangesButton.pack(side = "left", padx = 4)
		self.__discardChangesButton.pack(side = "left", padx = 4)
		
		#setting up a image canvas with scrollbars
		self.__imageFrame = tkinter.Frame(self.__mainWindow)
		self.__imageFrame.grid_rowconfigure(0, weight = 1)
		self.__imageFrame.grid_columnconfigure(0, weight = 1)
		
		self.__XScroll = tkinter.Scrollbar(self.__imageFrame, orient = tkinter.HORIZONTAL)
		self.__XScroll.grid(row = 1, column  = 0, sticky = tkinter.E + tkinter.W)
		
		self.__YScroll = tkinter.Scrollbar(self.__imageFrame, orient = tkinter.VERTICAL)
		self.__YScroll.grid(row = 0, column = 1, sticky = tkinter.N + tkinter.S)
		
		self.__imageCanvas = tkinter.Canvas(self.__imageFrame, xscrollcommand = self.__XScroll.set, yscrollcommand = self.__YScroll.set)
		self.__imageCanvas.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
		
		self.__XScroll.config(command = self.__imageCanvas.xview)
		self.__YScroll.config(command = self.__imageCanvas.yview)
		
		#mouseclick event binding
		self.__imageCanvas.bind("<ButtonRelease-1>", self.__setMouseCoords)

        #packs frames
		self.__canvas.pack(side = 'left', fill = 'both', expand = 'true')
		self.__scrollbar.pack(side = 'left', fill = 'y', expand = 'false')
		self.__imageFrame.pack(side = 'left', fill = tkinter.BOTH, expand = 1)
		self.__loadLabelFrame.pack()
		self.__loadEntryFrame.pack(pady = 4)
		self.__saveLabelFrame.pack()
		self.__saveEntryFrame.pack(pady = 4)
		self.__basicFilterLabelFrame.pack()
		self.__basicFilterOptionsFrame.pack(pady = 4)
		self.__variableFilterLabelFrame.pack()
		self.__variableFilterOptionsFrame.pack(pady = 4)
		self.__variableFilterEntryFrame.pack(pady = 2)
		self.__mouseFilterInstructionsFrame.pack()
		self.__mouseFilterOptionsFrame.pack(pady = 4)
		self.__changesButtonLabelFrame.pack()
		self.__changesButtonFrame.pack(pady =  4)

		#starts main loop
		self.__mainWindow.mainloop()
		
	#function to be called when mouse is clicked
	def __setMouseCoords(self, event):
		self.__mouseX, self.__mouseY = canvasEvent(event, self.__imageCanvas)
		if self.__mouseFilterSelected and (len(self.__mouseCoordsList) < self.__numMousePositions):
			self.__mouseCoordsList.append((self.__mouseX, self.__mouseY))
			if (len(self.__mouseCoordsList) >= self.__numMousePositions):
				self.__mouseFilter(self.__previewImage, self.__mouseFilterStringVar.get(), self.__mouseFilterShapeStringVar.get())
			
	#these functinos exist because of the scrollbar
	def __configureCanvas(self, event):
		if self.__masterFrame.winfo_reqwidth() != self.__canvas.winfo_width():
			self.__canvas.itemconfigure(self.__masterFrameID, width = self.__canvas.winfo_width())

	def __configureMasterFrame(self, event):
		self.__canvas.config(height = self.__masterFrame.winfo_reqheight())
		size = (self.__masterFrame.winfo_reqwidth(), self.__masterFrame.winfo_reqheight())
		self.__canvas.configure(scrollregion="0 0 %s %s" % size)
		if self.__masterFrame.winfo_reqwidth() != self.__canvas.winfo_width():
			self.__canvas.config(width = self.__masterFrame.winfo_reqwidth())
	
	#loads the specified image into the 
	def __loadImage(self):
		loadedImage = Image.open(self.__loadEntry.get())
		self.__mainImage = loadedImage
		self.__previewImage = loadedImage
		self.__updateTkinterImage()
		
	#saves the current pillow image
	def __saveImage(self):
		self.__mainImage = self.__previewImage
		self.__updateTkinterImage()
		self.__mainImage.save(self.__saveEntry.get())
		
	#applys the changes made to the preveiw image to the main image
	def __applyChanges(self):
		self.__mainImage = self.__previewImage
		self.__updateTkinterImage()
	
	#discards the changes made to the preview image and reverts to the main image
	def __discardChanges(self):
		self.__previewImage = self.__mainImage
		self.__updateTkinterImage()
	
	#updates the image displayed in the gui
	def __updateTkinterImage(self):
		self.__tkinterImage = ImageTk.PhotoImage(self.__previewImage)
		self.__imageCanvas.create_image(0,0 , image = self.__tkinterImage, anchor = "nw")
		self.__imageCanvas.config(scrollregion = self.__imageCanvas.bbox(tkinter.ALL))
		
	#applies a basic filter to the object passed in
	def __basicFilter(self, imageObject, filterString = "none"):
		#initializes the base parameters of the returnImage object based on the selcted filter
		if filterString == "Greyscale":
			returnImage = Image.new("L", imageObject.size)
		elif filterString == "Shrink":
			returnImage = Image.new("RGB", (int(round(imageObject.size[0]/2)), int(round(imageObject.size[1]/2))))
		elif filterString == "Expand":
			returnImage = Image.new("RGB", (imageObject.size[0]*2, imageObject.size[1]*2))
		elif filterString == "Rotate":
			returnImage = Image.new("RGB", (imageObject.size[1], imageObject.size[0]))
		else:
			returnImage = Image.new("RGB", imageObject.size)
			
		#applies filter and returns the modified (or for none unmodified) image object
		if filterString == "None":
			returnImage = imageObject
		if filterString == "Sunset":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					if RGBList[0] <= 62:
						RGBList = [int(RGBList[0] * 1.15), RGBList[1], int(RGBList[2] * 0.9)]
					elif RGBList[0] > 62 and RGBList[0] < 192:
						RGBList = [int(RGBList[0] * 1.2), RGBList[1], int(RGBList[2] * 0.85)]
					else:
						RGBList = [int(RGBList[0] * 1.16), RGBList[1], int(RGBList[2] * 0.5)]
					for i in range(len(RGBList)):
						if RGBList[i] > 255:
							RGBList[i] = 255
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Negative":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					for i in range(len(RGBList)):
						RGBList[i] = 255 - RGBList[i]
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Smooth":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					RGBAvg = 0
					for i in range(len(RGBList)):
						RGBAvg += RGBList[i]
					if RGBAvg/3 >= 125:
						for i in range(len(RGBList)):
							RGBList[i] = int(RGBList[i]*0.95)
							if RGBList[i] < 0:
								RGBList[i] = 0
					elif RGBAvg/3 < 125:
						for i in range(len(RGBList)):
							RGBList[i] = int(RGBList[i]*1.05)
							if RGBList[i] > 255:
								RGBList[i] = 255
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Contrast":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					RGBAvg = 0
					for i in range(len(RGBList)):
						RGBAvg += RGBList[i]
					if RGBAvg/3 >= 125:
						for i in range(len(RGBList)):
							RGBList[i] = int(RGBList[i]*1.05)
							if RGBList[i] > 255:
								RGBList[i] = 255
					elif RGBAvg/3 < 125:
						for i in range(len(RGBList)):
							RGBList[i] = int(RGBList[i]*0.95)
							if RGBList[i] < 0:
								RGBList[i] = 0
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Night Vision":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					RGBAvg = 0
					for i in range(len(RGBList)):
						RGBAvg += RGBList[i]
					RGBList[0] = 0
					RGBList[1] = int(RGBAvg/3)
					RGBList[2] = 0
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Brighten":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					for i in range(len(RGBList)):
						RGBList[i] = int(RGBList[i]*1.05)
						if RGBList[i] > 255:
							RGBList[i] = 255;
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Darken":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					for i in range(len(RGBList)):
						RGBList[i] = int(RGBList[i]*0.95)
						if RGBList[i] < 0:
							RGBList[i] = 0;
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Greyscale":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					RGBTotal = 0
					for i in range(len(RGBList)):
						RGBTotal += RGBList[i]
					returnImage.putpixel((x, y), int(RGBTotal/3))
		elif filterString == "Shrink":
			for x in range(0, imageObject.size[0] - 1, 2):
				for y in range(0, imageObject.size[1] - 1, 2):
					RGBList = list(imageObject.getpixel((x, y)))
					returnImage.putpixel((x//2, y//2), tuple(RGBList))
		elif filterString == "Expand":
			for x in range(0, imageObject.size[0]*2):
				for y in range(0, imageObject.size[1]*2):
					RGBList = list(imageObject.getpixel((x//2, y//2)))
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Rotate":
			for x in range(0, imageObject.size[0]):
				for y in range(0, imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					returnImage.putpixel((y, x), tuple(RGBList))
		self.__previewImage = returnImage
		self.__updateTkinterImage()
	
	#unlocks and updates variable slots
	def __modifyFilter(self, filterString = "None"):
		if filterString == "None":
			self.__variable1FilterEntryLabelStringVar.set("")
			self.__variable2FilterEntryLabelStringVar.set("")
			self.__variable3FilterEntryLabelStringVar.set("")
			self.__variableFilterButton.configure(state = "disabled")
			
			self.__loadLabelFrame.pack_forget()
			self.__loadEntryFrame.pack_forget()
			self.__saveLabelFrame.pack_forget()
			self.__saveEntryFrame.pack_forget()
			self.__basicFilterLabelFrame.pack_forget()
			self.__basicFilterOptionsFrame.pack_forget()
			self.__variableFilterLabelFrame.pack_forget()
			self.__variableFilterOptionsFrame.pack_forget()
			self.__variableFilterEntryFrame.pack_forget()
			self.__mouseFilterInstructionsFrame.pack_forget()
			self.__mouseFilterOptionsFrame.pack_forget()
			self.__changesButtonLabelFrame.pack_forget()
			self.__changesButtonFrame.pack_forget()
			
			self.__loadLabelFrame.pack()
			self.__loadEntryFrame.pack(pady = 4)
			self.__saveLabelFrame.pack()
			self.__saveEntryFrame.pack(pady = 4)
			self.__basicFilterLabelFrame.pack()
			self.__basicFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterLabelFrame.pack()
			self.__variableFilterOptionsFrame.pack(pady = 4)
			self.__mouseFilterInstructionsFrame.pack()
			self.__mouseFilterOptionsFrame.pack(pady = 4)
			self.__changesButtonLabelFrame.pack()
			self.__changesButtonFrame.pack(pady =  4)
			
		elif filterString == "Brightness Multiplier":
			self.__variable1FilterEntryLabelStringVar.set("Enter Color Intensity Multiplier")
			self.__variable2FilterEntryLabelStringVar.set("")
			self.__variable3FilterEntryLabelStringVar.set("")
			self.__variable1FilterEntry.delete(0, "end")
			self.__variable1FilterEntry.insert(0, "1")
			self.__variableFilterButton.configure(state = "normal")
			
			self.__lineOneFrame.pack_forget()
			self.__lineTwoFrame.pack_forget()
			self.__lineThreeFrame.pack_forget()
			
			self.__loadLabelFrame.pack_forget()
			self.__loadEntryFrame.pack_forget()
			self.__saveLabelFrame.pack_forget()
			self.__saveEntryFrame.pack_forget()
			self.__basicFilterLabelFrame.pack_forget()
			self.__basicFilterOptionsFrame.pack_forget()
			self.__variableFilterLabelFrame.pack_forget()
			self.__variableFilterOptionsFrame.pack_forget()
			self.__variableFilterEntryFrame.pack_forget()
			self.__mouseFilterInstructionsFrame.pack_forget()
			self.__mouseFilterOptionsFrame.pack_forget()
			self.__changesButtonLabelFrame.pack_forget()
			self.__changesButtonFrame.pack_forget()
			
			self.__loadLabelFrame.pack()
			self.__loadEntryFrame.pack(pady = 4)
			self.__saveLabelFrame.pack()
			self.__saveEntryFrame.pack(pady = 4)
			self.__basicFilterLabelFrame.pack()
			self.__basicFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterLabelFrame.pack()
			self.__variableFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterEntryFrame.pack(pady = 2)
			self.__mouseFilterInstructionsFrame.pack()
			self.__mouseFilterOptionsFrame.pack(pady = 4)
			self.__changesButtonLabelFrame.pack()
			self.__changesButtonFrame.pack(pady =  4)
			
			self.__lineOneFrame.pack(pady = 2)
			
		elif filterString == "RGB Multiplier":
			self.__variable1FilterEntryLabelStringVar.set("Enter Red Intensity Multiplier: ")
			self.__variable2FilterEntryLabelStringVar.set("Enter Green Intensity Multiplier: ")
			self.__variable3FilterEntryLabelStringVar.set("Enter Blue Intensity Multiplier: ")
			self.__variable1FilterEntry.delete(0, "end")
			self.__variable1FilterEntry.insert(0, "1")
			self.__variable2FilterEntry.delete(0, "end")
			self.__variable2FilterEntry.insert(0, "1")
			self.__variable3FilterEntry.delete(0, "end")
			self.__variable3FilterEntry.insert(0, "1")
			self.__variableFilterButton.configure(state = "normal")
			
			self.__lineOneFrame.pack_forget()
			self.__lineTwoFrame.pack_forget()
			self.__lineThreeFrame.pack_forget()
			
			self.__loadLabelFrame.pack_forget()
			self.__loadEntryFrame.pack_forget()
			self.__saveLabelFrame.pack_forget()
			self.__saveEntryFrame.pack_forget()
			self.__basicFilterLabelFrame.pack_forget()
			self.__basicFilterOptionsFrame.pack_forget()
			self.__variableFilterLabelFrame.pack_forget()
			self.__variableFilterOptionsFrame.pack_forget()
			self.__variableFilterEntryFrame.pack_forget()
			self.__mouseFilterInstructionsFrame.pack_forget()
			self.__mouseFilterOptionsFrame.pack_forget()
			self.__changesButtonLabelFrame.pack_forget()
			self.__changesButtonFrame.pack_forget()
			
			self.__loadLabelFrame.pack()
			self.__loadEntryFrame.pack(pady = 4)
			self.__saveLabelFrame.pack()
			self.__saveEntryFrame.pack(pady = 4)
			self.__basicFilterLabelFrame.pack()
			self.__basicFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterLabelFrame.pack()
			self.__variableFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterEntryFrame.pack(pady = 2)
			self.__mouseFilterInstructionsFrame.pack()
			self.__mouseFilterOptionsFrame.pack(pady = 4)
			self.__changesButtonLabelFrame.pack()
			self.__changesButtonFrame.pack(pady =  4)
			
			self.__lineOneFrame.pack(pady = 2)
			self.__lineTwoFrame.pack(pady = 2)
			self.__lineThreeFrame.pack(pady = 2)
		elif filterString == "Accent Multiplier":
			self.__variable1FilterEntryLabelStringVar.set("Enter Color Accent Multiplier: ")
			self.__variable2FilterEntryLabelStringVar.set("")
			self.__variable3FilterEntryLabelStringVar.set("")
			self.__variable1FilterEntry.delete(0, "end")
			self.__variable1FilterEntry.insert(0, "1")
			self.__variableFilterButton.configure(state = "normal")
			
			self.__lineOneFrame.pack_forget()
			self.__lineTwoFrame.pack_forget()
			self.__lineThreeFrame.pack_forget()
			
			self.__loadLabelFrame.pack_forget()
			self.__loadEntryFrame.pack_forget()
			self.__saveLabelFrame.pack_forget()
			self.__saveEntryFrame.pack_forget()
			self.__basicFilterLabelFrame.pack_forget()
			self.__basicFilterOptionsFrame.pack_forget()
			self.__variableFilterLabelFrame.pack_forget()
			self.__variableFilterOptionsFrame.pack_forget()
			self.__variableFilterEntryFrame.pack_forget()
			self.__mouseFilterInstructionsFrame.pack_forget()
			self.__mouseFilterOptionsFrame.pack_forget()
			self.__changesButtonLabelFrame.pack_forget()
			self.__changesButtonFrame.pack_forget()
			
			self.__loadLabelFrame.pack()
			self.__loadEntryFrame.pack(pady = 4)
			self.__saveLabelFrame.pack()
			self.__saveEntryFrame.pack(pady = 4)
			self.__basicFilterLabelFrame.pack()
			self.__basicFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterLabelFrame.pack()
			self.__variableFilterOptionsFrame.pack(pady = 4)
			self.__variableFilterEntryFrame.pack(pady = 2)
			self.__mouseFilterInstructionsFrame.pack()
			self.__mouseFilterOptionsFrame.pack(pady = 4)
			self.__changesButtonLabelFrame.pack()
			self.__changesButtonFrame.pack(pady =  4)
			
			self.__lineOneFrame.pack(pady = 2)
	
	#applies a variable filter to the object passed in
	def __variableFilter(self, imageObject, filterString = "none"):
		#grabs the values of the three 
		var1Value = self.__variable1FilterEntry.get()
		var2Value = self.__variable2FilterEntry.get()
		var3Value = self.__variable3FilterEntry.get()
		
		#new return image object
		returnImage = Image.new("RGB", imageObject.size)
			
		#applies filter and returns the modified (or for none unmodified) image object
		if filterString == "None":
			returnImage = imageObject
		elif filterString == "Brightness Multiplier":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					for i in range(len(RGBList)):
						RGBList[i] = int(RGBList[i]*float(var1Value))
						if RGBList[i] > 255:
							RGBList[i] = 255
						elif RGBList[i] < 0:
							RGBList[i] = 0
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "RGB Multiplier":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					RGBList[0] = int(RGBList[0]*float(var1Value))
					RGBList[1] = int(RGBList[1]*float(var2Value))
					RGBList[2] = int(RGBList[2]*float(var3Value))
					for i in range(len(RGBList)):
						if RGBList[i] > 255:
							RGBList[i] = 255
						elif RGBList[i] < 0:
							RGBList[i] = 0
					returnImage.putpixel((x, y), tuple(RGBList))
		elif filterString == "Accent Multiplier":
			for x in range(imageObject.size[0]):
				for y in range(imageObject.size[1]):
					RGBList = list(imageObject.getpixel((x, y)))
					if not(RGBList[0] == RGBList[1] == RGBList[2]):
						highestValue = RGBList[0]
						if RGBList[1] > highestValue:
							highestValue = RGBList[1]
						if RGBList[2] > highestValue:
							highestValue = RGBList[2]
						if RGBList[0] >= highestValue:
							RGBList[0] = int(RGBList[0]*float(var1Value))
						else:
							RGBList[0] = int(RGBList[0]*(1 - (float(var1Value) - 1)))
						if RGBList[1] >= highestValue:
							RGBList[1] = int(RGBList[1]*float(var1Value))
						else:
							RGBList[1] = int(RGBList[1]*(1 - (float(var1Value) - 1)))
						if RGBList[2] >= highestValue:
							RGBList[2] = int(RGBList[2]*float(var1Value))
						else:
							RGBList[2] = int(RGBList[2]*(1 - (float(var1Value) - 1)))
					for i in range(len(RGBList)):
						if RGBList[i] > 255:
							RGBList[i] = 255
						elif RGBList[i] < 0:
							RGBList[i] = 0
					returnImage.putpixel((x, y), tuple(RGBList))
		self.__previewImage = returnImage
		self.__updateTkinterImage()
		self.__modifyFilter()
		self.__variableFilterButton.configure(state = "disabled")
		
	
	#allows the user to select the area of the mouse filter
	def __selectArea(self, shapeString = "None"):
		if shapeString == "None":
			self.__mouseFilterInstructionStringVar.set("Select Variable Mouse Filter and Shape and Follow Instructions about Specific Filters: ")
			self.__numMousePositions = 0
			self.__mouseCoordsList = list()
			self.__mouseFilterSelected = False
		elif shapeString == "Square":
			self.__mouseFilterInstructionStringVar.set("Click on The  Top Left and Bottom Right Corner of The Filter Area: ")
			self.__numMousePositions = 2
			self.__mouseCoordsList = list()
			self.__mouseFilterSelected = True
			self.__mouseFilterButton.configure(state = "disabled")
		elif shapeString == "Crop":
			self.__mouseFilterInstructionStringVar.set("Click on The  Top Left and Bottom Right Corner of The Cropping Area: ")
			self.__numMousePositions = 2
			self.__mouseCoordsList = list()
			self.__mouseFilterSelected = True
			self.__mouseFilterButton.configure(state = "disabled")
		elif shapeString == "Circle":
			self.__mouseFilterInstructionStringVar.set("Click on First to Set the Origin, Then Second to Set The Radius: ")
			self.__numMousePositions = 2
			self.__mouseCoordsList = list()
			self.__mouseFilterSelected = True
			self.__mouseFilterButton.configure(state = "disabled")
	
	#distance between two points
	def __distance(self, pointOne, pointTwo):
		return math.sqrt((pointOne[0] - pointTwo[0])**2 + (pointOne[1] - pointTwo[1])**2)
	
	#applies a variable filter to the object passed in
	def __mouseFilter(self, imageObject, filterString = "none", shapeString = "None"):
		if shapeString == "Crop":
			rightMouseXCoord = int(self.__mouseCoordsList[1][0])
			if rightMouseXCoord > imageObject.size[0]:
				rightMouseXCoord = imageObject.size[0]
			bottomMouseYCoord = int(self.__mouseCoordsList[1][1])
			if bottomMouseYCoord > imageObject.size[1]:
				bottomMouseYCoord = imageObject.size[1]
			croppedImageSize = [int(rightMouseXCoord - self.__mouseCoordsList[0][0]), int(bottomMouseYCoord - self.__mouseCoordsList[0][1])]
			
			returnImage = Image.new("RGB", tuple(croppedImageSize))
			
			for x in range(croppedImageSize[0]):
				for y in range(croppedImageSize[1]):
					RGBList = list(imageObject.getpixel((x + self.__mouseCoordsList[0][0], y + self.__mouseCoordsList[0][1])))
					returnImage.putpixel((x, y), tuple(RGBList))
		else:
			if shapeString == "Square":
				rightMouseXCoord = int(self.__mouseCoordsList[1][0])
				bottomMouseYCoord = int(self.__mouseCoordsList[1][1])
			if shapeString == "Circle":
				circleOrigin = self.__mouseCoordsList[0]
				circleRadius = self.__distance(circleOrigin, self.__mouseCoordsList[1])
			
			returnImage = Image.new("RGB", imageObject.size)
			
			if filterString == "Remove":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								returnImage.putpixel((x, y), (0, 0, 0))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								returnImage.putpixel((x, y), (0, 0, 0))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Sunset":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								if RGBList[0] <= 62:
									RGBList = [int(RGBList[0] * 1.1), RGBList[1], int(RGBList[2] * 0.9)]
								elif RGBList[0] > 62 and RGBList[0] < 192:
									RGBList = [int(RGBList[0] * 1.15), RGBList[1], int(RGBList[2] * 0.85)]
								else:
									RGBList = [int(RGBList[0] * 1.08), RGBList[1], int(RGBList[2] * 0.5)]
								for i in range(len(RGBList)):
									if RGBList[i] > 255:
										RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								if RGBList[0] <= 62:
									RGBList = [int(RGBList[0] * 1.1), RGBList[1], int(RGBList[2] * 0.9)]
								elif RGBList[0] > 62 and RGBList[0] < 192:
									RGBList = [int(RGBList[0] * 1.15), RGBList[1], int(RGBList[2] * 0.85)]
								else:
									RGBList = [int(RGBList[0] * 1.08), RGBList[1], int(RGBList[2] * 0.5)]
								for i in range(len(RGBList)):
									if RGBList[i] > 255:
										RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Negative":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = 255 - RGBList[i]
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = 255 - RGBList[i]
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Smooth":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								if RGBAvg/3 >= 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*0.95)
										if RGBList[i] < 0:
											RGBList[i] = 0
								elif RGBAvg/3 < 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*1.05)
										if RGBList[i] > 255:
											RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								if RGBAvg/3 >= 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*0.95)
										if RGBList[i] < 0:
											RGBList[i] = 0
								elif RGBAvg/3 < 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*1.05)
										if RGBList[i] > 255:
											RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Contrast":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								if RGBAvg/3 >= 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*0.95)
										if RGBList[i] < 0:
											RGBList[i] = 0
								elif RGBAvg/3 < 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*1.05)
										if RGBList[i] > 255:
											RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								if RGBAvg/3 >= 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*0.95)
										if RGBList[i] < 0:
											RGBList[i] = 0
								elif RGBAvg/3 < 125:
									for i in range(len(RGBList)):
										RGBList[i] = int(RGBList[i]*1.05)
										if RGBList[i] > 255:
											RGBList[i] = 255
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Night Vision":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								RGBList[0] = 0
								RGBList[1] = int(RGBAvg/3)
								RGBList[2] = 0
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								RGBAvg = 0
								for i in range(len(RGBList)):
									RGBAvg += RGBList[i]
								RGBList[0] = 0
								RGBList[1] = int(RGBAvg/3)
								RGBList[2] = 0
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Brighten":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = int(RGBList[i]*1.05)
									if RGBList[i] > 255:
										RGBList[i] = 255;
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = int(RGBList[i]*1.05)
									if RGBList[i] > 255:
										RGBList[i] = 255;
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
			elif filterString == "Darken":
				for x in range(imageObject.size[0]):
					for y in range(imageObject.size[1]):
						if shapeString == "Square":
							if (x >= int(self.__mouseCoordsList[0][0]) and x <= rightMouseXCoord) and (y >= int(self.__mouseCoordsList[0][1]) and y <= bottomMouseYCoord):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = int(RGBList[i]*0.95)
									if RGBList[i] < 0:
										RGBList[i] = 0;
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
						elif shapeString == "Circle":
							if (self.__distance(circleOrigin, [x, y]) <= circleRadius):
								RGBList = list(imageObject.getpixel((x, y)))
								for i in range(len(RGBList)):
									RGBList[i] = int(RGBList[i]*0.95)
									if RGBList[i] < 0:
										RGBList[i] = 0;
								returnImage.putpixel((x, y), tuple(RGBList))
							else:
								RGBList = list(imageObject.getpixel((x, y)))
								returnImage.putpixel((x, y), tuple(RGBList))
		self.__previewImage = returnImage
		self.__updateTkinterImage()
		self.__mouseFilterInstructionStringVar.set("Select Variable Mouse Filter and Shape and Follow Instructions about Specific Filters: ")
		self.__numMousePositions = 0
		self.__mouseCoordsList = list()
		self.__mouseFilterSelected = False
		self.__mouseFilterButton.configure(state = "normal")
	
if __name__ == "__main__":
	inputWindow()