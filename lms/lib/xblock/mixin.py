"""
Namespace that defines fields common to all blocks used in the LMS
"""
from xblock.fields import Boolean, Scope, String, XBlockMixin

# Make '_' a no-op so we can scrape strings
_ = lambda text: text


class LmsBlockMixin(XBlockMixin):
    """
    Mixin that defines fields common to all blocks used in the LMS
    """
    hide_from_toc = Boolean(
        help="Whether to display this module in the table of contents",
        default=False,
        scope=Scope.settings
    )
    format = String(
        help="What format this module is in (used for deciding which "
             "grader to apply, and what to show in the TOC)",
        scope=Scope.settings,
    )
    chrome = String(
        display_name=_("Courseware Chrome"),
        help=_("Enter the chrome, or navigation tools, to use for the XBlock in the LMS. Valid values are: \n"
             "chromeless -- To not use tabs or the accordion\n"
             "tabs -- To use tabs only\n"
             "accordion -- To use the accordion only\n"
             "tabs,accordion -- To use tabs and the accorion"),
        scope=Scope.settings,
        default=None,
    )
    default_tab = String(
        display_name=_("Default Tab"),
        help=_("Enter the tab that is selected in the XBlock. If not set, the Courseware tab is shown."),
        scope=Scope.settings,
        default=None,
    )
    source_file = String(
        display_name=_("LaTeX Source File Name"),
        help=_("Enter the source file name for LaTeX."),
        scope=Scope.settings,
        deprecated=True
    )
    ispublic = Boolean(
        display_name=_("Course Is Public"),
        help=_("Enter true or false. If true, the course is open to the public. If false, the course is open only to admins."),
        scope=Scope.settings,
        deprecated=True
    )
