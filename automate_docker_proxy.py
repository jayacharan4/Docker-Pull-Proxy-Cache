import os
os.mkdir("/var/lib/registry-docker")
cmd = " sudo docker run -it --rm registry:2 cat \
       /etc/docker/registry/config.yml > /var/lib/registry-docker/config.yml"


os.system(cmd)

# File Appending Proxy Configurations 

fin = open("/root/Jay/Project_Files/proxy_config","r")
data = fin.read()
fin.close()

fout = open("/var/lib/registry-docker/config.yml","a")
fout.write(data)
fout.close()

cmd2 = "sudo docker run --restart=always -p 5000:5000 \
         --name v2-mirror -v /var/lib/registry-docker:/var/lib/registry \
         --detach registry:2 serve /var/lib/registry/config.yml "
os.system(cmd2)


cmd3 = "cp /root/Jay/Project_Files/daemon_config /etc/docker/daemon.json"
os.system(cmd3)

docker_cmd = "systemctl restart docker"
os.system(docker_cmd)




