import settings
import parameters_frame


if __name__ == "__main__":

    parameters_frame.change_to_parameters(settings.root,
                                          settings.organisms,
                                          settings.prey_attributes,
                                          settings.pred_attributes)
    settings.root.mainloop()
