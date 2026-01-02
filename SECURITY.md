# Security Policy

## Supported Versions

We actively support the following versions of Grandmaster Chess Suite:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in Grandmaster Chess Suite, please follow these steps:

1. **Do NOT** open a public issue
2. Email security details to: [your-email@example.com]
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Resolution**: Depends on severity

### Severity Levels

- **Critical**: Remote code execution, data breach
- **High**: Significant functionality compromise
- **Medium**: Limited functionality impact
- **Low**: Minor issues, edge cases

## Security Best Practices

This is a client-side application. For security:

1. **Do not** store sensitive data in localStorage
2. **Do not** trust client-side validation alone
3. **Do not** expose API keys or secrets in code
4. Always validate user input
5. Use HTTPS when deploying

## Known Security Considerations

- This is a **client-side only** application
- No server-side components (unless using optional server.py)
- All game logic runs in the browser
- No user data is collected or transmitted

## Updates

Security updates will be released as patches. Please keep your version updated.

---

**Thank you for helping keep Grandmaster Chess Suite secure!**
