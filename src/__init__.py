"""
IOST BSc CSIT Internship Report Formatter
A comprehensive Python toolkit for academic document formatting
"""

__version__ = "0.1.0"
__author__ = "IOST Academic Tools Team"
__description__ = "Advanced academic document formatting and analysis toolkit"

# Core modules
from .document_formatter import IOSTDocumentFormatter
from .enhanced_academic_tools import DocumentAutoFixer, auto_fix_document
from .academic_line_break_manager import AcademicLineBreakManager, process_document_line_breaks
from .academic_tools import LanguageChecker, CitationChecker, analyze_document

__all__ = [
    "IOSTDocumentFormatter",
    "DocumentAutoFixer",
    "auto_fix_document",
    "AcademicLineBreakManager",
    "process_document_line_breaks",
    "LanguageChecker",
    "CitationChecker",
    "analyze_document",
]
