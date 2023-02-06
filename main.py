import settings
import parameters_window
import tkinter

if __name__ == "__main__":
    organisms = []
    root = tkinter.Tk()

    parameters_window.change_to_parameters(root,
                                           organisms,
                                           settings.prey_attributes,
                                           settings.pred_attributes)
    root.mainloop()
