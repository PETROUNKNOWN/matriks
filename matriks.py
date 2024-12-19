import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Matriks 2.0.0")
        self.geometry("-5-0")
        self.resizable(0, True)
        
        self.canvasSize=800
        self.canvasSizeVar = customtkinter.StringVar(value=str(self.canvasSize)) 

        self.canvasDivisions=10
        self.canvasDivisionsVar = customtkinter.StringVar(value="10") 

        self.reticleSize=1
        self.reticleSizeVar = customtkinter.StringVar(value="1")        
        
        self.reticleToggle=1
        self.reticleToggleVar = customtkinter.StringVar(value="On")

        self.reticleColor="#0000FF"
        self.reticleColorVar = customtkinter.StringVar(value="Blue")

        self.reticleGapSize=0
        self.reticleGapSizeVar = customtkinter.StringVar(value="0") 

        self.gridToggle=1
        self.gridToggleVar = customtkinter.StringVar(value="On")

        self.gridSolid=True
        self.gridSolidVar = customtkinter.StringVar(value="Dashed")

        self.gridColor="#292929"
        self.gridColorVar = customtkinter.StringVar(value="Grey")

        self.gridIntersectionToggle=1
        self.gridIntersectionToggleVar=customtkinter.StringVar(value="On")

        self.gridIntersectionColor="#0000FF"
        self.gridIntersectionColorVar = customtkinter.StringVar(value="Blue")

        self.gridIntersectionSize=2
        self.gridIntersectionSizeVar = customtkinter.StringVar(value="2")

        self.backgroundColor="#191A19"

        self.accentColor="#0000FF"
        self.accentColorVar = customtkinter.StringVar(value="Blue")

        self.draw_app()

    def draw_app(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.matrix_canvas=customtkinter.CTkCanvas(self,bg=self.backgroundColor,bd=0,highlightbackground=self.accentColor,highlightthickness=1,highlightcolor=self.accentColor,width=self.canvasSize,height=self.canvasSize)
        self.matrix_canvas.grid(row=0, column=0,sticky="nsew",padx=(20,10),pady=20)
        self.matrix_canvas.grid_propagate(0)

        self.tabview = customtkinter.CTkTabview(self,border_color=self.accentColor,corner_radius=7,border_width=1,width=300,fg_color=self.backgroundColor)
        self.tabview.grid(row=0, column=2, padx=(10, 20), pady=20, sticky="nsew")
        #self.tabview.grid_propagate(0)
        self.tabview.add("Settings")
        self.tabview.tab("Settings").grid_columnconfigure(1, weight=1)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Reticle:", anchor="w").grid(row=0, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.reticleToggleVar,values=["On","Off"],command=lambda selected_option:  self.func_reticle(action="toggle",selected_value=selected_option)).grid(row=0, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid:", anchor="w").grid(row=1, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridToggleVar,values=["On","Off"],command=lambda selected_option:  self.func_grid(action="toggle",selected_value=selected_option)).grid(row=1, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Intersections:", anchor="w").grid(row=2, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridIntersectionToggleVar,values=["On","Off"],command=lambda selected_option: self.func_grid(action="gridIntersectionToggle",selected_value=selected_option)).grid(row=2, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Reticle Color:", anchor="w").grid(row=3, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.reticleColorVar,values=["Red", "Green", "Blue","White"],command=lambda selected_option: self.func_reticle(action="color",selected_value=selected_option)).grid(row=3, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Intersection Color:", anchor="w").grid(row=4, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridIntersectionColorVar,values=["Red", "Green", "Blue","White"],command=lambda selected_option: self.func_grid(action="gridIntersectionColor",selected_value=selected_option)).grid(row=4, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Accent Color:", anchor="w").grid(row=5, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.accentColorVar,values=["Red", "Green", "Blue","White"],command=lambda selected_option: self.func_app(action="color",selected_value=selected_option)).grid(row=5, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Intersection Size:", anchor="w").grid(row=6, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridIntersectionSizeVar,values=["2","3","5","7"],command=lambda selected_option: self.func_grid(action="gridIntersectionSize",selected_value=selected_option)).grid(row=6, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Type:", anchor="w").grid(row=7, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridSolidVar,values=["Solid","Dashed"],command=lambda selected_option: self.func_grid(action="gridSolidToggle",selected_value=selected_option)).grid(row=7, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Reticle Line Size:", anchor="w").grid(row=8, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.reticleSizeVar,values=["1","2","3","4","5","6","7","8"],command=lambda selected_option: self.func_reticle(action="reticleSize",selected_value=selected_option)).grid(row=8, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Divisions:", anchor="w").grid(row=9, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.canvasDivisionsVar,values=["5","10","15","20","25","30","35"],command=lambda selected_option: self.func_grid(action="gridStep",selected_value=selected_option)).grid(row=9, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Grid Color:", anchor="w").grid(row=10, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.gridColorVar,values=["Red", "Green", "Blue","Grey"],command=lambda selected_option: self.func_grid(action="color",selected_value=selected_option)).grid(row=10, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Reticle Gap Size:", anchor="w").grid(row=11, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.reticleGapSizeVar,values=["0","3","5","8","10","20","30","40","50","60"],command=lambda selected_option: self.func_reticle(action="reticleGapSize",selected_value=selected_option)).grid(row=11, column=2,sticky="e",padx=5,pady=5)
        customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Canvas Size:", anchor="w").grid(row=12, column=0,sticky="w",padx=5,pady=5)
        customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),variable=self.canvasSizeVar,values=["400","500","800"],command=lambda selected_option: self.func_app(action="appSize",selected_value=selected_option)).grid(row=12, column=2,sticky="e",padx=5,pady=5)

        halfCanvas=self.canvasSize/2
        fracCanvas=self.canvasSize*0.25
        match self.reticleToggle:
            
            case 0:
                pass
            case 1:
                self.matrix_canvas.create_line((halfCanvas,halfCanvas-self.reticleGapSize),(halfCanvas,halfCanvas-fracCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas,halfCanvas+self.reticleGapSize),(halfCanvas,halfCanvas+fracCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas-self.reticleGapSize,halfCanvas),(halfCanvas-fracCanvas,halfCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas+self.reticleGapSize,halfCanvas),(halfCanvas+fracCanvas,halfCanvas),fill=self.reticleColor,width=self.reticleSize)
            case _:
                pass

        match self.gridToggle:
            case 0:
                pass
            case 1:
                self.canvasStep=self.canvasSize/self.canvasDivisions
                for i in range(1, self.canvasDivisions):
                    for j in range(1, self.canvasDivisions):
                        x = i * self.canvasStep
                        y = j * self.canvasStep

                        
                        
                        # Draw vertical and horizontal lines
                        self.matrix_canvas.create_line(x, 0, x, self.canvasSize, fill=self.gridColor, dash=self.gridSolid)
                        self.matrix_canvas.create_line(0, y, self.canvasSize, y, fill=self.gridColor, dash=self.gridSolid)

                        match self.gridIntersectionToggle:
                            case 0:
                                pass
                            case 1:
                                # Draw a small circle at the intersection
                                self.matrix_canvas.create_oval(
                                    x - self.gridIntersectionSize, y - self.gridIntersectionSize,  # Top-left corner
                                    x + self.gridIntersectionSize, y + self.gridIntersectionSize,  # Bottom-right corner
                                    fill=self.gridIntersectionColor, outline=self.gridColor
                                )
                            case _:
                                pass
                        
                        
            case _:
                pass
        


    def draw_canvas(self):
        if self.matrix_canvas:
            self.matrix_canvas.destroy()
        self.matrix_canvas=customtkinter.CTkCanvas(self,bg=self.backgroundColor,bd=0,highlightbackground=self.accentColor,highlightthickness=1,highlightcolor=self.accentColor,width=self.canvasSize,height=self.canvasSize)
        self.matrix_canvas.grid(row=0, column=0,sticky="nsew",padx=(20,10),pady=20)
        self.matrix_canvas.grid_propagate(0)

        halfCanvas=self.canvasSize/2
        fracCanvas=self.canvasSize*0.25
        match self.reticleToggle:
            
            case 0:
                pass
            case 1:
                self.matrix_canvas.create_line((halfCanvas,halfCanvas-self.reticleGapSize),(halfCanvas,halfCanvas-fracCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas,halfCanvas+self.reticleGapSize),(halfCanvas,halfCanvas+fracCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas-self.reticleGapSize,halfCanvas),(halfCanvas-fracCanvas,halfCanvas),fill=self.reticleColor,width=self.reticleSize)
                self.matrix_canvas.create_line((halfCanvas+self.reticleGapSize,halfCanvas),(halfCanvas+fracCanvas,halfCanvas),fill=self.reticleColor,width=self.reticleSize)
            case _:
                pass

        match self.gridToggle:
            
            case 0:
                pass
            case 1:
                self.canvasStep=self.canvasSize/self.canvasDivisions
                for i in range(1, self.canvasDivisions):
                    for j in range(1, self.canvasDivisions):
                        x = i * self.canvasStep
                        y = j * self.canvasStep
                        
                        # Draw vertical and horizontal lines
                        self.matrix_canvas.create_line(x, 0, x, self.canvasSize, fill=self.gridColor, dash=self.gridSolid)
                        self.matrix_canvas.create_line(0, y, self.canvasSize, y, fill=self.gridColor, dash=self.gridSolid)

                        match self.gridIntersectionToggle:
                            case 0:
                                pass
                            case 1:
                                # Draw a small circle at the intersection
                                self.matrix_canvas.create_oval(
                                    x - self.gridIntersectionSize, y - self.gridIntersectionSize,  # Top-left corner
                                    x + self.gridIntersectionSize, y + self.gridIntersectionSize,  # Bottom-right corner
                                    fill=self.gridIntersectionColor, outline=self.gridColor
                                )
                            case _:
                                pass
                        
                        
            case _:
                pass
    
    def func_app(self,*args,**kwargs):
        match kwargs.get("action"):
            case "color":
                self.accentColor=kwargs.get("selected_value")
            case "appSize":
                self.canvasSize=int(kwargs.get("selected_value"))
            case _:
                print("FLAG 3")

        self.draw_app()

    def func_reticle(self,*args,**kwargs):
        match kwargs.get("action"):
            case "toggle":
                match kwargs.get("selected_value"):
                    case "On":
                        self.reticleToggle=1
                    case "Off":
                        self.reticleToggle=0
                    case _:
                        pass
            case "color":
                self.reticleColor=kwargs.get("selected_value")
            case "reticleSize":
                self.reticleSize=int(kwargs.get("selected_value"))
            case "reticleGapSize":
                self.reticleGapSize=int(kwargs.get("selected_value"))
            case _:
                print("FLAG 1")

        self.draw_canvas()

    def func_grid(self,*args,**kwargs):
        match kwargs.get("action"):
            case "toggle":
                match kwargs.get("selected_value"):
                    case "On":
                        self.gridToggle=1
                    case "Off":
                        self.gridToggle=0
                    case _:
                        pass
            case "gridIntersectionToggle":
                match kwargs.get("selected_value"):
                    case "On":
                        self.gridIntersectionToggle=1
                    case "Off":
                        self.gridIntersectionToggle=0
                    case _:
                        pass
            case "gridIntersectionColor":
                self.gridIntersectionColor=kwargs.get("selected_value")
            case "gridIntersectionSize":
                self.gridIntersectionSize=int(kwargs.get("selected_value"))
            case "gridSolidToggle":
                match kwargs.get("selected_value"):
                    case "Solid":
                        self.gridSolid=None
                    case "Dashed":
                        self.gridSolid=True
                    case _:
                        pass
            case "gridStep":
                self.canvasDivisions=int(kwargs.get("selected_value"))
            case "color":
                match kwargs.get("selected_value"):
                    case "Red":
                        self.gridColor="#502929"
                    case "Green":
                        self.gridColor="#295029"
                    case "Blue":
                        self.gridColor="#292950"
                    case "Grey":
                        self.gridColor="#292929"
                    case _:
                        pass
            case _:
                print("FLAG 2")

        self.draw_canvas()

if __name__ == "__main__":
    app = App()
    app.mainloop()