DEBUG=False
    # bool value
        # True for debug output
ADC_URL='http://192.168.1.1'
    # str value
        # URL to FortiADC Management/API interface
ADC_USERNAME='certificate_admin'
    # str value
        # Administrator account on FortiADC
        # Account requires only System Read-Write Access Profile
ADC_PASSWORD='ChangeThisPassword'
    # str value
        # Administrator account password on FortiADC
CERT_NAME='letsencrypt_certificate'
    # str value
        # Name of certificate in FortiADC
SQUASH_SSL=True
    # bool value
        # True to squash SSL warnings