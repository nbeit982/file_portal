## Creating Service

Copy file `nbems_it_file_portal.service` under `linux_service` dir to `/etc/systemd/system/`

```
sudo cp ./linux_service/nbems_it_file_portal.service /etc/systemd/system/nbems_it_file_portal.service 
```

Now give executable permissions to `nbems_it_file_portal`

```
sudo chmod +x nbems_it_file_portal
```

## Starting the Service

```
sudo systemctl daemon-reload
sudo systemctl enable nbems_it_file_portal.service
sudo systemctl start nbems_it_file_portal
sudo systemctl status nbems_it_file_portal
```
