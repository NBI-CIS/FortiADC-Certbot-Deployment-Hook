# FortiADC Certbot Deployment Hook

This script is a method to automatically deploy renewed [Let's Encrypt](https://letsencrypt.org/) certificates via [Certbot](https://certbot.eff.org/) to a [Fortinet](https://www.fortinet.com/) [FortiADC](https://www.fortinet.com/products/application-delivery-controller/fortiadc.html) appliance.


## Installation

Ensure Python 3.6 is installed on the host

```bash
yum -y install python36 python36-pip
```

Make the directory for the script and change into it
```bash
mkdir -p /opt/fortiadc-deployment-hook
cd /opt/fortiadc-deployment-hook
```

Copy the script and configuration example down in your directory
Make the script executable
Modify the configuration to your environment
```bash
chmod +x ./fortiadc-deployment-hook.py
cp ./config-EXAMPLE.py ./config.py
vim ./config.py
```

Create a virtual environment for the script
Install the requests module
```bash
python36 venv/bin/activate
pip install requests
```

Add a Shebang to the begining of the script pointing at the correct Python environment
```bash
sed -i "1s;^;#!$( which python )\n;" ./fortiadc-deployment-hook.py
```

## Usage

You should now be able to test the deployment with the following pre-existing certbot configuration:

```bash
certbot renew --force-renewal --deploy-hook /opt/fortiadc-deployment-hook/fortiadc-deployment-hook.py
```

If this is successful, you can modify your certbot cron job to the following:

```bash
certbot renew --deploy-hook /opt/fortiadc-deployment-hook/fortiadc-deployment-hook.py
```

## Credits

**Adam Carrgilson** - *Initial work* - [carrgilson](https://github.com/carrgilson)

[Computing Infrastructure for Science](http://cis.nbi.ac.uk), supporting the [Norwich BioScience Institutes](http://www.nbi.ac.uk/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
