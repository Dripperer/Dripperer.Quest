import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "In quale anno è stata creata la band Dripperer?",
        "options": ["2022", "2021", "2023", "2020"],
        "answer": "2023"
    },
    {
        "question": "Qual è il nome del primo album della band?",
        "options": ["Smile", "Reverie", "No Sleep", "Electric Souls"],
        "answer": "Smile"
    },
    {
        "question": "Qual è la prima canzone pubblicata dalla band?",
        "options": ["Drip & Chill Chill", "No Sleep", "Melodies of Drip", "Electric Vibes"],
        "answer": "Drip & Chill Chill"
    },
    {
        "question": "Chi è il chitarrista della band?",
        "options": ["Andrea", "Sebasthian", "Ilaria", "Lorelayne"],
        "answer": "Ilaria"
    },
    {
        "question": "Chi è il batterista della band?",
        "options": ["Andrea", "Sebasthian", "Lorelayne", "Ilaria"],
        "answer": "Sebasthian"
    },
    {
        "question": "Chi suona il piano nella band?",
        "options": ["Andrea", "Sebasthian", "Lorelayne", "Ilaria"],
        "answer": "Lorelayne"
    },
    {
        "question": "Chi è il membro che suona l'ukulele?",
        "options": ["Sebasthian", "Lorelayne", "Andrea", "Ilaria"],
        "answer": "Andrea"
    },
    {
        "question": "Qual era il nome iniziale della band prima di diventare Dripperer?",
        "options": ["Drip & Chill", "BEATZ", "The Jammers", "Chill Vibes"],
        "answer": "BEATZ"
    },
    {
        "question": "Quanti membri aveva la band all'inizio?",
        "options": ["4", "6", "5", "3"],
        "answer": "5"
    },
    {
        "question": "Chi ha cambiato il nome della band da BEATZ a Dripperer?",
        "options": ["Ilaria", "Andrea", "Lorelayne", "Sebasthian"],
        "answer": "Tutti insieme"
    }
]

score = 0
current_question = 0

def update_question():
    global current_question
    if current_question < len(questions):
        q = questions[current_question]
        question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            option_buttons[i].config(text=option)
    else:
        show_result()

def answer(option):
    global score, current_question
    correct_answer = questions[current_question]["answer"]
    if option == correct_answer:
        score += 1
    current_question += 1
    update_question()

def show_result():
    global score
    result_text = f"Il tuo punteggio finale è: {score}/{len(questions)}\n"
    if score == len(questions):
        result_text += "Sei un vero fan della band! 🎸🤘"
    elif score >= len(questions) // 2:
        result_text += "Non male! Continua a seguirci!"
    else:
        result_text += "Potresti fare meglio... ma grazie per aver partecipato!"
    messagebox.showinfo("Quiz completato", result_text)
    root.quit()

root = tk.Tk()
root.title("Dripperer Quiz Challenge")
root.config(bg="white")

font = ("Comic Sans MS", 14)

question_label = tk.Label(root, text="", font=("Comic Sans MS", 16, "bold"), bg="white", fg="black")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=font, bg="black", fg="white", command=lambda i=i: answer(questions[current_question]["options"][i]))
    button.pack(fill="both", pady=5, padx=50)
    option_buttons.append(button)

update_question()
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import json
import os

# File per salvare i dati degli utenti e i progressi
USERS_FILE = "users.json"
PROGRESS_FILE = "progress.json"

# Funzione per caricare i dati degli utenti
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

# Funzione per caricare i progressi settimanali
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as file:
            return json.load(file)
    return {}

# Funzione per salvare gli utenti
def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file)

# Funzione per salvare i progressi settimanali
def save_progress(progress):
    with open(PROGRESS_FILE, "w") as file:
        json.dump(progress, file)

