import tkinter as tk
from tkinter import messagebox

class Objective:
    def __init__(self, degree, hours):
        self.degree = degree
        self.hours = hours
        self.weighted_score = degree * hours


class GPA:
    def __init__(self, prev_gpa, prev_hours):
        self.prev_gpa = prev_gpa
        self.prev_hours = prev_hours
        self.objs = []
    
    def add_obj(self, obj):
        self.objs.append(obj)
    
    def calculate_new_gpa(self):
        if not self.objs:
            return 0
        total_weighted_score = sum(obj.weighted_score for obj in self.objs)
        new_hours = sum(obj.hours for obj in self.objs)
        return total_weighted_score / new_hours
    

    def calculate_current_gpa(self):
        if self.prev_hours == 0:
            messagebox.showerror("Error", "Previous hours cannot be zero")
            return 0
    
        new_gpa = self.calculate_new_gpa()
        total_hours = self.prev_hours + sum(obj.hours for obj in self.objs)
        return ((self.prev_gpa * self.prev_hours) + (new_gpa * sum(obj.hours for obj in self.objs))) / total_hours

    def __str__(self):
        return f"Current GPA: {round(self.calculate_current_gpa(), 2)}% or {round(self.calculate_current_gpa() * 4 / 100, 2)} out of 4.0"


class GPA_GUI:
    def __init__(self, master):
        self.master = master
        master.title("GPA Calculator")

        # Previous GPA widgets
        prev_gpa_label = tk.Label(master, text="Previous GPA:")
        prev_gpa_label.grid(row=0, column=0)
        self.prev_gpa_entry = tk.Entry(master)
        self.prev_gpa_entry.grid(row=0, column=1)

        prev_hours_label = tk.Label(master, text="Previous Hours:")
        prev_hours_label.grid(row=1, column=0)
        self.prev_hours_entry = tk.Entry(master)
        self.prev_hours_entry.grid(row=1, column=1)

        # Course info widgets
        degree_label = tk.Label(master, text="Degree:")
        degree_label.grid(row=2, column=0)
        self.degree_entry = tk.Entry(master)
        self.degree_entry.grid(row=2, column=1)

        hours_label = tk.Label(master, text="Hours:")
        hours_label.grid(row=3, column=0)
        self.hours_entry = tk.Entry(master)
        self.hours_entry.grid(row=3, column=1)

        add_button = tk.Button(master, text="Add Course", command=self.add_course)
        add_button.grid(row=4, column=0)

        self.course_listbox = tk.Listbox(master)
        self.course_listbox.grid(row=5, column=0, columnspan=2)

        calculate_button = tk.Button(master, text="Calculate GPA", command=self.calculate_gpa)
        calculate_button.grid(row=6, column=0)

    def add_course(self):
        try:
            obj = Objective(float(self.degree_entry.get()), float(self.hours_entry.get()))
            self.course_listbox.insert(tk.END, f"{self.degree_entry.get()} degree, {self.hours_entry.get()} hours")
            self.degree_entry.delete(0, tk.END)
            self.hours_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for degree and hours")

    def calculate_gpa(self):
        try:
            prev_gpa = float(self.prev_gpa_entry.get())
            prev_hours = float(self.prev_hours_entry.get())
            gpa = GPA(prev_gpa, prev_hours)
            for i in range(self.course_listbox.size()):
                degree, hours = self.course_listbox.get(i).split(',')
                obj = Objective(float(degree.split()[0]), float(hours.split()[0]))
                gpa.add_obj(obj)
            result = f"Current GPA: {round(gpa.calculate_current_gpa(), 2)}% or {round(gpa.calculate_current_gpa() * 4 / 100, 2)} out of 4.0"
            messagebox.showinfo("Result", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for previous GPA and hours")


if __name__ == '__main__':
    root = tk.Tk()
    gpa_gui = GPA_GUI(root)
    root.mainloop()
