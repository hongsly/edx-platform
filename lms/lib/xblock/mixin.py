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
        help=_("Which chrome to show. Options: \n"
             "chromeless -- No chrome\n"
             "tabs -- just tabs\n"
             "accordion -- just accordion\n"
             "tabs,accordion -- Full Chrome"),
        scope=Scope.settings,
        default=None,
    )
    default_tab = String(
        display_name=_("Default Tab"),
        help=_("Override which tab is selected. If not set, courseware tab is shown."),
        scope=Scope.settings,
        default=None,
    )
    source_file = String(
        display_name=_("LaTeX Source File Name"),
        help=_("Source file name for LaTeX"),
        scope=Scope.settings,
        deprecated=True
    )
    ispublic = Boolean(
        display_name=_("Course Is Public"),
        help=_("Whether this course is open to the public, or only to admins"),
        scope=Scope.settings,
        deprecated=True
    )
