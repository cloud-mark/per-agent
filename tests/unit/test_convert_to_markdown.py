# Generated by CodiumAI
from pr_agent.algo.utils import convert_to_markdown
import pytest
"""
Code Analysis

Objective:
The objective of the 'convert_to_markdown' function is to convert a dictionary of data into a markdown-formatted text. 
The function takes in a dictionary as input and recursively iterates through its keys and values to generate the 
markdown text.

Inputs:
- A dictionary of data containing information about a pull request.

Flow:
- Initialize an empty string variable 'markdown_text'.
- Create a dictionary 'emojis' containing emojis for each key in the input dictionary.
- Iterate through the input dictionary:
  - If the value is empty, continue to the next iteration.
  - If the value is a dictionary, recursively call the 'convert_to_markdown' function with the value as input and 
  append the returned markdown text to 'markdown_text'.
  - If the value is a list:
    - If the key is 'code suggestions', add an additional line break to 'markdown_text'.
    - Get the corresponding emoji for the key from the 'emojis' dictionary. If no emoji is found, use a dash.
    - Append the emoji and key to 'markdown_text'.
    - Iterate through the items in the list:
      - If the item is a dictionary and the key is 'code suggestions', call the 'parse_code_suggestion' function with 
      the item as input and append the returned markdown text to 'markdown_text'.
      - If the item is not empty, append it to 'markdown_text'.
  - If the value is not 'n/a', get the corresponding emoji for the key from the 'emojis' dictionary. If no emoji is 
  found, use a dash. Append the emoji, key, and value to 'markdown_text'.
- Return 'markdown_text'.

Outputs:
- A markdown-formatted string containing the information from the input dictionary.

Additional aspects:
- The function uses recursion to handle nested dictionaries.
- The 'parse_code_suggestion' function is called for items in the 'code suggestions' list.
- The function uses emojis to add visual cues to the markdown text.
"""


class TestConvertToMarkdown:
    # Tests that the function works correctly with a simple dictionary input
    def test_simple_dictionary_input(self):
        input_data = {
            'Main theme': 'Test',
            'Description and title': 'Test description',
            'Type of PR': 'Test type',
            'Relevant tests added': 'no',
            'Unrelated changes': 'n/a',  # won't be included in the output
            'Focused PR': 'Yes',
            'General PR suggestions': 'general suggestion...',
            'Code suggestions': [
                {
                    'Suggestion number': 1,
                    'Code example': {
                        'Before': 'Code before',
                        'After': 'Code after'
                    }
                },
                {
                    'Suggestion number': 2,
                    'Code example': {
                        'Before': 'Code before 2',
                        'After': 'Code after 2'
                    }
                }
            ]
        }
        expected_output = """\
- 🎯 **Main theme:** Test
- 🔍 **Description and title:** Test description
- 📌 **Type of PR:** Test type
- 🧪 **Relevant tests added:** no
- ✨ **Focused PR:** Yes
- 💡 **General PR suggestions:** general suggestion...

- 🤖 **Code suggestions:**

  - **Code example:**
    - **Before:**
        ```
        Code before
        ```
    - **After:**
        ```
        Code after
        ```

  - **Code example:**
    - **Before:**
        ```
        Code before 2
        ```
    - **After:**
        ```
        Code after 2
        ```
"""
        assert convert_to_markdown(input_data).strip() == expected_output.strip()

    # Tests that the function works correctly with an empty dictionary input
    def test_empty_dictionary_input(self):
        input_data = {}
        expected_output = ""
        assert convert_to_markdown(input_data).strip() == expected_output.strip()

    def test_dictionary_input_containing_only_empty_dictionaries(self):
        input_data = {
            'Main theme': {},
            'Description and title': {},
            'Type of PR': {},
            'Relevant tests added': {},
            'Unrelated changes': {},
            'Focused PR': {},
            'General PR suggestions': {},
            'Code suggestions': {}
        }
        expected_output = ""
        assert convert_to_markdown(input_data).strip() == expected_output.strip()
