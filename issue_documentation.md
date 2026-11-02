# Lab 5 – Static Code Analysis: Issue Documentation

**Repository:** `L5_36_smart_home_PES1UG24CS460`  
**Program:** `smart_home.py`

## Pylint Findings

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Missing module docstring | Code Quality | 1 | Module did not have a description. | Added a module-level docstring. |
| Missing function docstrings | Code Quality | Multiple | Functions did not describe their purpose. | Added docstrings to all functions. |
| Invalid naming conventions | Code Quality | Multiple | Function and argument names used camelCase. | Converted names to snake_case. |
| Mutable default argument | Bug | 11 | Empty dictionary was shared across function calls. | Changed default to `None` and initialized inside the function. |
| Inconsistent return statements | Code Quality | 16–20 | Function did not return a value in every execution path. | Added an explicit `False` return. |
| Unspecified encoding | Code Quality | 41 | File was opened without specifying encoding. | Added `encoding="utf-8"`. |

## Bandit Findings

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| B404 – Subprocess import | Security | 2 | Importing subprocess can introduce security risks. | Removed unnecessary subprocess import. |
| B104 – Hardcoded bind address | Security | 4 | `0.0.0.0` allows connections through all network interfaces. | Changed host to `127.0.0.1`. |
| B105 – Hardcoded password | Security | 7 | Password was directly stored in source code. | Used an environment variable with `os.getenv()`. |
| B602 – Shell execution | Security | 51 | `shell=True` can expose the application to command injection. | Removed shell execution and added scene script name validation. |

## Flake8 Findings

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| E203 – Whitespace before colon | Formatting | 6 | Unnecessary whitespace before a dictionary colon. | Removed extra whitespace. |
| E302 – Incorrect blank lines | Formatting | 40 | Function definition lacked required blank lines. | Added required blank lines. |
| E261 – Inline comment spacing | Formatting | 66 | Insufficient spacing before inline comment. | Added two spaces before the comment. |
| E501 – Line too long | Formatting | 68 | Line exceeded the 79-character limit. | Split the statement across multiple lines. |
| E122 – Continuation indentation | Formatting | 94 (during fixing) | Continued line had incorrect indentation. | Corrected multiline list indentation. |

## Final Verification Results

| Tool | Before | After |
|---|---|---|
| Pylint | 4.80/10 | **10.00/10** |
| Bandit | 4 findings | **0 findings** |
| Flake8 | 4 initial violations | **0 violations** |

## Conclusion

Static code analysis helped identify code quality issues, security vulnerabilities and formatting violations in the smart home application. The identified issues were fixed using Pylint, Bandit and Flake8.

The final program achieved a Pylint score of 10.00/10, zero Bandit security findings and zero Flake8 formatting errors. The program was also tested after modifications to ensure its original demonstration functionality was preserved.
