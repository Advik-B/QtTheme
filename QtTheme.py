from qtpy.QtWidgets import QMainWindow, QWidget
import typing

class ThemeNotFoundError(Exception): pass
class CanNotApplyThemeError(Exception): pass
class ClassDoesNotSupportStyleSheetsError(Exception): pass
class ThemeCouldNotBeAppliedError(Exception): pass

def apply_theme(gui: typing.Union[QMainWindow, QWidget], theme: str, mode: str="append"):
    """Summary

    Args:
        gui (QMainWindow | QWidget): Must be a valid widget that supports`setStyleSheet` method

        theme (str): the theme to set example: 
        >>> apply_theme(self, "ubuntu")
        
        mode (str, optional): Defaults to "append". mode can be "append" or "replace"
        mode "append" will append the style to the current style sheet
        mode "replace" will replace the current style sheet with the new style


        side-note: the theme(s) are case insensitive
    """
    try:
        OLD_STYLE = gui.styleSheet()
        with open(f"themes/{theme}.css", 'r') as theme:
            THEME = theme.read()
            if mode.casefold() == "append":
                gui.setStyleSheet(str(gui.styleSheet()) + THEME)
            elif mode.casefold() == "replace":
                gui.setStyleSheet(THEME)
        
        # Check if the theme was applied
        if gui.styleSheet() == OLD_STYLE:
            raise CanNotApplyThemeError(f"Theme {theme} could not be applied")
        # elif gui.styleSheet() == THEME:
        #     pass
        elif gui.styleSheet() == "":
            raise ThemeCouldNotBeAppliedError(f"Theme {theme} could not be applied")

    except FileNotFoundError as e:
        raise ThemeNotFoundError(f"Theme {theme} not found") from e
    
    except AttributeError as e:
        raise ClassDoesNotSupportStyleSheetsError(f"{gui.__class__.__name__} does not support setStyleSheet method") from e

    except Exception as e:
        raise e from e