# Domande e risposte
questions = [
    {
        "question": "In quale anno è stata creata la band Dripperer?",
        "options": ["2022", "2021", "2023", "2020"],
        "answer": "2023"
    },
    {
        "question": "Qual è il nome del primo album della band?",
        "options": ["Smile", "Reverie", "No Sleep", "Electric Souls"],
        "answer": "Smile"
    },
    {
        "question": "Qual è la prima canzone pubblicata dalla band?",
        "options": ["Drip & Chill Chill", "No Sleep", "Melodies of Drip", "Electric Vibes"],
        "answer": "Drip & Chill Chill"
    },
    {
        "question": "Chi è il chitarrista della band?",
        "options": ["Andrea", "Sebasthian", "Ilaria", "Lorelayne"],
        "answer": "Ilaria"
    },
    {
        "question": "Chi è il batterista della band?",
        "options": ["Andrea", "Sebasthian", "Lorelayne", "Ilaria"],
        "answer": "Sebasthian"
    },
    {
        "question": "Chi suona il piano nella band?",
        "options": ["Andrea", "Sebasthian", "Lorelayne", "Ilaria"],
        "answer": "Lorelayne"
    },
    {
        "question": "Chi è il membro che suona l'ukulele?",
        "options": ["Sebasthian", "Lorelayne", "Andrea", "Ilaria"],
        "answer": "Andrea"
    },
    {
        "question": "Qual era il nome iniziale della band prima di diventare Dripperer?",
        "options": ["Drip & Chill", "BEATZ", "The Jammers", "Chill Vibes"],
        "answer": "BEATZ"
    },
    {
        "question": "Quanti membri aveva la band all'inizio?",
        "options": ["4", "6", "5", "3"],
        "answer": "5"
    },
    {
        "question": "Chi ha cambiato il nome della band da BEATZ a Dripperer?",
        "options": ["Ilaria", "Andrea", "Lorelayne", "Sebasthian"],
        "answer": "Tutti insieme"
    }
]

