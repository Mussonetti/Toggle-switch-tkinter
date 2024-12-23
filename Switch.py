import tkinter as tk

class ToggleSwitchCanvas:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

        self.width = 200
        self.height = 100
        self.on_color = "#4caf50"
        self.off_color = "#dcdcdc"
        self.handle_color = "#ffffff"
        self.is_on = False  # Estado inicial OFF
        self.margin = 2
        self.radius = self.height // 2

        self.base = self.canvas.create_rounded_rectangle(
            x, y, x + self.width, y + self.height,
            radius=self.height // 2,
            fill=self.off_color,
            outline="",  
            tags="base"
        )

        self.handle = self.canvas.create_oval(
            x + 2, y + 2, x + self.height - 2, y + self.height - 2,
            fill=self.handle_color,
            outline="",  
            tags="handle"
        )

        self.canvas.tag_bind("base", "<Button-1>", self.toggle_state)
        self.canvas.tag_bind("handle", "<Button-1>", self.toggle_state)

    def toggle_state(self, event=None):
        """Alterna entre ON y OFF y actualiza el estado automáticamente."""
        self.is_on = not self.is_on
        self.update_switch()
        self.print_state()  

    def update_switch(self):
        """Actualiza el estado del toggle en el canvas."""
        if self.is_on:
            
            self.canvas.itemconfig(self.base, fill=self.on_color)
            self.canvas.coords(
                self.handle,
                self.x + self.width - self.height + 2, self.y + 2,
                self.x + self.width - 2, self.y + self.height - 2
            )
        else:
            
            self.canvas.itemconfig(self.base, fill=self.off_color)
            self.canvas.coords(
                self.handle,
                self.x + 2, self.y + 2,
                self.x + self.height - 2, self.y + self.height - 2
            )

    def get_state(self):
        """Devuelve el estado actual (ON=True, OFF=False)."""
        return self.is_on

    def print_state(self):
        """Imprime el estado actual automáticamente."""
        estado = "ON" if self.is_on else "OFF"
        print(f"El estado actual del toggle es: {estado}")


    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)


   
    tk.Canvas.create_rounded_rectangle = create_rounded_rectangle



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Toggle Switch en Canvas")
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()

    
    toggle = ToggleSwitchCanvas(canvas, x=50, y=50)

    root.mainloop()

### To get toggle state to mantain after resteting canvas
### toggle_state = self.toggle.get_state() ###Save toggle state before reseting canvas
###
###     This after reseting canvas to get state back 
###     if toggle_state:
###         self.toggle.is_on = True            
###     else:
###         self.toggle.is_on = False           
###     self.toggle.update_switch()

