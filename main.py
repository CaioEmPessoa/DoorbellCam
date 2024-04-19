import customtkinter as ctk
import cv2 
from PIL import Image, ImageTk 

class VideoRecord():
    def __init__(self):
        self.device_id = 0
        self.width, self.height = 500, 500

        self.capture = cv2.VideoCapture(self.device_id)
        
        # video height and width 
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width) 
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def record_image(self):
        return()
        # Capture the video frame by frame 
        _, frame = self.capture.read() 
    
        # Convert image from one color space to other 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image)
        
        return photo_image


class Root(ctk.CTk):
    def __init__(self, video_record):
        super().__init__()

        # initiating classes and functions.
        self.video_record = video_record

        self.root_elements()

        #self.geometry('500x700')

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def show_record(self):
    
        recorded_image = self.video_record.record_image()

        self.cam_label.photo_image = recorded_image

        # Configure image in the label 
        self.cam_label.configure(image=recorded_image) 
    
        # Repeat the same process after every 10 seconds 
        self.cam_label.after(10, self.show_record)

    def start_connection(self):
        self.loading_image = ImageTk.PhotoImage(Image.open("./img/conectando.png"))
        self.cam_label.configure(image=self.loading_image)
        self.after(1000, self.show_record)

    def root_elements(self):
        self.cam_label = ctk.CTkLabel(self, text="", width=500, height=500) 
        self.cam_label.grid(row=0, column=0, sticky="N", padx=10, pady=10,
                               columnspan=3)

        self.waiting_image = ImageTk.PhotoImage(Image.open("./img/aguardando.png"))
        self.cam_label.configure(image=self.waiting_image)

        self.phone_entry = ctk.CTkEntry(self, width=420, height=40, placeholder_text="",
                                   font=("Consolas", 20))
        self.phone_entry.grid(row=1, column=0, pady=20, columnspan=3)


        aptos = ['101', '102', '103', '201', '202', '203', '301', '302', '303']

        skip_row = 2
        btn_height, btn_width = 60, 90
        for numb in range(1, 10):
            button = ctk.CTkButton(master=self, text=aptos[numb-1], height=btn_height, width=btn_width,
                                   font=("Consolas", 30),
                                   command=lambda numb=numb: self.phone_entry.insert("end", numb))
            button.grid(row=(numb-1)//3 + skip_row, column=(numb-1)%3, padx=10, pady=10)

        zero_btn = ctk.CTkButton(master=self, text="000", height=btn_height, width=btn_width,
                                 font=("Consolas", 30),
                                 command=lambda numb=0: self.phone_entry.insert("end", numb))
        zero_btn.grid(row=3+skip_row, column=1, padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self, text="<---", font=("Consolas", 30),
                                            height=btn_height, width=btn_width-10, fg_color="#0561ad",
                                            command= lambda: self.phone_entry.delete(len(self.phone_entry.get())-1))
        self.delete_button.grid(row=3+skip_row, column=0, pady=10)

        self.confirm_button = ctk.CTkButton(self, text="--->", font=("Consolas", 30),
                                            height=btn_height, width=btn_width-10, fg_color="#0561ad",
                                            command=self.start_connection)
        self.confirm_button.grid(row=3+skip_row, column=2, pady=10)



class Container():
    def __init__(self):

        self.video_record = VideoRecord()

        self.root = Root(self.video_record)
        self.root.mainloop()


if __name__ == "__main__":
    Container()