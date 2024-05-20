import tkinter as tk
import tkinter.filedialog as tkFileDialog
import PIL.Image as Image
import PIL.ImageTk as ImageTk

class BasicGui:

  def __init__(self):
      self.mainWin=tk.Tk()
      self.mainWin.title("Photo Editor")
      self.titleLabel=tk.Label(self.mainWin, text="Photo Editor",
                          font="Times 32 bold",
                          bg="lavender",
                          relief=tk.RIDGE,
                          width=20)
      self.titleLabel.grid(row=0, column=0, columnspan=3)
      self.optionsLabel = tk.Label(self.mainWin, text="Click on a button or enter an INTEGER below",
                            font="Times 30 bold",
                            bg="lavender",
                            relief=tk.RIDGE)
      self.optionsLabel.grid(row=1, column=0, columnspan=4)
      self.darkenLabel = tk.Label(self.mainWin, text="Darken",
                           font="Times 28 bold",
                           bg="lavender",
                           relief=tk.RIDGE,
                           width=10)
      self.darkenLabel.grid(row=2, column=0)
      self.lightenLabel = tk.Label(self.mainWin, text="Lighten",
                             font="Times 28 bold",
                             bg="lavender",
                             relief=tk.RIDGE,
                             width=10)
      self.lightenLabel.grid(row=3, column=0)
      self.saturationLabel = tk.Label(self.mainWin, text="Saturation",
                              font="Times 28 bold",
                              bg="lavender",
                              relief=tk.RIDGE,
                              width=10)
      self.saturationLabel.grid(row=4, column=0)
      self.grayButton = tk.Button(self.mainWin, text="Grayscale",
                                  font="Times 28 bold",
                                  bg="lavender",
                                  relief=tk.RIDGE,
                                  width=10, command=self.grayscale)
      self.grayButton.grid(row=3, column=2)
      self.negativeButton = tk.Button(self.mainWin, text="Negative",
                                  font="Times 28 bold",
                                  bg="lavender",
                                  relief=tk.RIDGE,
                                  width=10, command = self.negative)
      self.negativeButton.grid(row=2, column=2)
      self.darkenEntry = tk.Entry(self.mainWin,
                              bg="lavender",
                              font="Times 20",
                              width=23, justify=tk.CENTER)
      self.darkenEntry.grid(row=2, column=1)
      self.darkenEntry.insert(5,"Enter an integer from 1 to 10")
      self.darkenEntry.bind("<Return>", self.darken)
      self.lightenEntry = tk.Entry(self.mainWin,
                                   bg="lavender",
                                   font="Times 20",
                                   width=23, justify=tk.CENTER)
      self.lightenEntry.grid(row=3, column=1)
      self.lightenEntry.insert(5, "Enter an integer from 1 to 10")
      self.lightenEntry.bind("<Return>", self.lighten)
      self.saturationEntry = tk.Entry(self.mainWin,
                                  bg="lavender",
                                  font="Times 20",
                                  width=23, justify=tk.CENTER)
      self.saturationEntry.grid(row=4, column=1)
      self.saturationEntry.insert(5, "Enter an integer from 1 to 10")
      self.saturationEntry.bind("<Return>", self.saturate)
      self.croppedLabel = tk.Label(self.mainWin, text="Cropping",
                                      font="Times 28 bold",
                                      bg="lavender",
                                      relief=tk.RIDGE,
                                      width=10)
      self.croppedLabel.grid(row=5, column=0)
      self.rightRotButton = tk.Button(self.mainWin, text="Right Rotate",
                                  font="Times 28 bold",
                                  bg="lavender",
                                  relief=tk.RIDGE,
                                  width=10, command=self.rightRot)
      self.rightRotButton.grid(row=5, column=2)
      self.leftRotButton = tk.Button(self.mainWin, text="Left Rotate",
                                      font="Times 28 bold",
                                      bg="lavender",
                                      relief=tk.RIDGE,
                                      width=10, command=self.leftRot)
      self.leftRotButton.grid(row=4, column=2)
      self.croppedEntry = tk.Entry(self.mainWin,
                                      bg="lavender",
                                      font="Times 20",
                                      width=23, justify=tk.CENTER)
      self.croppedEntry.grid(row=5, column=1)
      self.croppedEntry.insert(5, "Enter square width")
      self.croppedEntry.bind("<Return>", self.crop)
      self.pictureLabel = tk.Label(self.mainWin,
                                bg="lavender",
                                relief= tk.RIDGE, bd=5, image = None)
      self.pictureLabel.grid(row=1, column=4, rowspan=6)
      self.chooseFileButton = tk.Button(self.mainWin, text="Choose File",
                                     font="Times 28 bold",
                                     bg="lavender",
                                     relief=tk.RIDGE, command = self.fileOpen)
      self.chooseFileButton.grid(row=0, column=4)
      self.result = None
      self.savePictureButton = tk.Button(self.mainWin, text="Save picture!",
                                        font="Times 28 bold",
                                        bg="lavender",
                                        relief=tk.RIDGE,
                                        width=40, command=self.saveImage)
      self.savePictureButton.grid(row=6, column=0, columnspan=3)

  def run(self):
      self.mainWin.mainloop()
  def fileOpen(self):
      self.result = tkFileDialog.askopenfilename()
      self.imageImg = Image.open(self.result)
      self.img = ImageTk.PhotoImage(self.imageImg)
      self.pictureLabel["image"] = self.img

  def darken(self, event):
      pic = Image.open(self.result)
      factor=self.darkenEntry.get()
      if factor.isdigit():
          factor = int(factor)
          if factor > 0:
              factor = factor
          else:
              factor = 1
      else:
          factor = 1
      self.newPic = pic.copy()
      width, height = self.newPic.size
      for x in range(width):
          for y in range(height):
              r, g, b = self.newPic.getpixel((x, y))
              newRed = r // factor
              newGreen = g // factor
              newBlue = b // factor
              self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img #If i want changes to be on top of eachother, would I add self.result=filepath of this (but it hasn't been saved so it doesn't have a filepath?)

  def lighten(self, event):
      pic = Image.open(self.result)
      factor=self.lightenEntry.get()
      if factor.isdigit():
          if factor!=0:
            factor=int(factor)
          else:
              factor=1
      else:
          factor = 1
      self.newPic = pic.copy()
      width, height = self.newPic.size
      for x in range(width):
          for y in range(height):
              r, g, b = self.newPic.getpixel((x, y))
              newRed = r * factor
              newGreen = g * factor
              newBlue = b * factor
              self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def negative(self):
      pic = Image.open(self.result)
      self.newPic = pic.copy()
      width, height = self.newPic.size
      for x in range(width):
          for y in range(height):
              r, g, b = self.newPic.getpixel((x, y))
              newRed = 255- r
              newGreen = 255-g
              newBlue = 255-b
              self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def grayscale(self):
      pic = Image.open(self.result)
      self.newPic = pic.copy()
      width, height = self.newPic.size
      for x in range(width):
          for y in range(height):
              r, g, b = self.newPic.getpixel((x, y))
              lumin=(r+g+b)//3
              self.newPic.putpixel((x, y), (lumin, lumin, lumin))
          self.img = ImageTk.PhotoImage(self.newPic)
          self.pictureLabel["image"] = self.img

  def rightRot(self):
      pic = Image.open(self.result)
      width, height = pic.size
      self.newPic = Image.new(pic.mode, (height, width))
      for x in range(width):
          for y in range(height):
              r, g, b = pic.getpixel((x, y))
              self.newPic.putpixel((y,width-x-1), (r,g,b))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def leftRot(self):
      pic = Image.open(self.result)
      width, height = pic.size
      self.newPic = Image.new(pic.mode, (height, width))
      for x in range(width):
          for y in range(height):
              r, g, b = pic.getpixel((x, y))
              self.newPic.putpixel((height-y-1, x), (r, g, b))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def saturate(self, event):
      pic = Image.open(self.result)
      factor=self.saturationEntry.get()
      if factor.isdigit():
          if factor!=0:
            factor=int(factor)
          else:
              factor=1
      else:
          factor = 1
      self.newPic = pic.copy()
      width, height = self.newPic.size
      for x in range(width):
          for y in range(height):
              r, g, b = self.newPic.getpixel((x, y))
              if r > b and r > g:
                  newRed = r + factor * 10
                  newGreen = g - factor * 10
                  newBlue = b - factor * 10
                  self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
              if g > r and g > b:
                  newRed = r - factor * 10
                  newGreen = g + factor * 10
                  newBlue = b - factor * 10
                  self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
              if b > r and b > g:
                  newRed = r - factor * 10
                  newGreen = g - factor * 10
                  newBlue = b + factor * 10
                  self.newPic.putpixel((x, y), (newRed, newGreen, newBlue))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def crop(self, event):
      pic = Image.open(self.result)
      width, height = pic.size
      factor = self.croppedEntry.get()
      if self.isNumber(factor):
          factor= round(float(factor))
      elif factor < 0:
          factor = 1
      else:
          factor = 1
      left=int(max(0, width//2 - factor//2))
      right=int(min(width-1, width//2 + factor//2))
      top=int(max(0, height//2 - factor//2))
      bottom=int(min(height-1, height//2 + factor//2))
      self.newPic = Image.new(pic.mode, (right-left, bottom-top))
      for x in range(left, right):
          for y in range(top, bottom):
              r, g, b = pic.getpixel((x, y))
              self.newPic.putpixel((x-left, y-top), (r, g, b))
      self.img = ImageTk.PhotoImage(self.newPic)
      self.pictureLabel["image"] = self.img

  def isNumber(self, myString):
        try:
            float(myString)
            return True
        except ValueError:
            return False

  def saveImage(self):
      self.newPic.save("editedImage.jpg")



myGui=BasicGui()
myGui.run()

