
try:
    import ssl
    print('imported')
    SSLContext = ssl.SSLContext
    print('1:',SSLContext)
except ImportError:  # pragma: no cover
    ssl = None  # type: ignore
    print('nope:',ssl)
    SSLContext = object # type: ignore
    print('2:',SSLContext)
