# Codebase Security Scan #3

Scan Date: 11/13/2025, 2:23:33 PM
Total Files Scanned: 8
Files with Vulnerabilities: 4
Total Vulnerabilities Found: 11
Total Lines of Code: 384

---

## File: test1.py

**Lines of Code**: 36

### Vulnerability 1
- **Line**: 13
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded admin password found; storing secrets in code is insecure and can lead to credential compromise.

### Vulnerability 2
- **Line**: 20
- **Type**: sql_injection
- **Severity**: high
- **Description**: User input is directly interpolated into SQL query, allowing attackers to perform SQL injection.

### Vulnerability 3
- **Line**: 32
- **Type**: command_injection
- **Severity**: high
- **Description**: User input is passed directly to os.system, allowing arbitrary command execution.

---

## File: test.java

**Lines of Code**: 83

### Vulnerability 1
- **Line**: 17
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded database username in source code. Use environment variables or secure vaults instead.

### Vulnerability 2
- **Line**: 18
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded database password in source code. Use environment variables or secure vaults instead.

### Vulnerability 3
- **Line**: 31
- **Type**: sql_injection
- **Severity**: high
- **Description**: SQL query is constructed using unsanitized user input, making it vulnerable to SQL injection. Use prepared statements.

### Vulnerability 4
- **Line**: 52
- **Type**: arbitrary_file_write
- **Severity**: high
- **Description**: User credentials are written to a file without encryption or access control, leading to possible credential leakage.

### Vulnerability 5
- **Line**: 58
- **Type**: insecure_deserialization
- **Severity**: high
- **Description**: Deserializing objects from user-supplied files without validation, allowing for remote code execution via malicious serialized objects.

### Vulnerability 6
- **Line**: 70
- **Type**: arbitrary_file_write
- **Severity**: high
- **Description**: User-controlled filename used to create a file, allowing arbitrary file write in /tmp directory. Validate or sanitize input.

---

## File: test.cpp

**Lines of Code**: 30

### Vulnerability 1
- **Line**: 11
- **Type**: arbitrary code execution (buffer overflow)
- **Severity**: high
- **Description**: strcpy is used to copy user input into a fixed-size buffer without bounds checking, allowing buffer overflow and potential arbitrary code execution.

---

## File: backend/app.py

**Lines of Code**: 157

### Vulnerability 1
- **Line**: 57
- **Type**: vulnerability
- **Severity**: high
- **Description**: CORS policy allows all origins with allow_credentials=True, which can enable cross-site credential theft. Restrict allowed origins to trusted domains.

---

