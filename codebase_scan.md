# Codebase Security Scan Results

Scan Date: 10/25/2025, 3:04:06 AM
Total Files Scanned: 8
Files with Vulnerabilities: 3
Total Vulnerabilities Found: 9
Total Lines of Code: 384

---

## test.java

**Lines of Code**: 83

### Vulnerability 1
- **Line**: 8
- **Type**: hardcoded secret
- **Severity**: high
- **Description**: Hardcoded database credentials (DB_USER and DB_PASS) expose sensitive information.

### Vulnerability 2
- **Line**: 22
- **Type**: sql injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query, allowing SQL Injection.

### Vulnerability 3
- **Line**: 37
- **Type**: arbitrary file write
- **Severity**: high
- **Description**: User credentials are written to a file without proper protection, leading to possible exposure of sensitive data.

### Vulnerability 4
- **Line**: 43
- **Type**: insecure deserialization
- **Severity**: high
- **Description**: Untrusted user input is used to load and deserialize a file, allowing arbitrary code execution.

### Vulnerability 5
- **Line**: 52
- **Type**: arbitrary file write
- **Severity**: high
- **Description**: Username is used directly in file path creation, allowing arbitrary file write in /tmp directory.

---

## test.cpp

**Lines of Code**: 30

### Vulnerability 1
- **Line**: 10
- **Type**: Arbitrary File Write
- **Severity**: high
- **Description**: strcpy is used to copy user-controlled input into a fixed-size buffer without bounds checking, leading to a classic stack-based buffer overflow vulnerability. This can allow code execution or arbitrary function calls.

---

## ahgdja.py

**Lines of Code**: 36

### Vulnerability 1
- **Line**: 12
- **Type**: hardcoded_secret
- **Severity**: high
- **Description**: Hardcoded admin credentials (ADMIN_PASS) can be easily extracted and used by attackers.

### Vulnerability 2
- **Line**: 19
- **Type**: sql_injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query, allowing SQL injection via username or password.

### Vulnerability 3
- **Line**: 29
- **Type**: command_injection
- **Severity**: high
- **Description**: User input is passed directly to os.system(), allowing command injection.

---

