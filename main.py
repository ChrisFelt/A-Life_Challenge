import settings
import parameters_frame
import tkinter

organisms = []
root = tkinter.Tk()

if __name__ == "__main__":

    parameters_frame.change_to_parameters(root,
                                          organisms,
                                          settings.prey_attributes,
                                          settings.pred_attributes)
    root.mainloop()
