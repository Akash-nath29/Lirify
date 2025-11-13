# Codebase Security Scan Results

Scan Date: 11/12/2025, 11:36:42 AM
Total Files Scanned: 8
Files with Vulnerabilities: 4
Total Vulnerabilities Found: 13
Total Lines of Code: 384

---

## File: test.java

**Lines of Code**: 83

### Vulnerability 1
- **Line**: 18
- **Type**: Hardcoded Secrets
- **Severity**: high
- **Description**: Hardcoded database password 'password123' exposes credentials and should be stored securely.

### Vulnerability 2
- **Line**: 31
- **Type**: SQL Injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query without sanitization, allowing SQL injection attacks.

### Vulnerability 3
- **Line**: 51
- **Type**: Arbitrary File Write
- **Severity**: high
- **Description**: User-provided username is used to write to a file without validation, risking unauthorized file access.

### Vulnerability 4
- **Line**: 58
- **Type**: Insecure Deserialization
- **Severity**: high
- **Description**: Untrusted serialized data is deserialized without validation, which can lead to arbitrary code execution.

### Vulnerability 5
- **Line**: 70
- **Type**: Arbitrary File Write
- **Severity**: medium
- **Description**: User input is used directly in file path construction, leading to potential path traversal vulnerabilities.

---

## File: test1.py

**Lines of Code**: 36

### Vulnerability 1
- **Line**: 20
- **Type**: SQL Injection
- **Severity**: high
- **Description**: User input is directly concatenated into SQL query without sanitization, allowing SQL injection attacks.

### Vulnerability 2
- **Line**: 32
- **Type**: Command Injection
- **Severity**: high
- **Description**: User input is directly passed to os.system() without sanitization, allowing arbitrary command execution.

### Vulnerability 3
- **Line**: 13
- **Type**: Hardcoded Secrets
- **Severity**: high
- **Description**: Admin password is hardcoded directly in the source code, exposing it to anyone with access to the code.

### Vulnerability 4
- **Line**: 7
- **Type**: Broken Authentication
- **Severity**: medium
- **Description**: Database connection is created without proper thread safety, and credentials are stored in plain text.

---

## File: test.cpp

**Lines of Code**: 30

### Vulnerability 1
- **Line**: 11
- **Type**: buffer overflow
- **Severity**: high
- **Description**: Use of strcpy without bounds checking can lead to buffer overflow and potential code execution.

---

## File: backend/app.py

**Lines of Code**: 157

### Vulnerability 1
- **Line**: 51
- **Type**: arbitrary file write
- **Severity**: high
- **Description**: Loading model file 'lyrics_gen.keras' without validation. If this file is user-controllable or comes from an untrusted source, it could lead to arbitrary code execution during model loading.

### Vulnerability 2
- **Line**: 24
- **Type**: arbitrary file write
- **Severity**: high
- **Description**: Reading CSV file 'dataset.csv' without validation. If this file is user-controllable or comes from an untrusted source, it could lead to arbitrary code execution or data leakage.

### Vulnerability 3
- **Line**: 57
- **Type**: broken authentication
- **Severity**: medium
- **Description**: CORS policy allows all origins ('*'), which can lead to security issues if the API is intended for restricted access only. This could enable unauthorized domains to interact with the API.

---

