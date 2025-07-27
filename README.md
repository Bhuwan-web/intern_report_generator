# IOST BSc CSIT Internship Report Formatter

A comprehensive Python tool to format Word documents according to the Institute of Science and Technology (IOST), Tribhuvan University guidelines for BSc CSIT internship reports.

## Features

### 🔧 Document Formatting

-   **Font Standards**: Times New Roman throughout
-   **Font Sizes**:
    -   Paragraphs: 12pt
    -   Chapter Headings: 16pt (Bold)
    -   Section Headings: 14pt (Bold)
    -   Sub-section Headings: 12pt (Bold)
    -   Figure/Table Captions: 12pt (Bold)
-   **Line Spacing**: 1.5 for all paragraphs
-   **Alignment**: Justified paragraphs, centered captions
-   **Margins**: Top/Bottom/Right: 1", Left: 1.25"
-   **Page Size**: A4
-   **Table Formatting**: Centered alignment

### 📝 Language Analysis

-   Detects first-person pronouns (I, we, you, etc.)
-   Identifies contractions that should be expanded
-   Suggests passive voice alternatives
-   Provides academic writing recommendations

### 📚 Citation Checking

-   Identifies APA format citations
-   Detects bare URLs that need proper citation
-   Suggests citation management tools

## Installation

1. Install Python 3.6 or higher
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Format and analyze document (default)
python main.py my_report.docx

# Only format the document
python main.py my_report.docx format

# Only analyze language and citations
python main.py my_report.docx analyze
```

### Individual Tools

#### Document Formatting Only

```bash
python document_formatter.py my_report.docx
python document_formatter.py my_report.docx -o custom_output.docx
```

#### Language and Citation Analysis Only

```bash
python academic_tools.py my_report.docx
```

#### Simple Formatting Script

```bash
python format_document.py my_report.docx
```

## Output

The formatter creates:

-   `formatted_[filename].docx` - Formatted document
-   Console analysis of language and citation issues
-   Recommendations for improvement

## What Gets Formatted

### Automatic Detection and Formatting:

-   **Chapter headings**: "Chapter 1:", "CHAPTER 2:", etc.
-   **Section headings**: "1.1", "2.3", etc.
-   **Subsection headings**: "1.1.1", "2.3.4", etc.
-   **Figure captions**: "Figure 1.1:", "FIGURE 2.3:", etc.
-   **Table captions**: "Table 1.1:", "TABLE 2.3:", etc.
-   **Regular paragraphs**: All other text

### Manual Adjustments Needed:

-   Page numbering (Roman numerals for preliminary pages)
-   Chapter page breaks
-   Figure and table positioning
-   Reference formatting

## Recommended Tools for Complete Compliance

### Citation Management:

-   **Zotero** (Free, open-source)
-   **Mendeley** (Free with premium options)
-   **EndNote** (Paid, institutional licenses available)

### Grammar and Language:

-   **Grammarly** (Free/Premium)
-   **LanguageTool** (Free/Premium)
-   **Hemingway Editor** (Readability)

### APA Style:

-   **APA Style Guide** (Official resource)
-   **Purdue OWL** (Free APA guidelines)

## File Structure

```
├── main.py                 # Main script (format + analyze)
├── document_formatter.py   # Core formatting logic
├── academic_tools.py       # Language and citation analysis
├── format_document.py      # Simple formatting script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Example Output

```
IOST BSc CSIT Internship Report Processor
==================================================

🔧 FORMATTING DOCUMENT
------------------------------
Setting page margins...
Formatting paragraphs...
Formatting tables...
Document formatting completed!
✅ Formatted document saved as: formatted_my_report.docx

🔍 ANALYZING DOCUMENT
------------------------------
Analyzing document: my_report.docx
============================================================

📝 LANGUAGE ANALYSIS
------------------------------
⚠️  Found 3 language issues:

Paragraph 15:
Preview: I implemented the user authentication system using Django...
  - First_Person: 'I' → Consider using passive voice or third person

📚 CITATION ANALYSIS
------------------------------
✅ Found 12 properly formatted citations
⚠️  Found 2 citation issues:

Paragraph 23:
Preview: More information can be found at https://django.com/docs...
  - Bare_Url: 'https://django.com/docs' → URLs should be properly cited in APA format

🔧 RECOMMENDATIONS
------------------------------
For better academic writing:
• Use Grammarly or LanguageTool for grammar checking
• Use Zotero, Mendeley, or EndNote for citation management
• Consider Hemingway Editor for readability
• Use passive voice in technical descriptions
• Ensure all sources are properly cited in APA format
```

## Limitations

-   Page numbering requires manual adjustment in Word
-   Complex table formatting may need manual review
-   Citation format validation is basic (use dedicated tools for complete APA compliance)
-   Figure positioning may require manual adjustment

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is provided as-is for educational purposes.
