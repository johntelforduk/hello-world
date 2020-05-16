sudo yum -y update

yes | sudo amazon-linux-extras install nginx1.12
sudo cp flask.conf /etc/nginx/conf.d/+
sudo systemctl restart nginx

sudo yum -y install python3
sudo yum -y install git
git clone https://github.com/johntelforduk/hello-world.git
sudo pip3 install flask

echo python3 ./hello-world/hello-flask.py


