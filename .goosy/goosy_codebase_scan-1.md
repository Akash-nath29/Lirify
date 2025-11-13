# Codebase Security Scan #1

Scan Date: 11/13/2025, 11:05:00 AM
Total Files Scanned: 8
Files with Vulnerabilities: 4
Total Vulnerabilities Found: 11
Total Lines of Code: 384

---

## File: test2.py

**Lines of Code**: 31

### Vulnerability 1
- **Line**: 10
- **Type**: AttributeError
- **Severity**: high
- **Description**: Attempting to call 'append' method on a set object, which will raise an AttributeError. Should use 'add' method instead.

---

## File: test.java

**Lines of Code**: 83

### Vulnerability 1
- **Line**: 30
- **Type**: SQL Injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query without sanitization, allowing SQL injection attacks.

### Vulnerability 2
- **Line**: 20
- **Type**: Hardcoded Secrets
- **Severity**: high
- **Description**: Database credentials are hardcoded directly in the source code, exposing sensitive information.

### Vulnerability 3
- **Line**: 45
- **Type**: Insecure Deserialization
- **Severity**: high
- **Description**: Unvalidated user-supplied file is deserialized, which can lead to arbitrary code execution.

### Vulnerability 4
- **Line**: 56
- **Type**: Arbitrary File Write
- **Severity**: high
- **Description**: User-controlled input is used directly in file path, allowing arbitrary file write to predictable location.

### Vulnerability 5
- **Line**: 35
- **Type**: Broken Authentication
- **Severity**: medium
- **Description**: Passwords are stored in plain text in a file, leading to credential exposure.

---

## File: test.cpp

**Lines of Code**: 30

### Vulnerability 1
- **Line**: 11
- **Type**: buffer overflow
- **Severity**: high
- **Description**: strcpy() used without bounds checking, vulnerable to buffer overflow attack

---

## File: test1.py

**Lines of Code**: 36

### Vulnerability 1
- **Line**: 25
- **Type**: SQL Injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query without sanitization, allowing SQL injection attacks

### Vulnerability 2
- **Line**: 34
- **Type**: Command Injection
- **Severity**: high
- **Description**: User input is directly passed to os.system() without validation or sanitization, allowing arbitrary command execution

### Vulnerability 3
- **Line**: 12
- **Type**: Hardcoded Secrets
- **Severity**: high
- **Description**: Administrator credentials are hardcoded directly in the source code

### Vulnerability 4
- **Line**: 37
- **Type**: Broken Authentication
- **Severity**: medium
- **Description**: Passwords are stored and compared in plain text without hashing or encryption

---

