
#!/usr/bin/env python3
# Test CodeTF for parsing C++ code

# pip install -q -U git+https://github.com/huggingface/transformers.git

import sys
from pathlib import Path

from codetf.models import model_zoo

from codetf.code_utility.apex.apex_code_utility import ApexCodeUtility

apex_code_utility = ApexCodeUtility()

sample_code = """
    public class SampleClass {    
        public Integer myNumber;
        
        **
        * This is a method that returns the value of myNumber.
        * @return An integer value
        */
        public Integer getMyNumber() {
            // Return the current value of myNumber
            return this.myNumber;
        }
    }
"""
ast = apex_code_utility.parse(sample_code)

# This will print the tree-sitter AST object
print(ast)
