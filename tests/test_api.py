# ... existing code ...
failure = FailureHost(host='revoked.badssl.com', error_messages=[
    '"revoked.badssl.com" certificate is revoked',
    'Fatal trust failure occurred',
    'The certificate is revoked.',
    'Missing Authority Key Identifier',
    'certificates do not meet pinning requirements',
    'Basic Constraints of CA cert not marked critical'
])
# ... existing code ...