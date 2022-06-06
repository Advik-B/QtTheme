try:
    from qtpy.QtWidgets import QMainWindow, QWidget
except ModuleNotFoundError as e:
    try:
        from PyQt5.QtWidgets import QMainWindow, QWidget
    except ModuleNotFoundError as e:
        try:
            from PySide2.QtWidgets import QMainWindow, QWidget
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "QtTheme: Could not find any Qt library. Please install PyQt5, PySide2 or QtPy"
            ) from e
    finally:
        try:
            assert QMainWindow and QWidget
        except (AssertionError, NameError) as e:
            raise ModuleNotFoundError(
                "QtTheme: Could not find any Qt library. Please install PyQt5, PySide2 or QtPy"
            ) from e
        
import typing, random, os, platform

if platform.system().casefold() == "windows":
    cwd = __file__.split("\\")[:-1]
else:
    cwd = __file__.split("/")[:-1]
cwd = os.path.join(*cwd)
# print(cwd)

class ThemeNotFoundError(Exception):
    pass


class CanNotApplyThemeError(Exception):
    pass


class ClassDoesNotSupportStyleSheetsError(Exception):
    pass


class ThemeCouldNotBeAppliedError(Exception):
    pass


def apply_theme(
    gui: typing.Union[QMainWindow, QWidget], theme: str, mode: str = "append"
):
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
        with open(f"{cwd}/themes/{theme}.css", "r") as theme:
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
        raise ClassDoesNotSupportStyleSheetsError(
            f"{gui.__class__.__name__} does not support setStyleSheet method"
        ) from e

    except Exception as e:
        raise e from e


def list_themes():
    """Summary

    Returns:
        list: list of themes
    """
    themes = []
    for file in os.listdir(f"{cwd}/themes"):
        if file.endswith(".css"):
            themes.append(file.replace(".css", ""))
    return themes


def apply_random_theme(gui: typing.Union[QMainWindow, QWidget]):
    """Summary

    Args:
        gui (QMainWindow | QWidget): Must be a valid widget that supports`setStyleSheet` method
    """
    themes = list_themes()
    theme = random.choice(themes)
    apply_theme(gui, theme)
