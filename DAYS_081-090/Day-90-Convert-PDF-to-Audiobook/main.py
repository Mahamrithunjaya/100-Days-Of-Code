import pyttsx3 as tts
from PyPDF2 import PdfReader
import docx2txt
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

MIDNIGHTBLUE = "#191970"
SEAGREEN = "#2E8B57"
LIGHTMINT = "#569DAA"


# Reading a Word file
def read_word_files(f_name):
    return docx2txt.process(f_name)


# Reading a PDF file
def read_pdf_files(f_name):
    file_obj = PdfReader(f_name)
    return "".join([file_obj.pages[i].extract_text() for i in range(len(file_obj.pages))])


# Reading a simple text file
def read_text_files(f_name):
    with open(f_name) as file:
        return file.read()


def file_upload():
    filetypes = [('Choose File Type', '*.pdf *.docx *.doc *.txt')]
    file_name = askopenfilename(filetypes=filetypes)
    user_file_entry.insert(0, file_name)


def convert_text_to_audio():
    if not user_file_entry.get():
        return
    file_name = user_file_entry.get()
    if file_name[-3:].lower() == "pdf":
        file_text = read_pdf_files(file_name)
    elif file_name[-3:].lower() == "txt":
        file_text = read_text_files(file_name)
    elif file_name[-3:].lower() == "doc":
        file_text = read_word_files(file_name)
    elif file_name[-4:].lower() == "docx":
        file_text = read_word_files(file_name)
    else:
        messagebox.showerror(title="Wrong File Chosen", message="Please Choose a valid File")
        return
    file_name = file_name.split('/')[-1]
    convert_text_to_audio_using_pyttsx3_tts(file_text, file_name)
    messagebox.showinfo(title="Successful", message=f"Your text file \"{file_name}\" has been convert to Audio!!")
    user_file_entry.delete(0, END)
    user_file_entry.focus()
    window.iconify()


def convert_text_to_audio_using_pyttsx3_tts(file_text, file_name):
    engine = tts.init()
    engine.save_to_file(file_text, f"{file_name.split('.')[0]}.mp3")
    engine.runAndWait()


# ********** GUI ********** #
window = Tk()
window.title("Text to Speech Converter")
window.geometry("623x420")
window.resizable(False, False)
canvas = Canvas(window, width=623, height=420)
canvas.config(bg=LIGHTMINT)
canvas.place(x=0, y=0)

label_text = Label(window, text="Upload your file here:", font=("Arial", 14), bg=LIGHTMINT)
label_text.place(x=100, y=165)

user_file_entry = Entry(width=38, font=("Arial", 14), )
user_file_entry.place(x=100, y=197)
user_file_entry.focus()

upload_photo_button = Button(window, text="Browse", width=10, height=1, font=("Arial", 18, "bold"),
                             background=SEAGREEN,
                             activebackground=SEAGREEN, activeforeground="white", foreground="white",
                             command=file_upload)
upload_photo_button.place(x=100, y=240)

convert_button = Button(window, text="Convert", width=10, height=1, font=("Arial", 18, "bold"),
                        background=MIDNIGHTBLUE,
                        activebackground=MIDNIGHTBLUE, activeforeground="white", foreground="white",
                        command=convert_text_to_audio)
convert_button.place(x=363, y=240)
window.bind('<Return>', convert_text_to_audio())

window.mainloop()
