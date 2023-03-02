from gi.repository import GObject


class Thingy(GObject.GObject):
    _beep = "boop"

    @GObject.property
    def good_property_deprecated(self):
        """This property method docstring does not need to be written in imperative mood."""
        return self._beep

    @GObject.Property
    def good_property(self):
        """This property method docstring does not need to be written in imperative mood."""
        return self._beep
