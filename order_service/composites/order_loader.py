from order_service.composites.app_api import Application as app

info = {
        "type": "service_account",
        "project_id": "test-project-354211",
        "private_key_id": "cb36a28d9ffef00e681cabec142abd643123690b",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCmJnAFmR7P6CqO\n4VX1haGr/2tgAmwsRE9dbmTnqKqnhEsscIeyul7WVRxlQCv+0n6ZNlFHefu+kqUi\nXlLXEV8QQF4fhFpXu+jQTE4lL/24Amy2MKreN04y7Vwbqnci+I5JzBPaEeUYSuAt\nLmrh+GNe32F/8y8vbzOq4j018jgt+DMF3FdSGLvanIN3kt+jxZVucPJYCw9PjiaU\nFq/zrzU6BhOmlGc4iXdd2x8PciU/97k8aCfhnu8MiNOXXCiTtqp8sYY6ZoiRwN24\n6zsLcv2HBxXDYyrO1pN0TMzwPc6KnME6vMGChqkUacteH8bgQD1VaPvuYUs65T2b\nG4Fqqs9PAgMBAAECggEAJTGvnCE1+5beiBO7mXXrxkQsdla0fohgN+sxnYZthYih\nB3a9ee4sstBkxenCr43Rl1zIfza4e2X6n6H763dRD6NJLscDLma7bH3YdIy0wI+S\nZIqqhYpd8BqgpvTXLLX1rGGKBCRDY9fHLXYZqTJglGlvOyRmaLj9GQECcOQjXW64\ngBoyk0rIRl8FEIKK7Ar7Y8MpPNqKKs2oUb68oG+S/ZBWf4XQ457aA27CVzPtcG2+\nbkOMbFuJbtDf3vKtb6l2kBZwykABrYlRJLGwwSb996zWtBK7Ucx7eOhV+AfxtMIs\nx7G5/bOWW40AmRDL9d6BGyaAblDOpz6ri9qd8+RHUQKBgQDo4nOpkeyzfIS1zH6t\nfPCjTa8wXNbDlKHm9+5JQIPv+XRHo/APU5IdJkHL4BWifJI9v3Mgj13srjExopBq\nj3JAb6KnjjMWyTFOOKshiSFCMTIDcFN4M5xTIyVSxQ4cAXBtjuSC2lc5Jz6k6qRU\niGRgpSqxy+ZN94Id0fEjgrZVFwKBgQC2pEcliD2PNrjWEdPnofBeY3BWwSdvbPZH\nnLuQFjnH7aTwFKTt7yBUeKvyiJNO4Ui19fyJjDi0/eToisgAWnOX7uxFEjI5aZV2\nyt3r6qLaFkAHnLCtzGu7pHp3+yrIAPcdP7gtoufOcocogko0OqzjhGZcVmxQnjkc\nE8+mm9qqiQKBgDM/kiBgwmwFHNc89yuKcRIeyEymQYSssqw3JzLrhZ1LkfEp/GwD\nAgZ0IsqQt3IYY74+4UDrC8pH0v+PPKSWiJfxeSPSQR/kinsiMVah7LW6Sb1D/LpY\n8S/CbjY2sxIqpukVJug80DD9l+WG1T7c/OnfrvONYVMLApE5YA1meGVlAoGAKIJ3\nZVO6k7FHffOmVJIOhmD34cYlwQkh9vBEicjkN/v1wWpSypNnUFUTjk/MnIpLXlCZ\nGskHKt3Fj+54PdvSF7jentNSYHmStS552oHIbSbSPN38MhBNNOleYI5NBt9v8ATa\nDQU89QViBRIg80SwZCZRrdldXOQ7NocOX53h+kECgYBc+4wt70PKLbj4XQoYq2d3\noPrh2TFlLh7w+p7MH3wPtWQs/wvDmrk0QVIwTmlpWD4sZ2QYYFJCcF4JNiUDU093\nE0NcodQSgUTTiAwNYiDUQcPHdKcMAVd+OHYBJvjLnNsTv5dUp0f/hB9Bm7BS4txS\nGWOwLY3ASNf6jPffIvHmkA==\n-----END PRIVATE KEY-----\n",
        "client_email": "test-account@test-project-354211.iam.gserviceaccount.com",
        "client_id": "112743463147029212273",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-account%40test-project-354211.iam.gserviceaccount.com"
    }
def get_order():
        while True:
                app.orders.get_orders(info)

