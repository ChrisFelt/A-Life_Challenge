import settings
import parameters_window
import tkinter

if __name__ == "__main__":
    organisms = []
    root = tkinter.Tk()
    root.minsize(settings.screen_size, settings.screen_size//2)
    # root.eval('tk::PlaceWindow . center') # todo: find a better method to center window
    root.winfo_toplevel().title("A-Life Challenge")

    parameters_window.change_to_parameters(root,
                                           organisms,
                                           settings.prey_attributes,
                                           settings.pred_attributes)
    root.mainloop()
