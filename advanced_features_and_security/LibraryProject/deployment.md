# Deployment HTTPS Configuration

To support the Django security settings, the production web server (Nginx) must be configured to handle SSL/TLS termination.

### Nginx Configuration Steps:
1. Install Certbot for Let's Encrypt:
   `sudo apt install certbot python3-certbot-nginx`

2. Run Certbot to generate certificates and auto-configure Nginx:
   `sudo certbot --nginx -d yourdomain.com`

3. Ensure the Nginx config includes the following headers to communicate with Django:
   ```nginx
   proxy_set_header X-Forwarded-Proto $scheme;