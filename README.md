# 🎓 IOST BSc CSIT Internship Report Formatter

A comprehensive, intelligent Python toolkit for formatting Word documents according to the Institute of Science and Technology (IOST), Tribhuvan University guidelines for BSc CSIT internship reports. This advanced system combines document formatting, academic writing analysis, automatic language correction, and intelligent line break management.

## 🚀 Key Features

### 🔧 Advanced Document Formatting

-   **Intelligent Style Detection**: Automatically identifies and formats chapters, sections, subsections, figures, and tables
-   **IOST-Compliant Typography**:
    -   Font: Times New Roman throughout
    -   Chapter Headings: 16pt Bold
    -   Section Headings: 14pt Bold
    -   Subsection Headings: 12pt Bold
    -   Body Text: 12pt, 1.5 line spacing, justified
    -   Figure/Table Captions: 12pt Bold, centered
-   **Precise Page Layout**: A4 size with IOST-standard margins (Left: 1.25", Others: 1")
-   **Smart Page Break Management**: Automatic chapter page breaks with section break preservation

### 🤖 AI-Powered Language Enhancement

-   **Automatic Text Correction**: Converts first-person to passive voice
-   **Academic Tone Optimization**: Replaces informal language with academic alternatives
-   **Contraction Expansion**: Automatically expands contractions for formal writing
-   **Context-Aware Fixes**: Maintains original meaning while improving academic style

### 📏 Academic Line Break Management

-   **Standards-Based Spacing**: Implements proper academic line break standards
-   **Content-Type Recognition**: Distinguishes between chapters, sections, paragraphs, figures, and quotes
-   **Google Docs Import Compatibility**: Preserves existing section breaks from imported documents
-   **Excessive Whitespace Removal**: Intelligently removes unnecessary empty paragraphs

### 📚 Citation Intelligence

-   **APA Format Detection**: Identifies properly formatted citations
-   **URL Citation Conversion**: Automatically converts bare URLs to proper citation format
-   **Source Recognition**: Maps common websites to appropriate citation sources
-   **Citation Validation**: Comprehensive analysis of reference formatting

## 🛠️ Installation & Setup

### Prerequisites

-   Python 3.13+ (specified in pyproject.toml)
-   pip or uv package manager

### Quick Installation

```bash
# Using pip
pip install -r requirements.txt

# Using uv (recommended for faster installs)
uv pip install -r requirements.txt
```

### Dependencies

-   `python-docx>=1.2.0` - Core Word document manipulation

## 🎯 Usage Guide

### 🌟 Complete Processing (Recommended)

```bash
# Full optimization pipeline: autofix → line breaks → formatting → analysis
python src/main.py my_report.docx complete
```

### 🔧 Individual Processing Options

#### Automatic Language & Citation Fixing

```bash
python src/main.py my_report.docx autofix
# Output: auto_fixed_my_report.docx
```

#### Academic Line Break Optimization

```bash
python src/main.py my_report.docx linebreaks
# Output: line_break_fixed_my_report.docx
```

#### Document Formatting

```bash
python src/main.py my_report.docx format
# Output: formatted_my_report.docx
```

#### Language & Citation Analysis

```bash
python src/main.py my_report.docx analyze
# Provides detailed analysis without modifications
```

### 🔬 Advanced Individual Tools

#### Enhanced Auto-Fix Tool

```bash
python src/enhanced_academic_tools.py my_report.docx
python src/enhanced_academic_tools.py my_report.docx -o custom_output.docx
```

#### Academic Line Break Manager

```bash
python src/academic_line_break_manager.py my_report.docx
python src/academic_line_break_manager.py my_report.docx --output custom_output.docx
```

#### Document Formatter

```bash
python src/document_formatter.py my_report.docx
python src/document_formatter.py my_report.docx -o custom_output.docx
```

#### Academic Analysis Tools

```bash
python src/academic_tools.py my_report.docx
```

## 📊 Processing Pipeline & Output

### 🔄 Complete Processing Workflow

1. **Auto-Fix Phase**: Language correction and citation formatting
2. **Line Break Optimization**: Academic spacing standards application
3. **Document Formatting**: IOST style compliance
4. **Analysis & Validation**: Comprehensive quality assessment

