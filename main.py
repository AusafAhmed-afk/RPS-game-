import random
import customtkinter as ctk

youDict = {"R": 1, "P": -1, "S": 0}
reversedDict = {1: "Rock", -1: "Paper", 0: "Scissor"}

class RockPaperScissorsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors - Arcade Edition")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.configure(fg_color="#2a003f")  

        self.start_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.start_frame.pack(expand=True)

        title_label = ctk.CTkLabel(
            self.start_frame,
            text="🎮 Rock Paper Scissors 🎮",
            font=("Arial Black", 28),
            text_color="yellow"
        )
        title_label.pack(pady=40)

        start_btn = ctk.CTkButton(
            self.start_frame,
            text="▶ Start Game",
            text_color= "black",
            font=("Arial", 18, "bold"),
            fg_color="#39ff14",
            hover_color="#00cc00",
            command=self.start_game
        )
        start_btn.pack(pady=20)

        exit_btn = ctk.CTkButton(
            self.start_frame,
            text="❌ Exit",
            text_color= "black"  ,
            font=("Arial", 18, "bold"),
            fg_color="#ff3131",
            hover_color="#cc0000",
            command=self.destroy
        )
        exit_btn.pack(pady=20)

    def start_game(self):
        self.start_frame.pack_forget()
        self.show_game_frame()

    def show_game_frame(self):
        self.game_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.game_frame.pack(expand=True)

        self.result_label = ctk.CTkLabel(
            self.game_frame,
            text="Choose your move!",
            font=("Arial Black", 18),
            text_color="white"
        )
        self.result_label.pack(pady=20)

        button_frame = ctk.CTkFrame(self.game_frame, fg_color="transparent")
        button_frame.pack()

        rock_btn = ctk.CTkButton(button_frame, text="🪨 Rock", font=("Arial", 14, "bold"),
                                 fg_color="#4444ff", text_color="black" , hover_color="#0000cc",
                                 command=lambda: self.play_game("R"))
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = ctk.CTkButton(button_frame, text="📄 Paper", font=("Arial", 14, "bold"),
                                  fg_color="#44ff44", text_color="black" ,hover_color="#00cc00",
                                  command=lambda: self.play_game("P"))
        paper_btn.grid(row=0, column=1, padx=10)

        scissor_btn = ctk.CTkButton(button_frame, text="✂ Scissor",text_color="black" , font=("Arial", 14, "bold"),
                                    fg_color="#ff4444", hover_color="#cc0000",
                                    command=lambda: self.play_game("S"))
        scissor_btn.grid(row=0, column=2, padx=10)

        back_btn = ctk.CTkButton(self.game_frame, text="⬅ Back", font=("Arial", 14, "bold"),
                                 fg_color="orange", text_color= "black" , hover_color="#cc8400",
                                 command=self.back_to_menu)
        back_btn.pack(pady=20)

    def play_game(self, youstr):
        computer = random.choice([1, -1, 0])
        you = youDict[youstr]

        result_text = f"You choose {reversedDict[you]}\nComputer choose {reversedDict[computer]}\n"

        if computer == you:
            result_text += "It's a Draw 🤝"
        elif (you == 1 and computer == 0) or (you == -1 and computer == 1) or (you == 0 and computer == -1):
            result_text += "You Won 👑"
        else:
            result_text += "You Lose 😞"

        self.result_label.configure(text=result_text)

    def back_to_menu(self):
        self.game_frame.pack_forget()
        self.start_frame.pack(expand=True)


if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()



