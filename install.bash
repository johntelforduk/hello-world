sudo yum -y update

sudo yum -y install git
git clone https://github.com/johntelforduk/hello-world.git

yes | sudo amazon-linux-extras install nginx1.12
my_ip=$(curl http://checkip.amazonaws.com)
sudo cp hello-world/flask.conf /etc/nginx/conf.d/
sudo sed -i 's/$my_ip/'$my_ip'/g' /etc/nginx/conf.d/flask.conf

sudo systemctl restart nginx

sudo yum -y install python3
sudo pip3 install flask

python3 ./hello-world/hello-flask.py
