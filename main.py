import settings
import parameters_window
import tkinter

if __name__ == "__main__":
    organisms = []
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=settings.screen_size, height=settings.screen_size)
    # canvas.config(width=settings.frame_width, height=settings.frame_height)
    canvas.pack(side="top", anchor="nw")

    parameters_window.change_to_parameters(canvas,
                                          organisms,
                                          settings.prey_attributes,
                                          settings.pred_attributes)
    canvas.mainloop()
