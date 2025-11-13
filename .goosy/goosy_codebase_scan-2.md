# Codebase Security Scan #2

Scan Date: 11/13/2025, 11:28:14 AM
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
- **Description**: User input is passed directly to os.system(), allowing attackers to execute arbitrary system commands.

---

## File: test.java

**Lines of Code**: 83

### Vulnerability 1
- **Line**: 17
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded database username in source code.

### Vulnerability 2
- **Line**: 18
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded database password in source code.

### Vulnerability 3
- **Line**: 31
- **Type**: sql_injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query, allowing SQL injection.

### Vulnerability 4
- **Line**: 52
- **Type**: arbitrary_file_write
- **Severity**: high
- **Description**: User credentials are written to a file without encryption or access control.

### Vulnerability 5
- **Line**: 58
- **Type**: insecure_deserialization
- **Severity**: high
- **Description**: Untrusted file is deserialized without validation, allowing code execution.

### Vulnerability 6
- **Line**: 70
- **Type**: arbitrary_file_write
- **Severity**: high
- **Description**: Username is used directly in file path, allowing arbitrary file creation.

---

## File: test.cpp

**Lines of Code**: 30

### Vulnerability 1
- **Line**: 11
- **Type**: Arbitrary File Write / Buffer Overflow
- **Severity**: high
- **Description**: Use of strcpy on a fixed-size buffer without bounds checking allows buffer overflow, which can lead to code execution or access to the secret() function.

---

## File: backend/app.py

**Lines of Code**: 157

### Vulnerability 1
- **Line**: 57
- **Type**: vulnerability
- **Severity**: high
- **Description**: CORS policy allows all origins with allow_credentials=True, which can enable cross-site credential theft. Restrict allowed origins to trusted domains.

---