### 📁 Output Files Generated

-   `final_[filename].docx` - Complete processed document (recommended)
-   `auto_fixed_[filename].docx` - Language and citation corrections
-   `line_break_fixed_[filename].docx` - Academic spacing applied
-   `formatted_[filename].docx` - IOST formatting applied
-   `backup_[filename].docx` - Original document backup

## 🎯 Intelligent Content Recognition

### 📖 Automatic Detection & Processing

#### Chapter Structures

-   **Chapter Headings**: "Chapter 1", "CHAPTER 2", "chapter 3"
-   **Major Sections**: "1. Introduction", "2. Literature Review"
-   **Section Headings**: "1.1 Background", "2.3 Methodology"
-   **Subsections**: "1.1.1 Problem Statement", "2.3.4 Data Analysis"

#### Academic Elements

-   **Figures**: "Figure 2.1: System Architecture"
-   **Tables**: "Table 3.1: Comparison Results"
-   **Block Quotes**: Indented quotations with proper spacing
-   **List Items**: Bulleted and numbered lists
-   **Citations**: APA format detection and validation

#### Language Corrections

-   **First-Person Conversion**: "I implemented" → "The implementation involved"
-   **Contraction Expansion**: "don't" → "do not", "can't" → "cannot"
-   **Academic Tone**: "very important" → "significant", "big" → "substantial"
-   **URL Citations**: Bare URLs → Proper citation format

### 📏 Line Break Standards Applied

-   **Chapter Headings**: 2 line breaks before, 1 after
-   **Major Sections**: 2 line breaks before, 1 after
-   **Section Headings**: 1 line break before, none after
-   **Subsections**: 1 line break before, none after
-   **Figures/Tables**: 1 line break before and after
-   **Block Quotes**: 1 line break before and after
-   **Regular Paragraphs**: Standard academic spacing

## 🏗️ Project Architecture

### 📂 Core Components

```
src/
├── __init__.py                      # 📦 Package initialization
├── main.py                          # 🎯 Main processing pipeline
├── document_formatter.py            # 🔧 IOST formatting engine
├── enhanced_academic_tools.py       # 🤖 AI-powered auto-fix system
├── academic_tools.py               # 📝 Language & citation analysis
├── academic_line_break_manager.py  # 📏 Line break optimization
├── spacing_optimizer.py            # 📐 Advanced spacing control
├── page_break_manager.py           # 📄 Page break management
├── format_document.py              # 🔧 Simple formatting utility
└── install_dependencies.py         # 📦 Dependency installer

tests/
├── __init__.py                     # 📦 Test package initialization
├── run_tests.py                    # 🧪 Comprehensive test runner
├── test_document_formatter_fix.py  # 🧪 Formatter validation
├── test_line_breaks.py             # 🧪 Line break system tests
├── test_section_breaks.py          # 🧪 Section break tests
├── test_page_breaks.py             # 🧪 Page break testing
├── test_spacing.py                 # 🧪 Spacing validation
└── test_setup.py                   # 🧪 Test configuration

Root Files:
├── pyproject.toml                  # 📦 Project configuration
├── requirements.txt                # 📦 Dependencies
├── uv.lock                        # 🔒 Dependency lock file
└── README.md                      # 📖 Project documentation
```

### 🔧 System Architecture

#### Processing Layers

1. **Input Layer**: Document ingestion and validation
2. **Analysis Layer**: Content type recognition and structure analysis
3. **Correction Layer**: Automatic language and citation fixes
4. **Formatting Layer**: IOST compliance application
5. **Optimization Layer**: Line breaks, spacing, and page breaks
6. **Output Layer**: Final document generation and validation

#### Key Classes & Functions

-   `IOSTDocumentFormatter`: Core formatting engine
-   `DocumentAutoFixer`: AI-powered text correction
-   `AcademicLineBreakManager`: Line break optimization
-   `LanguageChecker`: Academic writing analysis
-   `CitationChecker`: APA format validation

## 🛠️ Recommended Complementary Tools

### 📚 Citation Management

