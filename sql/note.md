- Contains various sql problems and solution
- This problems will help revisit/learn edge cases,
important kind of quires.


# Markdown (.md) Cheat Sheet: Plain Text Formatting

Core Concept: 
- Markdown files (.md or .markdown) are just plain text files. 
- You write special characters (like #, *, [, ]) directly in the text, and a Markdown renderer (like GitHub, a text editor, or a website) then converts those characters into rich-text formatting (like bold text, headings, or links) for display.

### 1. Headings (Sizing Your Sections)

Syntax: 
- Use # symbols at the beginning of a line. The more #s, the smaller the heading.
Plain Text Example:
Plaintext
# Main Title
## Subheading
### Sub-subheading
#### Even Smaller
What it means: These are plain text markers that a Markdown renderer understands as HTML <h1>, <h2>, <h3>, etc.

## 3. Text Styling (Emphasis)

Syntax: Wrap text with * or _ for italic/bold, ~~ for strikethrough.
Plain Text Example:
Plaintext
This is *italic text* or _italic text_.
This is **bold text** or __bold text__.
This is ***bold and italic***.
This is ~~strikethrough~~.
What it means: These are plain text delimiters. The renderer sees *text* and makes it text.
3. Lists (Organizing Items)

Syntax: Use *, -, + for unordered lists; numbers followed by . for ordered lists. Indent for nested lists.
Plain Text Example:
Plaintext
* Item one
* Item two
    * Nested item 2.1
    * Nested item 2.2
1. First step
2. Second step
    1. Sub-step A
    2. Sub-step B
What it means: The leading characters *, -, +, 1., 2. tell the renderer to create <ul> (unordered) or <ol> (ordered) HTML lists.
4. Links (Connecting to Other Places)

Syntax: [Link Text](URL "Optional Title")
Plain Text Example:
Plaintext
Visit [Google](https://www.google.com "Search Engine") for more info.
What it means: The [ ] contains what the user sees, and the ( ) contains the web address. It's a simple, human-readable way to embed links in plain text.
5. Images (Displaying Pictures)

Syntax: ![Alt Text](URL_to_Image "Optional Title")
Plain Text Example:
Plaintext
![A beautiful sunset](https://example.com/sunset.jpg "Sunset over the ocean")
What it means: Similar to links, but with an ! in front. The Alt Text is what appears if the image doesn't load or for screen readers.
6. Code Blocks (Showing Code or Preformatted Text)

Syntax: Use backticks ` for inline code. For multi-line code blocks, use three backticks ``` ` `` on lines by themselves.
Plain Text Example (Inline):
Plaintext
Use `print()` for output.
Plain Text Example (Block - with optional language for syntax highlighting):
Plaintext
```python
def hello_world():
    print("Hello, Markdown!")
 (Note: The lines with three backticks are literally in the file.)
What it means: Backticks tell the renderer to display the enclosed text as fixed-width, monospaced font, often for code. Three backticks create a block, and the word after the opening backticks hints at the programming language.
```
# 7. Blockquotes (Quoting Text)

Syntax: Start a line with >.
Plain Text Example:
Plaintext
> This is a quoted passage.
> It can span multiple lines.
>
>> And can be nested.
What it means: The > character marks the text as a quotation, often rendered with an indentation or a special visual style.

## 8.Horizontal Rule / Thematic Break (Dividing Sections)

Syntax: Three or more hyphens, asterisks, or underscores on a line by themselves.
- Plain Text Example:
Plaintext
---
***
___
What it means: These are simple markers to draw a horizontal line across the page, acting as a visual separator.
## 9.Tables (Structured Data - GitHub Flavored Markdown)

Syntax: Use | for columns and - for header separators.
Plain Text Example:
Plaintext

| Header 1 | Header 2 |
| -------- | -------- |
| Data 1   | Data 2   |
| Data 3   | Data 4   |


What it means: This plain text grid gets converted into an HTML table. The alignment specifiers (:) can be added to the separator line (e.g., |:---|:---:|---:|) to control text alignment within columns.
Key Takeaway: The .md file itself is always a simple, human-readable text file. The magic happens when a program interprets that text and renders it with the intended formatting. This makes Markdown incredibly versatile for documentation, notes, and web content.