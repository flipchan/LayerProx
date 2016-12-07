How to run LayerProx with systemd, aka run it as a service in linux

set the directory
vim layerprox 
scp layerprox /etc/init.d/layerprox
echo ' ' > /run/layerprox.pid
scp layerprox.service /lib/systemd/system/layerprox.service
service layerprox start
