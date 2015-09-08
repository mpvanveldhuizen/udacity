# Linux Server Configuration
### About
Project 5 of Udacity's Full Stack Web Developer Nanodegree consisting of a Linux Server Configuration. Where I took a baseline installation of a Linux distribution on a virtual machine and prepare it to host my catalog web application, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

### Linux Configurations
This will describe some of the Linux configurations.

1. IP address: `52.10.31.45`
2. Port:       `2200`
3. URL:			http://52.10.31.45/
4. Summary:

* Created a new Virtual Machine with my Udacity account
* Created a new user named grader
* Give the grader the permission to sudo
* Updated all currently installed packages
* Changed the SSH port from 22 to 2200
* Configured the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)
* Configured the local timezone to UTC
* Installed and configured Apache to serve a Python mod_wsgi application
* Installed and configured PostgreSQL:
  * Does not allow remote connections
  * Created a new user named catalog that has limited permissions to my catalog application database
* Installed git, clone and setup your Catalog App project, it functions correctly when visiting my server’s IP address in a browser. Made my git directory not publicly accessible via a browser.