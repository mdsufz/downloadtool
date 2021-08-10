### GUI for download tool
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from os import listdir
from os.path import join
from re import match
import download_sra as sra

class Application(Frame):
    
	def selectCsvFile(self):
		# get file 
		fname = askopenfilename(title='Select a CSV',filetypes=[("CSV", "*.csv")])
		# store globally
		self.csvFile = fname
		# truncate name if to long
		fnameShort = fname
		if len(fname) > 40:
			fnameShort = "..."+fname[-40:]
		# update text	
		self.textScript.configure(text=fnameShort)
		self.update()
		
	def selectOutFolder(self):
		# dir name
		outdir = askdirectory(title='Select folder for output')
		# store globally
		self.outFolder = outdir
		# truncate name if to long
		outdirShort = outdir
		if len(outdir) > 40:
			outdirShort = "..."+outdir[-40:]
		# update text
		self.textOutFolder.configure(text=outdirShort)
		self.update()

	def selectToolPath(self):
		# dir name
		tooldir = askdirectory(title='Select path to SRAtoolkit')
		# store globally
		self.toolPath = tooldir
		# truncate name if to long
		tooldirShort = tooldir
		if len(tooldir) > 40:
			tooldirShort = "..."+tooldir[-40:]
		# update text
		self.textOutTool.configure(text=tooldirShort)
		self.update()		
	
	# download and configure SRAtoolkit
	def installSRA(self):
		# ask for install path
		installdir = askdirectory(title='Select folder to install SRAtoolkit')

		# check if install path is give and install
		if(installdir == ''):
			messagebox.showinfo("No install path", "Please select a path to install the SRAtoolkit!")
		else:
            
			# download SRA
			sra.download_sratoolkit(installdir)

			# parse sratoolkit dirctory
			files = [f for f in listdir(installdir) if match(r'sratoolkit', f)]
			files = [f for f in files if not match(r'.*tar.gz', f)]
			files = [f for f in files if not match(r'.*zip', f)]
			path = join(installdir,files[0])

			# configure
			sra.config_sratoolkit(path)
			
			# store globally
			self.toolPath = installdir
			# truncate name if to long
			tooldirShort = installdir
			if len(installdir) > 40:
				tooldirShort = "..."+installdir[-40:]
			# update text
			self.textOutTool.configure(text=tooldirShort)
			self.update()
			# status
			messagebox.showinfo("Installation done", "SRAtoolkit downloaded and installed under the following path: "+installdir)

	def execScript(self):
		# check if integer input
		try:
			co = int(self.selCores.get())
			si = int(self.selSize.get())
			# check if cores < 1
			if co < 1:
				co = 1
		except:
			co = ''
			si = ''
			
		# check that everything is given (path and folders)
		if((self.csvFile == '') or (self.csvFile == 'No file selected') or (self.toolPath == '') or (self.toolPath == 'No path selected') or (self.outFolder == '') or (self.outFolder == 'No output folder selected') or (co =='') or (si == '')):
			if((self.csvFile == '') or (self.csvFile == 'No file selected')):
				messagebox.showinfo("No CSV file given", "Please select a CSV file!")
			if((self.toolPath == '') or (self.toolPath == 'No path selected')):
				messagebox.showinfo("No tool path", "Please select the path/location of the SRAtoolkit!")
			if((self.outFolder == '') or (self.outFolder == 'No output folder selected')):
				messagebox.showinfo("No output folder", "Please select a output folder!")
			if(co == '' or si == ''):
				messagebox.showinfo("No integer", "Please enter integer number for cores and file size!")
		else:		
			# close/destroy main window
			root.destroy()
			
            # identify sratoolkit sub-dircetory
			files = [f for f in listdir(self.toolPath) if match(r'sratoolkit', f)]
			files = [f for f in files if not match(r'.*tar.gz', f)]
			files = [f for f in files if not match(r'.*zip', f)]
			if len(files)>0:
				tool_path = join(self.toolPath,files[0])
			else:
				tool_path = self.toolPath

            # run download
			sra.download_samples(self.csvFile,self.outFolder,tool_path,str(co),str(si*1000000))

			# create new Tkinter and show message
			root2 = Tk()
			root2.withdraw()
			messagebox.showinfo("Data download","Data download completed. Please check console for status!")
			root2.destroy()

	def createWidgets(self):
		# create text 
		self.heading = Label(self,text="Download SRA metagenomes using exported CSV and SRAtoolkit")
		self.heading.pack(pady=5)
		
		# button and text for script selection
		self.csvFrame = Frame(self)
		self.csvFrame.pack(pady=5)
		self.selScript = Button(self.csvFrame,width=20)
		self.selScript["text"] = "Select CSV file"
		self.selScript["command"] = self.selectCsvFile
		self.selScript.pack({"side": "left"})
		self.csvFile = 'No file selected'
		self.textScript = Label(self.csvFrame,text=self.csvFile,width=40)
		self.textScript.pack({"side": "left"},padx=5)
	
		# button and text for output folder
		self.outFolderFrame = Frame(self)
		self.outFolderFrame.pack(pady=5)
		self.selOutFolder = Button(self.outFolderFrame,width=20)
		self.selOutFolder["text"] = "Select output folder"
		self.selOutFolder["command"] = self.selectOutFolder
		self.selOutFolder.pack({"side": "left"},padx=5)
		self.outFolder = 'No output folder selected'
		self.textOutFolder = Label(self.outFolderFrame,text=self.outFolder,width=40)
		self.textOutFolder.pack({"side": "left"},padx=5)

		# button and text for SRAtoolkit path
		self.outToolFrame = Frame(self)
		self.outToolFrame.pack(pady=5)
		self.selOutTool = Button(self.outToolFrame,width=20)
		self.selOutTool["text"] = "Select path to SRAtoolkit"
		self.selOutTool["command"] = self.selectToolPath
		self.selOutTool.pack({"side": "left"},padx=5)
		self.toolPath = 'No path selected'
		self.textOutTool = Label(self.outToolFrame,text=self.toolPath,width=40)
		self.textOutTool.pack({"side": "left"},padx=5)

		# entry to chose cores
		self.coresFrame = Frame(self)
		self.coresFrame.pack(pady=5)
		self.textCores = Label(self.coresFrame,text='[optional] CPU cores to use: ',width=30)
		self.textCores.pack({"side": "left"},padx=5)
		self.selCores = Entry(self.coresFrame,width=10)
		self.selCores.pack({"side": "left"},padx=55)
		self.cores = 2
		self.selCores.insert(0,self.cores)
		
		# entry max file size in GB
		self.maxSizeFrame = Frame(self)
		self.maxSizeFrame.pack(pady=5)
		self.textSize = Label(self.maxSizeFrame,text='[optional] Max files size in GB: ',width=30)
		self.textSize.pack({"side": "left"},padx=5)
		self.selSize = Entry(self.maxSizeFrame,width=10)
		self.selSize.pack({"side": "left"},padx=55)
		self.size = '20'
		self.selSize.insert(0,self.size)

		# run button 
		self.outputFrame = Frame(self)
		self.outputFrame.pack(pady=5)
		self.execButton = Button(self.outputFrame)
		self.execButton["text"] = "Start download"
		self.execButton["command"] = self.execScript
		self.execButton.pack(pady=5)

		# button to install SRAtoolkit
		self.outInstallFrame = Frame(self)
		self.outInstallFrame.pack(pady=5)
		self.selOutInstall = Button(self.outInstallFrame,width=30)
		self.selOutInstall["text"] = "Download and configure SRAtoolkit"
		self.selOutInstall["command"] = self.installSRA
		self.selOutInstall.pack({"side": "left"},padx=5)

		# quit button
		self.quitFrame = Frame(self)
		self.quitFrame.QUIT = Button(self)
		self.quitFrame.QUIT["text"] = "QUIT"
		self.quitFrame.QUIT["fg"]   = "red"
		self.quitFrame.QUIT["command"] =  self.quit
		self.quitFrame.QUIT.pack({"side": "left"},padx=5,pady=5)

	# main function	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()    
		self.createWidgets()
		
# initialize window		
root = Tk()
app = Application(master=root)
# define window title
app.master.title("Download tool")
# App icon (but not taken as exe image, sometimes shown in the task bar but not always)
#app.master.iconbitmap('seedling64px.ico')
# start app
app.mainloop()