-   **Zotero** (Free, open-source) - Best for academic research
-   **Mendeley** (Free/Premium) - Good collaboration features
-   **EndNote** (Paid) - Industry standard for institutions

### ✍️ Writing Enhancement

-   **Grammarly** (Free/Premium) - Grammar and style checking
-   **LanguageTool** (Free/Premium) - Multi-language grammar checker
-   **Hemingway Editor** - Readability and clarity improvement
-   **ProWritingAid** - Comprehensive writing analysis

### 📖 Academic Style Resources

-   **APA Style Guide** (Official) - Authoritative style reference
-   **Purdue OWL** (Free) - Comprehensive APA guidelines
-   **Chicago Manual of Style** - Alternative academic style
-   **MLA Handbook** - Literature and humanities style

## 📋 Example Processing Output

### 🚀 Complete Processing Session

```
IOST BSc CSIT Internship Report Processor
==================================================

🤖 AUTO-FIXING LANGUAGE & CITATIONS
----------------------------------------
🔧 Auto-fixing document: my_report.docx
============================================================
📋 Backup created: backup_my_report.docx

🎉 AUTO-FIX COMPLETED!
� SNtatistics:
   - Paragraphs modified: 23
   - Total fixes applied: 47
   - Output file: final_my_report.docx

📝 DETAILED FIXES:
----------------------------------------

Paragraph 15:
Preview: I implemented the user authentication system using Django...
  ✓ First Person Fix: 'I implemented' → 'The implementation involved'
    Context: Converted to passive voice
  ✓ Contraction Fix: 'don't' → 'do not'
    Context: Expanded contraction for formal writing

Paragraph 23:
Preview: More information can be found at https://django.com/docs...
  ✓ Url Citation Fix: 'https://django.com/docs' → '(Django Software Foundation, retrieved from https://django.com/docs)'
    Context: Converted bare URL to proper citation format

📏 APPLYING ACADEMIC LINE BREAKS
----------------------------------------
� ACADEMICD LINE BREAK PROCESSING
============================================================
Processing: final_my_report.docx

🔧 PRESERVING EXISTING SECTION BREAKS
----------------------------------------
   ✅ Found 3 section breaks to preserve:
      - Section 1: Section break (next page)
      - Section 2: Section break (next page)
      - Section 3: Section break (continuous)

📏 APPLYING ACADEMIC LINE BREAK STANDARDS
==================================================
   ✅ Fixed chapter_heading: Chapter 1: Introduction...
      → Spacing before: 0pt → 36pt
   ✅ Fixed major_section: 1. Literature Review...
      → Spacing before: 6pt → 36pt
   ✅ Fixed section_heading: 1.1 Background...
      → Spacing before: 0pt → 18pt

🧹 REMOVING EXCESSIVE EMPTY PARAGRAPHS
----------------------------------------
   ✅ Removed 12 excessive empty paragraphs

📄 ADDING REQUIRED PAGE BREAKS
-----------------------------------
   ✅ Added page break before: Chapter 2: Methodology...
   ✅ Added page break before: Chapter 3: Implementation...

🎉 LINE BREAK PROCESSING COMPLETED!
==================================================
   📝 Line break corrections: 34
   🧹 Empty paragraphs removed: 12
   📄 Page breaks added: 2
   💾 Saved as: final_my_report.docx

🔧 FORMATTING DOCUMENT
------------------------------
Setting page margins...
Cleaning unnecessary page breaks...
Removing excessive empty paragraphs...
Adding proper chapter page breaks...
Formatting paragraphs...
Fixing heading line breaks...
Formatting tables...
Applying IOST spacing standards...
Document formatting completed!
✅ Final formatted document saved as: final_my_report.docx

🔍 ANALYZING DOCUMENT
------------------------------
Analyzing document: final_my_report.docx
============================================================

📝 LANGUAGE ANALYSIS
------------------------------
✅ No language issues found!

📚 CITATION ANALYSIS
------------------------------
✅ Found 15 properly formatted citations
✅ No citation issues found!

🔧 RECOMMENDATIONS
------------------------------
For better academic writing:
• Use Grammarly or LanguageTool for grammar checking
• Use Zotero, Mendeley, or EndNote for citation management
• Consider Hemingway Editor for readability
• Use passive voice in technical descriptions
• Ensure all sources are properly cited in APA format

==================================================
PROCESSING COMPLETED!
==================================================
📄 Final document: final_my_report.docx

📋 NEXT STEPS:
1. Review the final document for accuracy
2. Manually adjust page numbering (Roman/Arabic)
3. Add proper page breaks for chapters
4. Verify figure and table positioning
5. Check that auto-fixes maintain original meaning
```