# Classe principale per il gioco
class DrippererQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DRIPPERER QUEST")
        self.root.config(bg="white")
        
        self.users = load_users()
        self.progress = load_progress()
        self.current_user = None
        self.score = 0
        self.current_question = 0
        self.video_urls = []
        
        self.create_widgets()

    def create_widgets(self):
        # Menu laterale
        self.menu_button = tk.Button(self.root, text="☰", font=("Comic Sans MS", 16), command=self.show_menu)
        self.menu_button.pack(side="left", padx=10)

        # Schermata di login/registrazione
        self.login_frame = tk.Frame(self.root, bg="white")
        self.login_frame.pack(fill="both", expand=True)
        
        self.username_label = tk.Label(self.login_frame, text="Username:", font=("Comic Sans MS", 14), bg="white")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame, font=("Comic Sans MS", 14))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Comic Sans MS", 14), bg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Comic Sans MS", 14))
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.login_frame, text="Accedi", font=("Comic Sans MS", 14), command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.login_frame, text="Registrati", font=("Comic Sans MS", 14), command=self.register)
        self.register_button.pack(pady=10)
    
    def show_menu(self):
        menu = tk.Toplevel(self.root)
        menu.title("Menu")
        
        if self.current_user:
            menu_button_1 = tk.Button(menu, text="Cambia Account", command=self.logout)
            menu_button_1.pack(pady=5)
        else:
            menu_button_1 = tk.Button(menu, text="Accedi", command=self.show_login)
            menu_button_1.pack(pady=5)
        
        menu_button_2 = tk.Button(menu, text="Home", command=self.show_home)
        menu_button_2.pack(pady=5)
        
        if self.is_end_of_week():
            menu_button_3 = tk.Button(menu, text="Classifica Settimanale", command=self.show_leaderboard)
            menu_button_3.pack(pady=5)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username] == password:
            self.current_user = username
            messagebox.showinfo("Login", "Accesso riuscito!")
            self.show_home()
        else:
            messagebox.showerror("Errore", "Credenziali errate o utente non trovato!")
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username not in self.users:
            self.users[username] = password
            save_users(self.users)
            messagebox.showinfo("Registrazione", "Registrazione avvenuta con successo!")
            self.login()
        else:
            messagebox.showerror("Errore", "Username già esistente!")
    
    def logout(self):
        self.current_user = None
        self.show_login()
    
    def show_login(self):
        self.login_frame.pack(fill="both", expand=True)
    
    def show_home(self):
        # Rimuovere la schermata di login
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        self.login_frame.pack_forget()
        
        # Creare la schermata principale con domande
        home_frame = tk.Frame(self.root, bg="white")
        home_frame.pack(fill="both", expand=True)
        
        tk.Label(home_frame, text="DRIPPERER QUEST", font=("Comic Sans MS", 24, "bold"), bg="white").pack(pady=10)
        
        # Mostra le domande
        for i, question in enumerate(questions):
            button = tk.Button(home_frame, text=question["question"], font=("Comic Sans MS", 14), bg="black", fg="white", command=lambda i=i: self.show_question(i))
            button.pack(fill="both", pady=5, padx=50)
        
        # Casella per TikTok/Shorts
        self.video_label = tk.Label(home_frame, text="Inserisci massimo 5 link TikTok/Shorts", font=("Comic Sans MS", 14), bg="white")
        self.video_label.pack(pady=10)
        
        self.video_entries = []
        for _ in range(5):
            entry = tk.Entry(home_frame, font=("Comic Sans MS", 14))
            entry.pack(pady=5)
            self.video_entries.append(entry)
        
        # Bottone per inviare video
        submit_video_button = tk.Button(home_frame, text="Invia Video", font=("Comic Sans MS", 14), command=self.submit_videos)
        submit_video_button.pack(pady=10)
    
    def show_question(self, index):
        question = questions[index]
        
        question_frame = tk.Frame(self.root, bg="white")
        question_frame.pack(fill="both", expand=True)
        
        tk.Label(question_frame, text=question["question"], font=("Comic Sans MS", 16, "bold"), bg="white").pack(pady=10)
        
        for option in question["options"]:
            button = tk.Button(question_frame, text=option, font=("Comic Sans MS", 14), bg="black", fg="white", command=lambda option=option: self.check_answer(option, question["answer"]))
            button.pack(fill="both", pady=5, padx=50)
    
    def check_answer(self, selected_answer, correct_answer):
        if selected_answer == correct_answer:
            self.score += 10
            messagebox.showinfo("Corretto!", "Risposta corretta!")
        else:
            messagebox.showerror("Sbagliato", f"Risposta sbagliata! La risposta corretta era: {correct_answer}")
        
        self.current_question += 1
        if self.current_question >= len(questions):
            self.end_week()
        else:
            self.show_question(self.current_question)
    
    def submit_videos(self):
        video_links = [entry.get() for entry in self.video_entries if entry.get()]
        self.score += len(video_links) * 5  # Ogni video porta 5 punti
        messagebox.showinfo("Video inviati", f"Videos inviati: {len(video_links)}\nHai guadagnato {len(video_links) * 5} punti!")

    def end_week(self):
        """Termina la settimana e mostra il punteggio totale."""
        if self.current_user not in self.progress:
            self.progress[self.current_user] = {}
        
        self.progress[self.current_user]["score"] = self.score
        save_progress(self.progress)
        
        # Mostra il messaggio di fine settimana
        messagebox.showinfo("Fine settimana", f"Fine della settimana! Il tuo punteggio è: {self.score}")
        
        # Mostra la classifica
        self.show_leaderboard()

    def show_leaderboard(self):
        """Mostra la classifica dei punteggi settimanali."""
        leaderboard_frame = tk.Frame(self.root, bg="white")
        leaderboard_frame.pack(fill="both", expand=True)
        
        tk.Label(leaderboard_frame, text="Classifica Settimanale", font=("Comic Sans MS", 16, "bold"), bg="white").pack(pady=10)

        sorted_progress = sorted(self.progress.items(), key=lambda x: x[1]["score"], reverse=True)
        
        for idx, (user, data) in enumerate(sorted_progress):
            user_label = tk.Label(leaderboard_frame, text=f"{idx + 1}. {user} - {data['score']} punti", font=("Comic Sans MS", 14), bg="white")
            user_label.pack(pady=5)

    def is_end_of_week(self):
        """Controlla se è la fine della settimana per mostrare la classifica."""
        # Qui possiamo impostare una logica che determina la fine della settimana, per esempio:
        return True  # Per il momento mettiamo sempre True per simulare la fine della settimana

# Creazione e avvio dell'app
root = tk.Tk()
app = DrippererQuizApp(root)
root.mainloop()