## 🧪 Testing & Quality Assurance

### 🔬 Comprehensive Test Suite

```bash
# Run all tests with comprehensive test runner
python tests/run_tests.py

# Run individual test modules
python tests/test_line_breaks.py
python tests/test_document_formatter_fix.py
python tests/test_section_breaks.py
python tests/test_page_breaks.py
python tests/test_spacing.py

# Run tests using pytest (if installed)
python -m pytest tests/
```

### 🎯 Test Coverage

-   **Line Break Standards**: Academic spacing validation
-   **Document Formatting**: IOST compliance verification
-   **Language Corrections**: Auto-fix accuracy testing
-   **Section Breaks**: Google Docs import compatibility
-   **Integration Testing**: Full pipeline validation

## ⚠️ Known Limitations & Manual Steps

### 🔧 Requires Manual Attention

-   **Page Numbering**: Roman numerals for preliminary pages (abstract, acknowledgments)
-   **Complex Tables**: Multi-page tables may need positioning adjustment
-   **Figure Placement**: Large figures might require manual positioning
-   **Reference Section**: Final APA format verification recommended
-   **Chapter Numbering**: Verify sequential chapter numbering

### 🎯 System Limitations

-   **Citation Validation**: Basic APA checking (use Zotero/Mendeley for comprehensive validation)
-   **Language Context**: Auto-fixes preserve meaning but manual review recommended
-   **Complex Formatting**: Nested lists and special formatting may need adjustment
-   **Document Corruption**: Always creates backups, but complex documents may have edge cases

## 🚀 Advanced Features & Tips

### 💡 Pro Tips for Best Results

1. **Start with Clean Document**: Remove manual formatting before processing
2. **Use Consistent Headings**: Follow "Chapter X", "X.Y", "X.Y.Z" patterns
3. **Backup Important Work**: Tool creates backups, but keep your own copies
4. **Review Auto-Fixes**: Check that meaning is preserved after language corrections
5. **Process Incrementally**: Use individual tools for fine-tuned control

### 🔧 Troubleshooting Common Issues

-   **Import Errors**: Ensure all dependencies are installed (`pip install -r requirements.txt`)
-   **File Access**: Close Word document before processing
-   **Memory Issues**: Large documents may require processing in sections
-   **Formatting Conflicts**: Remove existing styles before applying IOST formatting

## 🤝 Contributing & Development

### 🛠️ Development Setup

```bash
# Clone and setup development environment
git clone <repository-url>
cd intern-report-generator
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 🎯 Contribution Areas

-   **Language Models**: Improve auto-fix accuracy
-   **Citation Formats**: Add support for other academic styles
-   **Testing**: Expand test coverage for edge cases
-   **Documentation**: Improve user guides and examples
-   **Performance**: Optimize processing for large documents

### 📝 Code Style

-   Follow PEP 8 Python style guidelines
-   Add docstrings for all functions and classes
-   Include type hints where appropriate
-   Write comprehensive tests for new features

## 📄 License & Acknowledgments

### 📜 License

This project is provided as-is for educational purposes under the MIT License.

### 🙏 Acknowledgments

-   **IOST, Tribhuvan University** - For academic formatting standards
-   **python-docx Community** - For excellent Word document manipulation library
-   **Academic Writing Community** - For best practices and standards
-   **Open Source Contributors** - For tools and libraries that make this possible

### 📞 Support & Contact

For issues, suggestions, or contributions:

-   Create GitHub issues for bug reports
-   Submit pull requests for improvements
-   Follow academic writing best practices
-   Share feedback for continuous improvement

---

**Made with ❤️ for IOST BSc CSIT students and academic excellence**
